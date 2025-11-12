# AliceNeoLog

Python 프로젝트입니다.

## 설치 방법

```bash
# 가상 환경 생성
python -m venv .venv

# 가상 환경 활성화
# macOS/Linux:
source .venv/bin/activate
# Windows:
# venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 개발 환경 설정

```bash
# 개발 의존성 설치
pip install -e .
```

## 프로젝트 구조

```
AliceNeoLog/
├── src/
│   └── alice_neo_log/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── __init__.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## 실행 방법

```bash
python -m src.alice_neo_log.main
```

## 테스트 실행

```bash
pytest
```

## 코드 포맷팅

```bash
black .
```

## 라이선스

MIT

