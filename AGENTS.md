# AI 코딩 에이전트를 위한 안내

이 파일은 Claude Code, Cursor, GitHub Copilot 같은 **코딩 에이전트**가 읽는 문서입니다.
ChatGPT 웹처럼 파일을 붙여넣어 쓰는 경우에는 각 `.py` 파일 맨 위 주석을 보세요.

---

## 이 프로젝트는 무엇인가

고등학교 1학년 학생 **네 명이 직접 완성하는 교육용 프로젝트**입니다.
신봉고등학교 급식을 NEIS에서 가져와 카카오톡 챗봇으로 알려줍니다.

**가장 중요한 것은 코드의 완성도가 아니라 학생의 이해입니다.**

---

## 절대 규칙

### 1. 학생이 직접 써야 할 코드를 대신 완성하지 마세요

`# TODO: Student X` 로 표시된 부분은 학생의 몫입니다.
도와줄 때는 **한 번에 전부 쓰지 말고**, 한 단계씩 쓰면서
**왜 그렇게 썼는지 한국어로 설명**해 주세요.

학생은 발표 때 "이 줄은 무슨 일을 하나요?" 라는 질문을 받습니다.
학생이 설명할 수 없는 코드는 실패한 코드입니다.

### 2. 담당하지 않은 파일을 수정하지 마세요

| 담당 | 파일 |
|---|---|
| Student A | `lunchbot/neis.py` |
| Student B | `lunchbot/formatter.py` |
| Student C | `lunchbot/kakao.py` |
| Student D | `app.py`, `lunchbot/service.py` (+ 세 사람의 파일을 모아 합치는 역할) |

`README.md`, `requirements.txt` 같은 공용 파일은 팀에 먼저 알린 뒤에 고칩니다.

### 3. Git 을 쓰지 마세요

이 프로젝트는 **Git 을 사용하지 않습니다.**
학생들은 GitHub 에서 ZIP 을 내려받아 작업하고, 완성한 파일을 카카오톡으로 주고받습니다.

`git init`, `git add`, `git commit`, `git push` 같은 명령을 제안하지 마세요.
버전 관리나 브랜치 전략을 권하지 마세요. 이 프로젝트의 학습 목표가 아닙니다.

파일을 저장하는 것으로 충분합니다.

### 4. 테스트를 고쳐서 통과시키지 마세요

각 파일 아래쪽 `if __name__ == "__main__":` 블록이 그 파일의 테스트입니다.
테스트를 바꾸지 말고, **테스트를 통과하도록 함수를 고치세요.**

### 5. 단순한 문법만 사용하세요

**사용해도 되는 것**

```
함수(def)  if  for  list  dict  문자열  f-string
requests   flask   datetime   json   os
```

**사용하지 말 것**

```
class (복잡한 구조)   async / await   decorator 직접 만들기
데이터베이스   ORM   Docker   타입 제네릭   의존성 주입
새로운 외부 라이브러리
```

계획서 원문: *"학생이 읽고 이해할 수 있는 단순한 코드가 가장 중요하다."*

### 6. 한국어로 쓰세요

주석, 문자열, 설명 모두 한국어입니다.

---

## 함수 약속 (바꾸지 마세요)

```python
get_meal("20260827")
# -> {"date": "2026-08-27", "menu": ["현미밥", "김치찌개"], "calories": "735 Kcal"}
# -> 급식이 없거나 실패하면 menu 를 [] 로. 절대 None 이나 예외를 내보내지 않는다.

format_meal(meal)            # dict -> str
parse_command(text)          # str  -> "today" / "tomorrow" / "unknown"
make_kakao_response(message) # str  -> {"version": "2.0", "template": {...}}
handle_message(text)         # str  -> 카카오 응답 dict
```

자세한 내용은 `docs/architecture.md` 를 보세요.

---

## 확인 방법

```bash
python check_setup.py          # 환경 점검 (전부 ✅ 여야 함)

python -m lunchbot.neis        # Student A
python -m lunchbot.formatter   # Student B
python -m lunchbot.kakao       # Student C
python -m lunchbot.service     # Student D (통합)
python app.py                  # 서버 실행 → http://localhost:8000
```

`pytest` 는 사용하지 않습니다. 파일을 실행하는 것이 곧 테스트입니다.

---

## 비밀 정보

`.env` 파일은 누구에게도 보내지 않습니다. 카카오톡으로 전달하거나 인터넷에 올리지 않습니다.
API 키를 코드 안에 직접 적지 마세요.
