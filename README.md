# SK네트웍스 Family AI 캠프 24기 3차 프로젝트
## 🏎️ F1을 쉽게！For every1

<p align="center">  
  <img src="https://github.com/user-attachments/assets/ca9539ed-dded-4755-b088-43c4e4bcb944" width="500" height="300" alt="image" />
</p>

### 0️⃣ 팀 소개 
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

### 1️⃣ 프로젝트 개요

- 프로젝트 소개
  > F1 입문자를 위해 어려운 용어와 복잡한 규정을 쉽게 설명해주는 **한국어 기반 F1 전문 챗봇**입니다.  
  > 사용자의 질문 의도에 따라 규정집, 용어집, 과거 기록, 라운드별 경기 정보 등을 바탕으로 적절한 답변을 제공할 수 있도록 LLM 챗봇을 구현했습니다.  

- 프로젝트 필요성(배경)
  > 최근 국내에서 F1 경기에 대한 관심과 팬 유입이 증가하고 있지만, 입문자가 처음 접하기에는 F1의 용어와 규정이 매우 어렵고 복잡합니다.  
  > 특히, 규정은 매년 개정되기 때문에 단순 검색만으로는 정확한 정보를 이해하기 어렵습니다.  
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

### 2️⃣ 기술 스택 & 사용한 모델 (임베딩 모델, LLM)

| 분류 | 기술/도구 |
|---|---|
| Language | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| Orchestration | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white) ![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=langchain&logoColor=3399FF) |
| Framework & API | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| VectorDB | ![ChromaDB](https://img.shields.io/badge/ChromaDB-5A31F4?style=for-the-badge&logo=databricks&logoColor=white) |
| Data Scraping | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge&logo=python&logoColor=white) |
| Infrastructure | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Runpod](https://img.shields.io/badge/Runpod-6C47FF?style=for-the-badge&logo=runpod&logoColor=white) |
| Demo & UI | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| Collaboration | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) |

