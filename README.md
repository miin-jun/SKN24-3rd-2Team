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
    <td align="center" width="200"><a href="https://github.com/miin-jun">miin-jun</a></td>
    <td align="center" width="200"><a href="https://github.com/shortcut-2">youjin</a></td>
    <td align="center" width="200"><a href="https://github.com/aprkaos56">aprkaos56</a></td>
    <td align="center" width="200"><a href="https://github.com/Yunu-Jeon">Yunu-Jeon</a></td>
    <td align="center" width="200"><a href="https://github.com/lifeisgoodlg">lifeisgoodlg</a></td>
  </tr>
</table>

---

### 1️⃣ 프로젝트 개요

- 프로젝트 소개
  > F1 입문자를 위해 어려운 용어와 복잡한 규정을 쉽게 설명해주는 한국어 기반 F1 전문 챗봇입니다. 사용자의 질문 의도에 따라 규정집, 용어집, 과거 기록, 라운드별 경기 정보 등을 바탕으로 적절한 답변을 제공할 수 있도록 LLM 챗봇을 구현했습니다.
- 프로젝트 필요성(배경)
  > 최근 국내에서 F1 경기에 대한 관심과 팬 유입이 증가하고 있지만, 입문자가 처음 접하기에는 F1의 용어와 규정이 매우 어렵고 복잡합니다. 특히 규정은 매년 개정되기 때문에 단순 검색만으로는 정확한 정보를 이해하기 어렵습니다. 이에 따라, 입문자도 쉽고 빠르게 F1 정보를 이해할 수 있도록 돕는 챗봇의 필요성을 느껴 본 프로젝트를 기획하게 되었습니다.
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
  > F1 입문자가 자주 궁금해하는 용어, 규정, 경기 관련 정보를 한국어로 쉽고 정확하게 제공하는 챗봇을 구현하는 것을 목표로 합니다. 이를 위해 F1 규정집과 용어집을 비롯해 플래그, 타이어, 역사, F1 개요 등의 데이터를 RAG 기반으로 구축하고, 변화하는 규정과 다양한 질문 유형에 유연하게 대응할 수 있는 질의응답 시스템을 개발하고자 합니다.

---

### 2️⃣ 기술 스택 & 사용한 모델 (임베딩 모델, LLM)

| 분류 | 기술/도구 |
|---|---|
| 언어 | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| LLM 프레임워크 | ![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge) ![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge) |
| 모델 / 추론 | ![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black) ![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white) |
| VectorDB / 검색 | ![ChromaDB](https://img.shields.io/badge/ChromaDB-5A31F4?style=for-the-badge) |
| 웹 파싱 | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-59666C?style=for-the-badge) |
| 개발 환경 | ![Google Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white) ![Runpod](https://img.shields.io/badge/Runpod-6C47FF?style=for-the-badge) |
| UI | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| 협업 도구 | ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white) |

