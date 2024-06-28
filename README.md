# AI 기반 검색 증강 생성(Retrieval-Augmented Generation) 기술을 이용한 법률 데이터 분석 및 응답 시스템 개발

이 프로젝트는 도전학기에 제출한 계획 프로젝트입니다.

## 프로젝트 배경
최근 인공지능(AI) 기술의 급속한 발전은 다양한 산업 분야에서 큰 변화를 이끌고 있습니다. 특히, GPU와 같은 고성능 컴퓨팅 자원의 발달로 자연어 처리(NLP) 분야에서 큰 진전을 이루었으며, 그 결과 OpenAI의 GPT-3나 네이버의 클로바X와 같은 대규모 언어 모델이 등장하여 인간 수준의 언어 이해와 생성을 가능하게 했습니다.

그러나 이러한 언어 모델들은 종종 잘못된 정보를 사실인 것처럼 답변하는 '환각 현상(Hallucination)' 문제를 가지고 있습니다. 이는 특히 법률과 같이 정확한 정보가 필수적인 분야에서 심각한 문제로 작용할 수 있습니다.

우리 팀은 이러한 환각 문제를 개선하고자 검색 증강 생성(RAG: Retrieval-Augmented Generation) 기법에 주목하게 되었습니다. RAG는 외부 지식 소스를 검색하여 해당 정보를 활용함으로써, 모델이 단순히 학습된 데이터에 의존하지 않고 실제 데이터를 바탕으로 더 정확하고 신뢰성 있는 답변을 생성할 수 있게 합니다.

이번 프로젝트에서는 AI Hub의 법률/규정 텍스트 분석 데이터를 활용하여 법률 분야에서 RAG 기법의 성능을 평가하고 개선하고자 합니다. 이를 통해 법률 분야에서의 환각 문제를 줄이고, 보다 정확하고 신뢰성 있는 정보 제공 시스템을 개발하려고 합니다.

## 프로젝트 목표
이번 프로젝트의 주요 목표는 RAG(Retrieval-Augmented Generation) 기법을 이해하고 이를 법률 데이터에 적용하여 정확하고 신뢰성 있는 응답 시스템을 개발하는 것입니다. 이를 통해 법률 분야에서의 환각 문제를 줄이고, 보다 신뢰성 있는 정보 제공을 가능하게 하고자 합니다.

- **RAG 기법 학습 및 이해**: RAG 기법을 학습하고 이해하며, 이를 실제 법률 데이터에 적용합니다.
- **법률 데이터 분석**: AI Hub에서 제공하는 법률/규정(판결서, 약관 등) 텍스트 분석 데이터를 활용하여 법률 데이터를 분석합니다.
- **응답 시스템 개발**: Flutter 프레임워크를 사용하여 사용자 인터페이스를 설계하고, 언어 모델 API를 통합하여 실시간으로 응답을 제공하는 시스템을 개발합니다.
- **성능 평가 및 개선**: 개발된 시스템의 성능을 평가하고, 필요시 개선 작업을 수행합니다.


## 프로젝트 구조
    ```bash
    my_rag_project/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── model.py
    │
    ├── data/
    │   ├── data.json
    │   ├── data.xml
    │
    ├── requirements.txt
    ├── run.py
    └── README.md
    ```

## 사용 기술 및 도구
- **프로그래밍 언어**: Python, Dart
- **프레임워크**: Flask, Flutter
- **데이터베이스**: Chroma Vector DB, 기타 SQL/NoSQL 데이터베이스
- **AI 모델**: OpenAI GPT-3, 기타 NLP 모델
- **기타 도구**: Docker, Git

## 설치 및 실행 방법

### 사전 준비
- Python 및 필요한 라이브러리 설치
- Flutter 설치
- Docker 설치 (선택사항)

### 서버 설정
1. 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/yourusername/AI_RAG_Legal_Data_Analysis.git
    cd AI_RAG_Legal_Data_Analysis
    ```

2. 가상환경을 설정하고 필요한 패키지를 설치합니다:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows에서는 venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Flask 서버를 실행합니다:
    ```bash
    flask run
    ```

### 클라이언트 설정
1. Flutter 프로젝트를 설정합니다:
    ```bash
    cd flutter_app
    flutter pub get
    ```

2. Flutter 앱을 실행합니다:
    ```bash
    flutter run
    ```

## 사용 예제
1. 사용자 인터페이스에서 법률 관련 질문을 입력합니다.
2. 시스템이 질문을 처리하고 관련 법률 데이터를 검색합니다.
3. 검색된 데이터를 바탕으로 정확하고 신뢰성 있는 응답을 생성하여 사용자에게 제공합니다.

## 기여 방법
1. 이슈를 등록하여 버그를 보고하거나 새로운 기능을 제안합니다.
2. 포크를 하고 피처 브랜치를 생성합니다 (`git checkout -b feature/NewFeature`).
3. 변경사항을 커밋합니다 (`git commit -m 'Add some NewFeature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/NewFeature`).
5. 풀 리퀘스트를 엽니다.

## 라이선스
이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