| 분류 | 모델 |
|---|---|
| Embedding | ![intfloat/multilingual-e5-large](https://img.shields.io/badge/intfloat%2Fmultilingual--e5--large-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
| LLM | ![google/gemma-3-12b-it](https://img.shields.io/badge/google%2Fgemma--3--12b--it-8E75B2?style=for-the-badge&logo=google-gemini&logoColor=white) ![OpenAI-gpt-4o-mini](https://img.shields.io/badge/gpt--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white) |
| Re-ranker | ![CrossEncoder](https://img.shields.io/badge/CrossEncoder-00BFA5?style=for-the-badge&logo=scikitlearn&logoColor=white) |


---

### 3️⃣ LLM 모델 선택 이유
  > 1, 2차 테스트 결과, Qwen 계열 대비 gemma 모델이 할루시네이션이 적고, 언어 일관성 및 문장 구조가 안정적이었습니다.  
  최종적으로, 파라미터가 더 큰 **gemma-3-12b**를 선택하여 응답 품질을 높였습니다.

### 4️⃣ 임베딩 모델 선정 이유
  > OpenAI 임베딩 모델(small/large) 테스트 결과, 사용자 쿼리 요청 시마다 API 비용이 발생하는 문제와 "패독", "피트레인" 등 한글화된 F1 용어 인식 한계로 인해 다국어 특화 오픈소스 모델인 intfloat/multilingual-e5-large로 전환했습니다.  
  > 단, 한글 쿼리의 정확한 벡터 검색을 위해 번역 단계에서는 **GPT-4o-mini**를 활용하여 비용을 최소화하면서도 번역 품질을 확보했습니다.

<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/7fecca53-9476-46bc-acf7-8b1243301153" />

---

### 5️⃣ 시스템 아키텍처
<img width="600" height="800" alt="image" src="https://github.com/user-attachments/assets/1724827c-0138-4f38-b015-36a81ff8e4ec" />

---

### 6️⃣ WBS
<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/4cadbbaa-3030-42af-b820-87f973ea7ec9" />

---

### 7️⃣ 요구사항 명세서
<img width="1700" height="900" alt="image" src="https://github.com/user-attachments/assets/9d3eb164-618d-41c4-a546-cfe693bc018f" />


---

### 8️⃣ 수집한 데이터 및 전처리 요약

<table>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/1b514ecc-ddbf-40ca-bb75-0536f786302d" width="450" alt="data1" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/85d81d71-2e98-4e20-aa55-be2e57b821cc" width="450" alt="data2" />
    </td>
  </tr>
  <tr>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/f7b2b2fb-9dba-4eb6-b5b5-eb9e1973bb41" width="450" alt="data3" />
    </td>
    <td align="center" width="50%">
      <img src="https://github.com/user-attachments/assets/d7e15075-ba65-41ea-855d-af7ae002b0ae" width="450" alt="data4" />
    </td>
  </tr>
</table>
<img width="1263" height="538" alt="image" src="https://github.com/user-attachments/assets/7ba40e16-c348-457d-8479-87d1ce6fce75" />

**데이터 개수**
| 데이터셋 | 항목 수 |
|---|---:|
| section_a_general_provisions | 171 |
| section_b_sporting | 294 |
| section_c_technical | 651 |
| section_d_financial_f1_teams | 202 |
| section_f_operational | 76 |
| f1_glossary | 224 |
| f1_circuits | 78 |
| f1_flags_wiki | 25 |
| f1_history_wiki | 23 |
| f1_intro_wiki | 36 |
| pirelli_f1_tires | 8 |
| steward_decisions | 16 |
| **총 데이터 항목 수** | **1,804 건** |

**Finetune 데이터 개수**

| 항목 | 개수 |
|---|---:|
| Finetune된 데이터 개수 | 15,260 건 |

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

---

### 9️⃣ DB 연동 구현 코드 (링크만)

---

### 🔟 테스트 계획 및 결과 보고서

#### 1) 테스트 개요

  > 본 테스트는 F1 입문자용 챗봇이 사용자의 질문에 대해 **정확하고 이해하기 쉬운 답변**을 제공하는지 검증하기 위해 수행하였습니다.
  > 특히, **FIA 규정, F1 용어, 플래그, 역사, 스튜어드 판정문**을 기반으로 한 질의응답 품질과 한국어 설명 능력을 중점적으로 평가하였습니다.

##### 테스트 목적
  > 규정 기반 질의응답의 정확성 검증  
  > 한국어 질문 이해 및 응답 생성 능력 검증  
  > 입문자 친화적인 쉬운 설명 제공 여부 검증  
  > 시스템 응답 속도 및 서비스 안정성 검증

#### 2) 테스트 항목

##### 2-1. 질의응답 정확성
  > FIA 규정을 근거로 정확한 답변을 제공하는가?  
  > 용어, 플래그, 역사, 판정문 관련 질문에도 올바르게 응답하는가?

##### 2-2. 한국어 자연어 이해 능력
  > 한국어 질문 의도를 정확히 파악하는가?  
  > 동일 의미의 다양한 표현에도 적절히 응답하는가?

##### 2-3. 쉬운 설명 변환 능력
  > 초보자가 이해하기 어려운 기술 용어나 규정을 쉽게 풀어서 설명하는가?  
  > 불필요하게 어려운 표현 없이 자연스럽게 설명하는가?

##### 2-4. 응답 시간 및 성능
  > 평균 응답 시간이 10초 이내인가?  
  > 질문 유형이 달라져도 일관된 속도로 응답하는가?


#### 3) 테스트 케이스

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

##### 평가 기준
- **정확성**: 규정/원문과 일치하는가?
- **이해성**: 한국어 문장이 자연스럽고 의미 전달이 명확한가?
- **친절성**: 초보자도 이해할 수 있도록 쉬운 표현을 사용하는가?
- **응답시간**: 응답 생성 시간이 10초 이내인가?

`평가는 각 문항별로 수동 검토 방식으로 진행하였으며, 필요 시 원문 규정과 대조하여 사실 여부를 재확인하였습니다.`

#### 4) 테스트 결과

  > 테스트 결과, 챗봇은 **대다수의 규정 기반 질문에 대해 정확한 답변**을 제공하였으며,  
  > 용어 설명과 조건형 질문에서도 **안정적인 성능**을 보였습니다.  
  > 특히, 단순 정의형 질문과 조문 근거가 명확한 질문에서는 **높은 정확도**를 보였습니다.  
  > 하지만 응답 시간이 평균 **10~20초의 시간**이 소요되었습니다.

##### 확인된 개선 필요 사항
  > 일부 기술 규정 질문에서 답변이 조문 수준으로 딱딱하게 출력되는 경우가 있습니다.  
  > 예외 조항이 포함된 질문에서는 설명이 길어져 초보자 관점에서 다소 어렵게 느껴질 수 있습니다.  
  > 한국어 문장은 전반적으로 자연스러웠으나, 일부 용어는 추가적인 쉬운 풀이가 필요합니다.  
  > 응답 생성 시간이 비교적 오래 걸리므로, 최적화가 필요합니다.

#### 5) 종합 평가

  > 본 테스트를 통해 F1 입문자용 챗봇은 입문자 사용자를 대상으로 한 **규정 설명 서비스로서 기본적인 정확성과 설명 가능성**을 확보하였음을 확인하였습니다.  
  > 향후에는 **예외 조항 설명 간소화**, **기술 용어의 쉬운 재서술**, **응답 속도 최적화**를 통해 사용자 친화성을 더욱 높일 필요가 있습니다.

---

### 📒 진행 과정 중 프로그램 개선 노력

#### 1. 프롬프트 엔지니어링
- F1 규정 원문은 표현이 복잡하고 전문 용어가 많아, 그대로 답변할 경우 입문자가 이해하기 어려운 문제가 있었습니다.
- 이를 개선하기 위해 한국어 설명형 답변 중심으로 프롬프트를 설계하여, 규정의 핵심 내용을 쉽고 자연스럽게 풀어서 설명할 수 있도록 개선했습니다.

#### 2. Q 데이터셋
- 규정집 원문만 검색할 경우 질문과 직접 관련 없는 조항이 함께 검색되어, 답변 정확도가 떨어지는 문제가 있었습니다.
- 이를 보완하기 위해 실제 사용자 관점에서 자주 나올 수 있는 질문 형태의 Q 데이터셋을 구축하고, 사용자의 질의와 가장 유사한 질문을 우선적으로 검색할 수 있도록 하여 검색 성능을 높였습니다.

#### 3. 에이전트 구조
- 모든 질문을 하나의 방식으로 처리할 경우, 규정 질의와 경기 결과 질의를 동일한 흐름으로 다루게 되어 응답 품질이 불안정해지는 문제가 있었습니다.
- 이에 따라 질문 유형을 규정, 실시간 경기 결과, 과거 기록, 특정 라운드 기록 등으로 구분하고, 각 질문에 맞는 도구를 선택하도록 에이전트 구조를 설계하여 응답 품질을 개선했습니다.

#### 4. 파인 튜닝
- 사용자의 질문은 규정집 문장 그대로가 아니라 일상적인 표현으로 입력되는 경우가 많아, 단순 검색만으로는 관련 조항을 정확히 찾기 어려운 문제가 있었습니다.
- 이를 해결하기 위해 규정 기반 질문-답변 데이터를 활용해 모델을 파인튜닝함으로써, 자연스러운 사용자 질문에도 보다 적절한 답변을 생성할 수 있도록 개선했습니다.

---

### 📜 수행결과(테스트/시연 페이지)

---

### 📒 한 줄 회고
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
