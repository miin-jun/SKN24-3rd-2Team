# SK네트웍스 Family AI 캠프 24기 3차 프로젝트
## 🏎️ F1을 쉽게！For every1
### 1. 팀 소개
  > F1에 익숙한 시선 1개와 낯선 시선 4개가 만나, 어렵고 복잡한 정보를 쉽고 친절하게 🔃새로고침하는 팀 **F5**입니다.
  
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
    <td align="center" width="200"><a href="https://github.com/miin-jun">miin-jun</a></td>
    <td align="center" width="200"><a href="https://github.com/shortcut-2">youjin</a></td>
    <td align="center" width="200"><a href="https://github.com/aprkaos56">aprkaos56</a></td>
    <td align="center" width="200"><a href="https://github.com/Yunu-Jeon">Yunu-Jeon</a></td>
    <td align="center" width="200"><a href="https://github.com/lifeisgoodlg">lifeisgoodlg</a></td>
  </tr>
</table>


### 2. 프로젝트 개요
- 프로젝트 명
  > F1을 쉽게! For every1
- 프로젝트 소개
  > F1 입문자를 위해 어려운 용어와 복잡한 규정을 쉽게 설명해주는 한국어 기반 F1 전문 챗봇입니다. 사용자의 질문 의도에 따라 규정집, 용어집, 과거 기록, 라운드별 경기 정보 등을 바탕으로 적절한 답변을 제공할 수 있도록 구현하였습니다.
- 프로젝트 필요성(배경)
  > 최근 국내에서 F1 경기에 대한 관심과 팬 유입이 증가하고 있지만, 입문자가 처음 접하기에는 F1의 용어와 규정이 매우 어렵고 복잡합니다. 특히 규정은 매년 개정되기 때문에 단순 검색만으로는 정확한 정보를 이해하기 어렵습니다. 이에 따라, 입문자도 쉽고 빠르게 F1 정보를 이해할 수 있도록 돕는 챗봇의 필요성을 느껴 본 프로젝트를 기획하였습니다.
- 프로젝트 목표
  > F1 입문자가 자주 궁금해하는 용어, 규정, 경기 관련 정보를 한국어로 쉽고 정확하게 제공하는 챗봇을 구현하는 것을 목표로 합니다. 이를 위해 F1 규정집과 용어집을 비롯해 플래그, 타이어, 역사, F1 개요 등의 데이터를 RAG 기반으로 구축하고, 변화하는 규정과 다양한 질문 유형에 유연하게 대응할 수 있는 질의응답 시스템을 개발하였습니다.

### 3. 기술 스택 & 사용한 모델 (임베딩 모델, LLM)

| 분류 | 기술/도구 |
|---|---|
| 언어 | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| LLM 프레임워크 | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge) ![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge) |
| 모델 / 추론 | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| 벡터DB / 검색 | ![ChromaDB](https://img.shields.io/badge/ChromaDB-5A31F4?style=for-the-badge) |
| 웹 파싱 | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge) |
| 개발 환경 | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Runpod](https://img.shields.io/badge/Runpod-6C47FF?style=for-the-badge) |
| UI | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| 협업 도구 | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) |

| 분류 | 모델 |
|---|---|
| Embedding 모델 | ![intfloat/multilingual-e5-large](https://img.shields.io/badge/intfloat%2Fmultilingual--e5--large-FF6600?style=for-the-badge) ![OpenAI Embeddings](https://img.shields.io/badge/OpenAI%20Embeddings-FF6600?style=for-the-badge) |
| LLM | ![google/gemma-3-12b-it](https://img.shields.io/badge/google%2Fgemma--3--12b--it-FF6600?style=for-the-badge) ![OpenAI API](https://img.shields.io/badge/OpenAI%20API-FF6600?style=for-the-badge) |
| Re-ranker | ![CrossEncoder](https://img.shields.io/badge/CrossEncoder-FF6600?style=for-the-badge) |

### 4. 시스템 아키텍처
<img width="500" height="600" alt="image" src="https://github.com/user-attachments/assets/1724827c-0138-4f38-b015-36a81ff8e4ec" />

### 5. WBS

### 6. 요구사항 명세서

### 7. 수집한 데이터 및 전처리 요약

### 8. DB 연동 구현 코드 (링크만)

### 9. 테스트 계획 및 결과 보고서

### 10. 진행 과정 중 프로그램 개선 노력

### 11. 수행결과(테스트/시연 페이지)

### 12. 한 줄 회고
- 김민준
> 안녕하세요

- 김유진
> 안녕하세요

- 박영훈
> 안녕하세요

- 전윤우
> 안녕하세요

- 최현진
> 안녕하세요
