# SK네트웍스 Family AI 캠프 24기 3차 프로젝트
## 🏎️ F1을 쉽게！For every1

<p align="center">  
  <img src="https://github.com/user-attachments/assets/ca9539ed-dded-4755-b088-43c4e4bcb944" width="500" height="300" alt="image" />
</p>

## 1. 팀 소개 
  > F1에 익숙한 시선 1개와 낯선 시선 4개가 만나, 어렵고 복잡한 정보를 쉽고 친절하게 🔃새로고침하는 팀 **F5** 입니다❗
  
<table>
  <tr>
    <th width="200">김민준</th>
    <th width="200">김유진</th>
    <th width="200">박영훈</th>
    <th width="200">전윤우</th>
    <th width="200">최현진</th>
  </tr>
  <tr>
    <td align="center" width="200">
      <img src="./assets/images/mj.png" width="180" height="180" alt="mj" />
    </td>
    <td align="center" width="200">
      <img src="./assets/images/yj.png" width="180" height="180" alt="yj" />
    </td>
    <td align="center" width="200">
      <img src="./assets/images/yh.png" width="180" height="180" alt="yh" />
    </td>
    <td align="center" width="200">
      <img src="./assets/images/yw.png" width="180" height="180" alt="yw" />
    </td>
    <td align="center" width="200">
      <img src="./assets/images/hj.png" width="180" height="180" alt="hj" />
    </td>
  </tr>
  <tr>
    <td align="center" width="200">테스트케이스 설계<br>파인튜닝 / Git 관리</td>
    <td align="center" width="200">벡터DB / 임베딩<br>RAG 구현</td>
    <td align="center" width="200">데이터 전처리<br>파인튜닝 / 모델 평가</td>
    <td align="center" width="200">데이터 전처리<br>파인튜닝 / Streamlit 구현</td>
    <td align="center" width="200">아키텍처 설계<br>Agent 구현</td>
  </tr>
<tr>
    <td align="center" width="200">
      <a href="https://github.com/miin-jun"><img src="https://img.shields.io/badge/miin--jun-181717?style=for-the-badge&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="200">
      <a href="https://github.com/shortcut-2"><img src="https://img.shields.io/badge/youjin-181717?style=for-the-badge&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="200">
      <a href="https://github.com/aprkaos56"><img src="https://img.shields.io/badge/aprkaos56-181717?style=for-the-badge&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="200">
      <a href="https://github.com/Yunu-Jeon"><img src="https://img.shields.io/badge/Yunu--Jeon-181717?style=for-the-badge&logo=github&logoColor=white"></a>
    </td>
    <td align="center" width="200">
      <a href="https://github.com/lifeisgoodlg"><img src="https://img.shields.io/badge/lifeisgoodlg-181717?style=for-the-badge&logo=github&logoColor=white"></a>
    </td>
  </tr>
</table>

---

## 2. 프로젝트 개요

- 프로젝트 소개
  > F1 입문자를 위해 어려운 용어와 복잡한 규정을 쉽게 설명해주는 **한국어 기반 F1 전문 챗봇**입니다.  
  > 사용자의 질문 의도에 따라 규정집, 용어집, 과거 기록, 라운드별 경기 정보 등을 바탕으로 적절한 답변을 제공할 수 있도록 LLM 챗봇을 구현했습니다.  