| 분류 | 모델 |
|---|---|
| Embedding | ![intfloat/multilingual-e5-large](https://img.shields.io/badge/intfloat%2Fmultilingual--e5--large-FF6600?style=for-the-badge)
| LLM | ![google/gemma-3-12b-it](https://img.shields.io/badge/google%2Fgemma--3--12b--it-FF6600?style=for-the-badge) ![OpenAI API](https://img.shields.io/badge/OpenAI%20API-FF6600?style=for-the-badge) |
| Re-ranker | ![CrossEncoder](https://img.shields.io/badge/CrossEncoder-FF6600?style=for-the-badge) |

---

### 3️⃣ 시스템 아키텍처
<img width="500" height="600" alt="image" src="https://github.com/user-attachments/assets/1724827c-0138-4f38-b015-36a81ff8e4ec" />

---

### 4️⃣ WBS

---

### 5️⃣ 요구사항 명세서
<img width="1600" height="600" alt="image" src="https://github.com/user-attachments/assets/aa3be328-bdc1-48f4-863a-fd4e26e7aa36" />

---

### 6️⃣ 수집한 데이터 및 전처리 요약

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
| **총 데이터 항목 수** | **1,804** |

**Finetune 데이터 개수**

| 항목 | 개수 |
|---|---:|
| Finetune된 데이터 개수 | 15,260 |

**데이터 출처**

> F1 규정: https://www.fia.com/regulation/category/110?utm_source=chatgpt.com

> F1 용어: https://www.formula1.com/en/page/f1-glossary

> F1 역사: https://en.wikipedia.org/wiki/History_of_Formula_One

> F1 타이어: https://www.pirelli.com/tires/en-us/motorsport/f1/tires

> F1 개요: https://en.wikipedia.org/wiki/Formula_One

> F1 깃발: https://en.wikipedia.org/wiki/Racing_flags

> Jolpi.ca F1 API: https://api.jolpi.ca/ergast/

> openf1 API: https://openf1.org/

---

### 7️⃣ DB 연동 구현 코드 (링크만)

---

### 8️⃣ 테스트 계획 및 결과 보고서

#### 1) 테스트 개요

> 본 테스트는 **F1 입문자용 챗봇**이 사용자의 질문에 대해  
> **정확하고 이해하기 쉬운 답변**을 제공하는지 검증하기 위해 수행하였다.  
> 특히 **FIA 규정, F1 용어, 플래그, 역사, 스튜어드 판정문**을 기반으로 한  
> 질의응답 품질과 **한국어 설명 능력**을 중점적으로 평가하였다.

##### 테스트 목적
- 규정 기반 질의응답의 정확성 검증
- 한국어 질문 이해 및 응답 생성 능력 검증
- 입문자 친화적인 쉬운 설명 제공 여부 검증
- 시스템 응답 속도 및 서비스 안정성 검증

#### 2) 테스트 환경

| 항목 | 내용 |
|---|---|
| **LLM** | google/gemma-3-12b-it (QLoRA fine-tuned) |
| **임베딩 모델** | multilingual-e5-large |
| **Vector DB** | ChromaDB |
| **검색 방식** | RAG 기반 문서 검색 |
| **데이터셋** | FIA 규정, F1 용어집, 서킷, 깃발, 역사, 타이어, 스튜어드 판정문 |
| **평가 방식** | 수동 질의응답 평가 + 응답 시간 측정 |

#### 3) 테스트 항목

##### 3-1. 질의응답 정확성
- FIA 규정을 근거로 정확한 답변을 제공하는가?
- 용어, 플래그, 역사, 판정문 관련 질문에도 올바르게 응답하는가?

##### 3-2. 한국어 자연어 이해 능력
- 한국어 질문 의도를 정확히 파악하는가?
- 동일 의미의 다양한 표현에도 적절히 응답하는가?

##### 3-3. 쉬운 설명 변환 능력
- 초보자가 이해하기 어려운 기술 용어나 규정을 쉽게 풀어서 설명하는가?
- 불필요하게 어려운 표현 없이 자연스럽게 설명하는가?

##### 3-4. 응답 시간 및 성능
- 평균 응답 시간이 10초 이내인가?
- 질문 유형이 달라져도 일관된 속도로 응답하는가?

#### 4) 테스트 시나리오

> 테스트는 실제 **F1 입문자**가 챗봇을 사용하는 상황을 가정하여 진행하였다.

##### 시나리오 1. 규정 기반 사실 질문
- 사용자가 특정 조문이나 규정 내용을 직접 질문
- 챗봇이 관련 규정을 검색하고 정확한 사실을 설명하는지 확인
> 예시 질문
- Pistons는 어떤 금속 혼합물로부터 제조되어야 하는가?
- Heat Hazard가 선언되는 조건 중 하나는 무엇인가?
- 시상식에서 몇 개의 트로피가 수여되는가?

##### 시나리오 2. 용어/약어 설명 질문
- 사용자가 F1 약어나 전문 용어를 질문
- 챗봇이 정의와 맥락을 함께 설명하는지 확인
> 예시 질문
- LTC, TRC, FSC는 무엇을 의미합니까?
- Current Car(CC)는 어떤 차량을 의미합니까?

##### 시나리오 3. 규정 문서 이해 질문
- 사용자가 특정 문장의 성격이나 출처를 묻는 경우
- 챗봇이 해당 내용이 어느 규정/분류에 속하는지 설명하는지 확인
> 예시 질문
- 이 텍스트는 어떤 규정에 대한 내용을 담고 있나요?

##### 시나리오 4. 조건형/예외형 질문
- 사용자가 규정의 예외 조건이나 세부 조건을 질문
- 챗봇이 단순 암기형 답변이 아니라 조건을 구분하여 설명하는지 확인
> 예시 질문
- 어떤 조건 하에서 SQ1에서 제일 빠른 라운드 시간을 초과한 선수가 탈락하지 않고 계속 진행할 수 있나요?

#### 5) 테스트 케이스

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

#### 6) 테스트 수행 방법

> 각 테스트 문장을 챗봇에 입력한 뒤, 아래 기준에 따라 결과를 평가하였다.

##### 평가 기준
- **정확성**: 규정/원문과 일치하는가
- **이해성**: 한국어 문장이 자연스럽고 의미 전달이 명확한가
- **친절성**: 초보자도 이해할 수 있도록 쉬운 표현을 사용하는가
- **응답시간**: 응답 생성 시간이 10초 이내인가

평가는 각 문항별로 **수동 검토 방식**으로 진행하였으며,  
필요 시 원문 규정과 대조하여 사실 여부를 재확인하였다.

#### 7) 테스트 결과

> 테스트 결과, 챗봇은 **모든 규정 기반 질문에 대해 정확한 답변**을 제공하였으며,  
> 용어 설명과 조건형 질문에서도 **안정적인 성능**을 보였다.  
> 특히 단순 정의형 질문과 조문 근거가 명확한 질문에서는 **높은 정확도**를 보였다.  
> 하지만, 응답 시간이 평균 **10~20초의 시간**이 소요되었다.

##### 확인된 개선 필요 사항
- 일부 기술 규정 질문에서 답변이 조문 수준으로 딱딱하게 출력되는 경우가 있음
- 예외 조항이 포함된 질문에서는 설명이 길어져 초보자 관점에서 다소 어렵게 느껴질 수 있음
- 한국어 문장은 전반적으로 자연스러웠으나, 일부 용어는 추가적인 쉬운 풀이가 필요함
- 응답 생성 시간이 비교적 오래 걸리므로, 최적화가 필요함

#### 8) 종합 평가

> 본 테스트를 통해 F1 입문자용 챗봇은  
> 입문자 사용자를 대상으로 한 **규정 설명 서비스로서 기본적인 정확성과 설명 가능성**을 확보하였음을 확인하였다.  
> 향후에는 **예외 조항 설명 간소화**, **기술 용어의 쉬운 재서술**, **응답 속도 최적화**를 통해  
> 사용자 친화성을 더욱 높일 필요가 있다.

---

### 9️⃣ 진행 과정 중 프로그램 개선 노력

- 규정집 원문을 단순 검색하던 방식에서 벗어나, 조문·주제별로 구조화된 RAG 데이터셋을 구축하여 검색 정확도 향상
- 질문 유형(규정, 실시간 경기, 과거 기록, 특정 라운드 기록)에 따라 적절한 도구를 선택하도록 에이전트 구조를 설계해 응답 품질을 개선
- 매년 개정되는 F1 규정의 특성을 반영해, 공식 규정집 기반 데이터를 업데이트 가능한 구조로 설계하여 유지보수성 향상
- 입문자도 이해할 수 있도록 한국어 설명형 답변 중심으로 프롬프트를 개선

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
