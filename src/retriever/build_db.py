import os
import json
import shutil
import glob
import re
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from collections import defaultdict

DATA_DIR = "/workspace/SKN24-3rd-2Team/data/processed"
# DATA_DIR = "/workspace/data/processed"
VECTOR_DIR = "/workspace/SKN24-3rd-2Team/vectorstore/chroma_f1_e5"

# steward_decisions.json 로드
def load_steward_decisions() -> list[Document]:
    with open(f"{DATA_DIR}/steward_decisions.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []
    for i, item in enumerate(data):
        grand_prix = item.get("grand_prix", "").strip()
        year = item.get("year", "")
        fact = item.get("fact", "").strip()
        infringement = item.get("infringement", "").strip()
        decision = item.get("decision", "").strip()
        reason = item.get("reason", "").strip()

        if not fact or not reason:
            continue

        content = (
            f"Grand Prix: {grand_prix} {year}\n"
            f"Fact: {fact}\n"
            f"Infringement: {infringement}\n"
            f"Decision: {decision}\n"
            f"Reason: {reason}"
        )

        doc = Document(
            page_content=content,
            metadata={"source": item.get("source", ""), "doc_type": "steward_decision", "grand_prix": grand_prix, "year": year},
        )
        docs.append(doc)

    return docs


# glossary.json 로드
def load_glossary() -> list[Document]:
    with open(f"{DATA_DIR}/f1_glossary_all.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = []
    for i, item in enumerate(data):
        term = item.get("term", "").strip()
        desc = item.get("description", "").strip()

        if not term or not desc:
            continue

        doc = Document(
            page_content=f"Term: {term}\nDescription: {desc}",
            metadata={"source": "f1_glossary_all.json", "doc_type": "glossary", "row": i, "term": term},
        )
        docs.append(doc)

    return docs


# history_wiki.json 로드
def load_wiki() -> list[Document]:
    with open(f"{DATA_DIR}/f1_history_wiki.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, str):
        text = data
    else:
        text = json.dumps(data, ensure_ascii=False)

    doc = Document(
        page_content=text,
        metadata={"source": "f1_history_ko_wiki.json", "doc_type": "wiki"},
    )
    return [doc]


# regulations.md 로드
def load_regulations() -> list[Document]:
    docs = []

    md_files = glob.glob(f"{DATA_DIR}/*.md")
    for md_path in md_files:
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()

        filename = os.path.basename(md_path)

        doc = Document(
            page_content=text,
            metadata={"source": filename, "doc_type": "regulation"},
        )
        docs.append(doc)

    return docs


# tire.txt 로드
def load_tires() -> list[Document]:
    with open(f"{DATA_DIR}/pirelli_f1_tires.txt", "r", encoding="utf-8") as f:
        text = f.read()

    doc = Document(
        page_content=text,
        metadata={"source": "pirelli_f1_tires.txt", "doc_type": "tires"},
    )
    return [doc]


# 청킹 
def get_article_group(article_str: str) -> str:
    clean = re.sub(r'\*+', '', article_str).strip()
    match = re.match(r'(B\d+\.\d+)', clean)

    if match:
        return match.group(1)
    return clean


def split_by_header(docs: list[Document]) -> list[Document]:
    md_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[("##", "article")],
        strip_headers=False,
    )

    chunks = []
    for doc in docs:
        for split in md_splitter.split_text(doc.page_content):
            split.metadata.update({
                "source": doc.metadata["source"],
                "doc_type": "regulation",
            })
            chunks.append(split)

    return chunks


def merge_by_article(chunks: list[Document]) -> list[Document]:
    grouped = defaultdict(list)
    for chunk in chunks:
        article = chunk.metadata.get("article", "")
        key = (chunk.metadata["source"], get_article_group(article))
        grouped[key].append(chunk.page_content)

    merged = []
    for (source, article), contents in grouped.items():
        text = "\n\n".join(contents)
        doc = Document(
            page_content=text,
            metadata={"source": source, "doc_type": "regulation", "article": article},
        )
        merged.append(doc)

    return merged


def chunk_regulations(docs: list[Document], splitter) -> list[Document]:
    header_chunks = split_by_header(docs)
    split_chunks = splitter.split_documents(header_chunks)
    merged = merge_by_article(split_chunks)
    return splitter.split_documents(merged)


def chunk_all(glossary, other_docs, regulation_docs) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=400,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    other_chunks = splitter.split_documents(other_docs)
    reg_chunks = chunk_regulations(regulation_docs, splitter)

    return glossary + other_chunks + reg_chunks


# 벡터 저장
def save_to_chroma(chunks: list[Document]):
    embedding_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cuda"},
        encode_kwargs={
            "normalize_embeddings": True, 
            "prompt": "passage: "
            },
    )

    if os.path.exists(VECTOR_DIR):
        shutil.rmtree(VECTOR_DIR)
    os.makedirs(VECTOR_DIR, exist_ok=True)

    vector_store = Chroma.from_documents(
        chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DIR,
        collection_name="f1_rules_e5",
    )
    print(f"벡터 저장 완료: {vector_store._collection.count()}개 청크")


# 코드 실행 부분
glossary = load_glossary()
wiki = load_wiki()
tires = load_tires()
regs = load_regulations()
steward_docs = load_steward_decisions()

chunks = chunk_all(glossary, wiki + tires + steward_docs, regs)
print(f"최종 chunk 수: {len(chunks)}")

save_to_chroma(chunks)