- 프로젝트 필요성(배경)
  > 최근 국내에서 F1 경기에 대한 관심과 팬 유입이 증가하고 있지만, 입문자가 처음 접하기에는 F1의 용어와 규정이 매우 어렵고 복잡합니다.  
  > 특히, 규정은 매년 개정되기 때문에 단순 검색만으로는 정확한 정보를 이해하기 어렵습니다.  
  > 쿠팡플레이의 윤재수 F1 해설위원 또한 "국내엔 체계적으로 설명해 주는 자료나 교육 프로그램이 거의 없어 진입장벽이 높다"고 지적한 바 있습니다. ([출처](https://v.daum.net/v/xKESU0PKEy))  
  > 이에 따라, 입문자도 쉽고 빠르게 F1 정보를 이해할 수 있도록 돕는 챗봇의 필요성을 느껴 본 프로젝트를 기획하게 되었습니다.  

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/aa967686-65d9-467e-b108-83623113669e" width="400" alt="image1" /><br>
      <sub>출처: <a href="https://v.daum.net/v/HQc9YRwaEp">gpkorea 기사</a></sub>
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/aef35137-807a-4161-a7e8-7f99e2243cd8" width="700" alt="image3" /><br>
      <sub>출처: <a href="https://digitalchosun.dizzo.com/site/data/html_dir/2026/03/06/2026030680090.html"> 디지틀조선일보 기사</a></sub>
    </td>
  </tr>
</table>

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/0902f0e4-9a85-4c1f-8b0d-7ddb61e1639b" width="600" alt="image2" /><br>
  <sub>출처: <a href="https://www.chosun.com/sports/sports_general/2026/03/05/INS5ESTOJBEW3CJ3EC3RFBRPXY/">조선일보 기사</a></sub>
</p>


- 프로젝트 목표
  > F1 입문자가 자주 궁금해하는 용어, 규정, 경기 관련 정보를 한국어로 쉽고 정확하게 제공하는 챗봇을 구현하는 것을 목표로 합니다.  
  > 이를 위해 F1 규정집과 용어집을 비롯해 플래그, 타이어, 역사, F1 개요 등의 데이터를 RAG 기반으로 구축하고, 변화하는 규정과 다양한 질문 유형에 유연하게 대응할 수 있는 질의응답 시스템을 개발하고자 합니다.

---

## 3. 기술 스택 & 사용한 모델 (임베딩 모델, LLM)

| 분류 | 기술/도구 |
|---|---|
| Language | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| Orchestration | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=langchain&logoColor=3399FF) |
| Framework & API | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| VectorDB | ![ChromaDB](https://img.shields.io/badge/ChromaDB-5A31F4?style=for-the-badge&logo=databricks&logoColor=white) |
| Data Scraping | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge&logo=python&logoColor=white) |
| Fine-tuning | ![PEFT](https://img.shields.io/badge/PEFT-FF6F00?style=for-the-badge) |
| Infrastructure | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Runpod](https://img.shields.io/badge/Runpod-6C47FF?style=for-the-badge&logo=runpod&logoColor=white) |
| Demo & UI | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| Collaboration | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) |

| 분류 | 모델 |
|---|---|
| Embedding | ![intfloat/multilingual-e5-large](https://img.shields.io/badge/intfloat%2Fmultilingual--e5--large-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
| LLM | ![google/gemma-3-12b-it](https://img.shields.io/badge/google%2Fgemma--3--12b--it-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white) ![OpenAI-gpt-4o-mini](https://img.shields.io/badge/gpt--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white) |
| Re-ranker | ![CrossEncoder](https://img.shields.io/badge/CrossEncoder-00BFA5?style=for-the-badge&logo=scikitlearn&logoColor=white) |

### ▶️ 임베딩 모델 선정 이유
  > OpenAI 임베딩 모델(text-embedding-3-small/large) 테스트 결과, 사용자 쿼리 요청 시마다 API 비용이 발생하는 문제와 "패독", "피트레인", "피트스탑" 등 한글화된 F1 용어 인식 한계로 인해 다국어 특화 오픈소스 모델인 **intfloat/multilingual-e5-large**로 전환했습니다.  

### ▶️ LLM 모델 선택 이유
  > 1, 2차 테스트 결과, Qwen 계열 대비 gemma 모델이 할루시네이션이 적고, 언어 일관성 및 문장 구조가 안정적이었습니다.  
  최종적으로, 파라미터가 더 큰 **gemma-3-12b**를 선택하여 응답 품질을 높였습니다.

<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/7fecca53-9476-46bc-acf7-8b1243301153" />

  > 단, 한글 쿼리의 정확한 벡터 검색을 위해 번역 단계에서는 **GPT-4o-mini**를 활용하여 비용을 최소화하면서도 번역 품질을 확보했습니다.

### ▶️ 리랭커 모델 선정 이유
  > 벡터 검색만으로는 의미적으로 유사하지만 실제로는 관련 없는 문서가 상위에 올라오는 경우가 있어, 검색 정확도를 높이기 위해 리랭킹 단계를 추가했습니다.  
  > cross-encoder/mmarco-mMiniLMv2-L12-H384-v1은 14개 언어로 번역된 MS MARCO 데이터셋으로 학습된 다국어 크로스 인코더 모델로, 영어로 번역된 쿼리와 F1 문서 간의 유사도를 정밀하게 재정렬하는 데 적합합니다. 오픈소스로 추가 비용 없이 사용 가능한 점도 선택 이유 중 하나입니다.

---

## 4. 시스템 아키텍처
<img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/1724827c-0138-4f38-b015-36a81ff8e4ec" />

---

## 5. WBS
<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/4cadbbaa-3030-42af-b820-87f973ea7ec9" />

---

## 6. 요구사항 명세서
<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/57acdeb4-0b79-429f-a505-12822b60a37e" />

---

## 7. 수집한 데이터 및 전처리 요약

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/1b514ecc-ddbf-40ca-bb75-0536f786302d" width="450" alt="data1" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/85d81d71-2e98-4e20-aa55-be2e57b821cc" width="450" alt="data2" />
    </td>
  </tr>
</table>

<img width="1263" height="538" alt="image" src="https://github.com/user-attachments/assets/7ba40e16-c348-457d-8479-87d1ce6fce75" />

#### ✅ 요약
> 1. FIA 2026 F1 규정 PDF는 계층 구조를 보존하기 위해 Markdown으로 변환한 뒤, 조항(Article) 단위로 청킹하여 RAG 검색에 활용했습니다.  
> 2. Wikipedia, 서킷, 타이어, 용어 사전 데이터는 크롤링 또는 API 수집 후, 섹션·항목 단위로 청킹하여 JSON 형태로 정리했습니다.  
> 3. 전처리 과정에서는 빈 항목, 중복 데이터, 지나치게 짧거나 의미가 약한 본문을 제거하여 데이터 품질을 높였습니다.  

</table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/f7b2b2fb-9dba-4eb6-b5b5-eb9e1973bb41" width="450" alt="data3" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/47b87f1a-de16-4d0c-b873-bd9e6f4fdabd" width="450" alt="data4" />
    </td>
  </tr>
</table>

**데이터 개수**
| 구분 | 파일명 | 항목 수 |
|---|---|---:|
| 규정집 | section_a_general_provisions | 171 |
| 규정집 | section_b_sporting | 294 |
| 규정집 | section_c_technical | 651 |
| 규정집 | section_d_financial_f1_teams | 202 |
| 규정집 | section_f_operational | 76 |
| 가이드북 | f1_glossary | 224 |
| Wikipedia | f1_circuits | 78 |
| Wikipedia | f1_flags_wiki | 25 |
| Wikipedia | f1_history_wiki | 23 |
| Wikipedia | f1_intro_wiki | 36 |
| Pirelli | pirelli_f1_tires | 8 |
| FiA | steward_decisions | 16 |
|| **합계** | **1,804** |
> 규정 데이터(section_*)는 조항 단위, 그 외 데이터는 JSON 항목 단위로 집계

**데이터 출처**
| 출처 | url |
|---|:---|
| F1 규정 | https://www.fia.com/regulation/category/110 | 
| F1 용어 | https://www.formula1.com/en/page/f1-glossary | 
| F1 역사 | https://en.wikipedia.org/wiki/History_of_Formula_One | 
| F1 타이어 | https://www.pirelli.com/tires/en-us/motorsport/f1/tires | 
| F1 개요 | https://en.wikipedia.org/wiki/Formula_One |
| F1 깃발 | https://en.wikipedia.org/wiki/Racing_flags |  
| Jolpi.ca F1 API | https://api.jolpi.ca/ergast/ |  
| openf1 API | https://openf1.org/ |
>

---

## 8. DB 연동 구현 코드

<details>
<summary><b>🗄️ Database Connection (build_db.py)</b></summary>

> ChromaDB 연동 구현 코드 
> 전체 코드는 [여기](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN24-3rd-2Team/blob/29dba76607d9f463d24614a69c307257749203ec/src/retriever/build_db.py)에서 확인하실 수 있습니다.

```python

# ChromaDB 연동/벡터스토어 생성
def save_to_chroma(chunks: list[Document]):
    # 임베딩 모델 설정
    embedding_model = HuggingFaceEmbeddings(
        model_name="intfloat/multilingual-e5-large",
        model_kwargs={"device": "cuda"},
        encode_kwargs={
            "normalize_embeddings": True, 
            "prompt": "passage: "
            },
    )
    # 기존 벡터 DB 초기화/신규 생성
    if os.path.exists(VECTOR_DIR):
        shutil.rmtree(VECTOR_DIR)
    os.makedirs(VECTOR_DIR, exist_ok=True)

    # Chroma DB 구축
    vector_store = Chroma.from_documents(
        chunks,
        embedding=embedding_model,
        persist_directory=VECTOR_DIR,
        collection_name="f1_rules_e5",
    )
    print(f"벡터 저장 완료: {vector_store._collection.count()}개 청크")

```
</details>

---

## 9. 테스트 계획 및 결과 보고서

### ✅ 테스트 개요

  > 본 테스트는 F1 입문자용 챗봇이 사용자의 질문에 대해 **정확하고 이해하기 쉬운 답변**을 제공하는지 검증하기 위해 수행하였습니다.
  > 특히, **FIA 규정, F1 용어, 플래그, 역사, 스튜어드 판정문**을 기반으로 한 질의응답 품질과 한국어 설명 능력을 중점적으로 평가하였습니다.

#### 테스트 목적
  > 1. 규정 기반 질의응답의 정확성 검증  
  > 2. 한국어 질문 이해 및 응답 생성 능력 검증  
  > 3. 입문자 친화적인 쉬운 설명 제공 여부 검증  
  > 4. 시스템 응답 속도 및 서비스 안정성 검증

### ✅ 테스트 항목

- 질의응답 정확성
  > FIA 규정을 근거로 정확한 답변을 제공하는가?  
  > 용어, 플래그, 역사, 판정문 관련 질문에도 올바르게 응답하는가?

- 한국어 자연어 이해 능력
  > 한국어 질문 의도를 정확히 파악하는가?  
  > 동일 의미의 다양한 표현에도 적절히 응답하는가?

- 쉬운 설명 변환 능력
  > 초보자가 이해하기 어려운 기술 용어나 규정을 쉽게 풀어서 설명하는가?  
  > 불필요하게 어려운 표현 없이 자연스럽게 설명하는가?

- 응답 시간 및 성능
  > 평균 응답 시간이 10초 이내인가?  
  > 질문 유형이 달라져도 일관된 속도로 응답하는가?


### ✅ 테스트 케이스

| 테스트 ID | 질문 | 테스트 목적 |
|---|---|---|
| **F1QA001** | F1 바닥에 있는 플랭크는 그냥 보호판 같은 건가요? 두께 기준도 있나요? | 기술 규정 기반 상세 조건 이해 평가 |
| **F1QA002** | 피트레인에서는 무조건 시속 80km 이하로 달려야 하나요? 넘으면 바로 벌점 받나요? | 경기 운영 규정 및 제재 방식 이해 평가 |
| **F1QA003** | 폭염 경기에서는 드라이버 냉각장치를 아무거나 달아도 되나요? | 운영 규정 기반 조건 이해 평가 |
| **F1QA004** | 더블 웨이브 옐로우가 나온 구간에서 예선 랩을 계속 밀어붙이면 어떻게 되나요? | 스포츠 규정 기반 제재 이해 평가 |
| **F1QA005** | 2026년에 말하는 ‘액티브 에어로’는 예전 DRS랑 같은 건가요? | 용어·개념 비교 설명 평가 |
| **F1QA006** | 에어로 레이크는 차 성능을 높이는 부품인가요? | 용어 정의 및 오개념 교정 평가 |
| **F1QA007** | F1 예산 제한은 그냥 “돈을 이 이상 쓰면 안 된다”는 뜻인가요? | 재무 규정 맥락 이해 평가 |
| **F1QA008** | 왜 1952~1953년에는 원래 F1 규정이 아니라 다른 규정이 쓰였나요? | 역사적 배경 설명 능력 평가 |

#### 평가 기준
- **정확성**: 규정/원문과 일치하는가?
- **이해성**: 한국어 문장이 자연스럽고 의미 전달이 명확한가?
- **친절성**: 초보자도 이해할 수 있도록 쉬운 표현을 사용하는가?
- **응답시간**: 응답 생성 시간이 10초 이내인가?

`평가는 각 문항별로 수동 검토 방식으로 진행하였으며, 필요 시 원문 규정과 대조하여 사실 여부를 재확인하였습니다.`


### ✅ 테스트 진행 과정 및 결과
  > 1. 평가자: F1 비경험자 3인 (일반 사용자 관점)  
  > 2. 평가 항목: 정확성 / 이해 용이성 / 친절도 / 응답시간 (5점 만점)  
  > 3. 테스트 케이스: 8개  
  > 4. 서비스 가능 기준: 4개 항목 평균 3.5점 이상

  <img width="1328" height="303" alt="image" src="https://github.com/user-attachments/assets/d9872506-facb-4dc2-945f-0324174f297a" />
  
  > 종합 평균: 4.05 / 5.0 (Pass 8/8)

  > 항목별 평균: 친절도 4.19 · 응답시간 4.0 · 정확성 3.9 · 이해 용이성 3.8

  > 테스트 결과, 챗봇은 **대다수의 규정 기반 질문에 대해 정확한 답변**을 제공하였으며,  
  > 용어 설명과 조건형 질문에서도 **안정적인 성능**을 보였습니다.  
  > 특히, 단순 정의형 질문과 조문 근거가 명확한 질문에서는 **높은 정확도**를 보였습니다.

#### 확인된 개선 필요 사항
  > 일부 기술 규정 질문에서 답변이 조문 수준으로 딱딱하게 출력되는 경우가 있습니다.  
  > 예외 조항이 포함된 질문에서는 설명이 길어져 초보자 관점에서 다소 어렵게 느껴질 수 있습니다.  
  > 한국어 문장은 전반적으로 자연스러웠으나, 일부 용어는 추가적인 쉬운 풀이가 필요합니다.  
  > 응답 생성 시간이 비교적 오래 걸리므로, 최적화가 필요합니다.

### ✅ 종합 평가

  > 본 테스트를 통해 F1 입문자용 챗봇은 입문자 사용자를 대상으로 한 **규정 설명 서비스로서 기본적인 정확성과 설명 가능성**을 확보하였음을 확인하였습니다.  
  > 향후에는 **예외 조항 설명 간소화**, **기술 용어의 쉬운 재서술**, **응답 속도 최적화**를 통해 사용자 친화성을 더욱 높일 필요가 있습니다.

---

## 10. 진행 과정 중 프로그램 개선 노력

### 1. 프롬프트 엔지니어링
- **Problem:**
  > F1 규정 원문은 표현이 복잡하고 전문 용어가 많아, 그대로 답변할 경우 입문자가 이해하기 어려운 문제가 있었습니다.
- **Solution:**
  > 이를 개선하기 위해 규정 조문을 바탕으로 입문자 친화적인 한국어 질문-답변 데이터를 생성하는 프롬프트를 설계했습니다.
  > 프롬프트에는 규정 외 내용 추측 금지, 숫자·조건·예외 유지, 쉬운 한국어 설명, 자연스러운 입문자 질문 생성 등의 기준을 반영해, 복잡한 원문 규정을 초보자도 이해하기 쉬운 학습 데이터로 변환할 수 있도록 했습니다.

### 2. 파인 튜닝

- **Problem:**
  > 규정집 원문만 기반으로 검색할 경우, 질문과 직접 관련 없는 조항이 함께 검색되거나 사용자의 일상적인 질문 표현과 규정 문장 사이의 차이로 인해 관련 조항을 정확히 찾기 어려운 문제가 있었습니다. 그 결과, 단순 유사도 검색만으로는 답변 정확도가 떨어질 수 있었습니다.

- **Solution:**
  > 이를 보완하기 위해 실제 사용자 관점에서 자주 나올 수 있는 규정 기반 질문-답변 데이터를 직접 구축했습니다. 조항별 핵심 내용을 자연스러운 사용자 질문 형태로 변환하고, 중복되거나 불명확한 샘플은 필터링해 학습 데이터를 정제했습니다.  
  > 이후 QLoRA 기반 파인튜닝을 적용하여, 모델이 일상적인 표현의 질문도 규정 문맥에 맞게 해석하고 보다 정확하고 이해하기 쉬운 답변을 생성할 수 있도록 개선했습니다.

**▶️ Finetune 데이터 개수**
| 항목 | 개수 |
|---|---:|
| section_a_general_provisions + section_b_sporting | 3,502 |
| section_c_technical | 4,115 |
| section_d_financial_f1_teams + section_f_operational| 895 |
| f1_glossary + f1_history_wiki | 1,570 |
| f1_flags + pirelli_f1_tires + f1_intro | 1,449 |
| jolpi_ca | 3,729 |
| **총 개수** | **15,260** |

```
{"messages": [{"role": "user", "content": "경기가 최소 몇 대의 F1 차량이 있어야 정상적으로 진행될 수 있나요?"}, {"role": "assistant", "content": "경기는 최소 12대 이상의 F1 차량이 있어야 진행할 수 있습니다. 12대 미만이면 경기가 연기되거나 취소될 수 있습니다."}]}
{"messages": [{"role": "user", "content": "대회가 연기되거나 취소될 수 있는 공식적인 규정은 무엇인가요?"}, {"role": "assistant", "content": "경기는 국제 스포츠 규정(ISC)에 따라 연기되거나 취소될 수 있습니다."}]}
{"messages": [{"role": "user", "content": "F1 경기가 12대 차량이 준비되지 않았을 때 어떤 조치를 취해야 하나요?"}, {"role": "assistant", "content": "12대 미만일 경우 경기 자체를 연기하거나 취소하는 조치가 가능합니다."}]}
{"messages": [{"role": "user", "content": "'국제 스포츠 규정(ISC)'란 대회 연기나 취소에 어떤 역할을 하나요?"}, {"role": "assistant", "content": "ISC는 경기를 공식적으로 연기하거나 취소하는 절차와 기준을 정해주는 규정입니다."}]}
{"messages": [{"role": "user", "content": "만약 경기가 연기된다면 어떤 상황에서 그럴 가능성이 높나요?"}, {"role": "assistant", "content": "차량이 12대 미만으로 부족하거나 ISC가 정한 다른 특별한 이유가 있을 때 경기가 연기될 수 있습니다."}]}
{"messages": [{"role": "user", "content": "경기 취소와 연기, 둘 중 하나만 가능합니까?"}, {"role": "assistant", "content": "두 가지 모두 가능합니다. 상황에 따라 국제 스포츠 규정에 의거해 경기 연기 또는 취소가 결정됩니다."}]}
```

### ▶️ Gemma3-12B - Base 모델 vs Finetuned 모델 비교

<img width="766" height="548" alt="image" src="https://github.com/user-attachments/assets/295fe45d-fa1a-43de-bf2a-fda880512fa1" />

> 모델 평가는 **BERTScore**, **ROUGE-L**, **Perplexity**를 사용하여 각각 의미 유사도, 표현 유사도, 문장 자연스러움을 함께 확인했습니다.  
> 평가 결과, 파인튜닝 모델은 **BERTScore에서 통계적으로 유의미한 향상**을 보여 의미적 답변 품질이 개선된 것으로 확인되었습니다.  
> 반면 **ROUGE-L**과 **Perplexity**에서는 유의미한 차이가 크지 않아, 표현 유사도와 유창성 측면의 개선은 제한적이었습니다.  
> 따라서 본 프로젝트에서는 **의미 정확도가 중요한 질의에 대해 파인튜닝 모델을 우선적으로 활용하는 것이 적절하다**고 판단했습니다.

#### ▶️ 링크 : [HuggingFace](https://huggingface.co/YHPark0208/SKN24_3rd_2Team)

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/589a1509-e030-4ad1-baa0-4c36653893c3" height="400" alt="image1" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/c9a413a5-9004-48ac-8277-ea243372a235" height="400" alt="image2" />
    </td>
  </tr>
</table>

---

## 11. 수행결과

<img width="2852" height="1051" alt="image" src="https://github.com/user-attachments/assets/9d7eb9a6-4dcf-45fe-b951-85dda5119800" />
<img width="1610" height="906" alt="image" src="https://github.com/user-attachments/assets/ff6ad80b-1e1f-4d92-a12f-45cc2212d76b" />

---

## 12. 한 줄 회고
- 김민준
  > 이번 프로젝트에서 초기 시스템 설계를 명확히 하지 못한 채 데이터 전처리부터 파인튜닝, 모델 성능 비교, 학습 데이터 생성까지 진행하며 시행착오가 많았고, AI 의존도가 높았던 점이 아쉬움으로 남았습니다. 그리고 다음 프로젝트에서는 전체 파이프라인 구조를 먼저 설계하고, 코드 한 줄 한 줄의 의미를 스스로 이해하며 구현하는 습관을 길러 더 주도적으로 개발할 수 있도록 노력하고 싶습니다.

- 김유진
  > 이전 프로젝트보다 초기 단계에서 데이터 구조를 좀 더 이해하려 노력했습니다. 그 결과, 금번 프로젝트의 데이터를 PDF→Markdown으로 전처리하는 방식을 제안, 데이터 손실을 최소화하여 RAG 답변 정확도를 높였습니다. 팀원들과 아키텍처와 기능에 대해서 충분히 공유했다고 생각했으나, 진행하며 팀원 간 아키텍처 이해도가 달라 재작업이 발생했습니다. 차후 프로젝트에서는 요구사항 명세서와 WBS를 시작 전 확정하고, 매일 스크럼 하는 방식을 통해 명료한 커뮤니케이션으로 프로젝트의 방향성을 명확히 설정하겠습니다.

- 박영훈
  > 이번 프로젝트를 통해 프롬프트 설계가 챗봇의 답변 품질을 결정하는 중요한 요소임을 다시 한번 체감할 수 있었습니다. 특히 사용자 친화적인 챗봇 구현을 목표로 하면서, “초보자도 이해하기 쉽게 설명”, “답변은 2~4문장으로 구성”과 같은 세밀한 조건 설정이 필요하다는 점을 재차 확인했습니다. 추후에는 사용자의 관점에서 요구를 더욱 구체적으로 파악하고, 이에 맞는 프롬프트를 설계하는 과정이 중요할 것이라고 생각합니다.

- 전윤우
  > 프로젝트를 통해 sLLM을 활용한 RAG 챗봇이 전체적으로 어떤 플로우로 진행되는지를 파악할 수 있었습니다. sLLM 모델을 활용해서 답변에 좋은 성능을 내는 과정이 쉽지 않았으며, 파인 튜닝에 있어서도 전체적인 파이프라인은 이해했으나 학습 데이터 생성이나 구현에 있어 아쉬운 점이 많았습니다. 시스템의 큰 나무를 팀원들과 함께 먼저 의논하고구획한 후에 세부적인 내용을 논의하는 것이 효과적인 협업임을 배웠습니다.

- 최현진
  > 이번 프로젝트를 하면서 시스템 구조를 설계하는 것에 대한 중요성을 크게 체감했습니다. 초기에 시스템의 구조를 명확히 정하지 않아 개발 중간에 팀원들과 구조에 대한 지속적인 회의를 진행해야만 했습니다. 다음에는 개발 시작 전에 시스템의 구조를 먼저 구체적으로 정의하고 설계를 진행하고 싶습니다.
