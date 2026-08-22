# 프로그램 구조

## 전체 흐름

```
사용자
  │  "오늘 급식"
  ▼
카카오톡 챗봇
  │  POST /kakao
  ▼
app.py                      ← Student D
  │
  ▼
handle_message()            ← Student D  (lunchbot/service.py)
  │
  ├─▶ parse_command()       ← Student C  "오늘 급식" → "today"
  │
  ├─▶ (날짜 계산)             "today" → "20260827"
  │
  ├─▶ get_meal()            ← Student A  "20260827" → 급식 dict
  │
  ├─▶ format_meal()         ← Student B  급식 dict → 읽기 좋은 문자열
  │
  └─▶ make_kakao_response() ← Student C  문자열 → 카카오 dict
  │
  ▼
카카오톡 챗봇
  │
  ▼
사용자
```

---

## 함수 약속 (계약)

이 약속은 특별한 이유가 없으면 프로젝트 중간에 바꾸지 않는다.
바꿔야 한다면 반드시 네 명이 같이 정한다.

### A → B

```
get_meal(date)
```

| | |
|---|---|
| 입력 | `"20260827"` (문자열, YYYYMMDD) |
| 출력 | `dict` |

```json
{
  "date": "2026-08-27",
  "menu": ["현미밥", "김치찌개"],
  "calories": "735 Kcal"
}
```

### B → C/D

```
format_meal(meal)
```

| | |
|---|---|
| 입력 | `dict` |
| 출력 | `str` |

### C

```
parse_command(text)
```

| | |
|---|---|
| 입력 | `str` |
| 출력 | `"today"` / `"tomorrow"` / `"unknown"` |

```
make_kakao_response(message)
```

| | |
|---|---|
| 입력 | `str` |
| 출력 | `dict` |

### D

```
handle_message(text)
```

| | |
|---|---|
| 입력 | `str` |
| 출력 | `dict` (카카오 응답 형식) |

---

## 이번 프로젝트에서 정한 것

계획서에 없어서 네 명이 헷갈릴 수 있는 부분을 미리 정해두었다.

| 상황 | 약속 |
|---|---|
| 급식이 없는 날 (주말·방학) | `get_meal()` 은 **항상 dict 를 돌려준다.** `menu` 를 빈 리스트 `[]` 로 한다 |
| NEIS 연결 실패 | 위와 같다. 프로그램이 멈추면 안 된다 |
| `menu` 가 `[]` 일 때 메시지 | `"오늘은 급식이 없습니다."` |
| 모르는 말이 들어왔을 때 | `parse_command` 는 `"unknown"`, 메시지는 `"'오늘 급식'이라고 입력해주세요!"` |
| 급식 종류 | 중식(점심)만 사용한다. `MMEAL_SC_CODE = "2"` |
| NEIS 인증키 | 없어도 된다. 있으면 `.env` 에 넣는다 |
| 웹 프레임워크 | Flask |
| 서버 포트 | 8000 |
| 날짜를 정하는 곳 | `service.py` (`"today"` → `"20260827"`) |

---

## NEIS 정보

```
교육청 코드 (ATPT_OFCDC_SC_CODE) : J10       경기도교육청
학교 코드   (SD_SCHUL_CODE)      : 7531013   신봉고등학교
급식 종류   (MMEAL_SC_CODE)      : 2         중식
주소                              : https://open.neis.go.kr/hub/mealServiceDietInfo
```

자세한 사용법과 응답 구조는 `lunchbot/neis.py` 파일 안 주석에 적어두었다.

---

## 파일과 담당

| 담당 | 파일 | 실행 방법 |
|---|---|---|
| Student A | `lunchbot/neis.py` | `python -m lunchbot.neis` |
| Student B | `lunchbot/formatter.py` | `python -m lunchbot.formatter` |
| Student C | `lunchbot/kakao.py` | `python -m lunchbot.kakao` |
| Student D | `app.py`, `lunchbot/service.py` | `python app.py` |
| (공용) | `check_setup.py` | `python check_setup.py` |

Student D 는 세 사람이 카카오톡으로 보낸 파일을 모아 하나의 폴더에서 합치는 역할도 한다.

---

## 파일을 주고받는 방법

```
GitHub 에서 ZIP 내려받기
        ↓
각자 자기 담당 파일만 수정
        ↓
카카오톡으로 파일 전달  (A, B, C  →  D)
        ↓
D 가 한 폴더에 모아 합치기
        ↓
GitHub 에 올리기 (3주차, D 담당)
```

파일 하나에 담당자가 한 명뿐이므로 서로의 코드가 섞일 일이 없다.
자세한 순서는 `README.md` 의 「6. 파일 주고받기」 참고.
