"""
============================================================
 Student D 담당 파일 (1/2) — 세 사람의 함수를 하나로 연결하기
============================================================

■ 이 파일에서 할 일
    handle_message("오늘 급식")  →  카카오톡에 보낼 최종 dict

■ 실행해서 확인하는 방법
    터미널에서:  python -m lunchbot.service
    (VS Code 오른쪽 위 ▶ 버튼을 눌러도 됩니다)

  ★ 이 파일은 A, B, C 세 사람의 함수가 모두 완성되어야 통과합니다.
    그 전에는 아래 테스트에서 "아직 완성되지 않았습니다" 가 나옵니다. 정상입니다.
    Student D 는 먼저 app.py 로 서버를 띄우는 일부터 하세요.

■ AI(ChatGPT 등)에게 물어보는 방법
    1) 이 파일 전체를 복사한다  (Ctrl+A → Ctrl+C, Mac은 Cmd+A → Cmd+C)
    2) AI 채팅창에 붙여넣는다
    3) 아래 문장을 이어서 보낸다

    ┌──── 복사해서 쓰는 질문 ────────────────────────┐
    │ 이건 고등학교 1학년 파이썬 프로젝트 파일이야.  │
    │ 파일 아래쪽 테스트를 통과하도록                │
    │ handle_message 함수의 TODO 부분만 채워줘.      │
    │                                                │
    │ 규칙:                                          │
    │ - class, async 를 쓰지 마                      │
    │ - 새 라이브러리를 추가하지 마                  │
    │ - if / for / list / dict / f-string 만 사용해  │
    │ - 주석은 한국어로 써줘                         │
    │ - 코드를 한 줄씩 왜 그렇게 썼는지 설명해줘     │
    │ - 파일 전체를 다시 쓰지 말고 TODO 부분만 줘    │
    │ - 위쪽 import 부분과 아래 테스트는 고치지 마   │
    └────────────────────────────────────────────────┘
"""

import datetime

# 이 부분은 어디서 실행해도 잘 되게 해주는 코드입니다. 건드리지 마세요.
try:
    from lunchbot.neis import get_meal
    from lunchbot.formatter import format_meal
    from lunchbot.kakao import parse_command, make_kakao_response
except ImportError:
    from neis import get_meal
    from formatter import format_meal
    from kakao import parse_command, make_kakao_response


# =========================================================
#  1. 전체 흐름
# =========================================================
#
#      카카오톡  ("오늘 급식")
#         ↓
#      app.py            ← Student D
#         ↓
#      handle_message()  ← 지금 이 파일에서 만드는 함수
#         ↓
#      parse_command()   ← Student C :  "오늘 급식" → "today"
#         ↓
#      (날짜 계산)        ← 여기서 "today" → "20260827"
#         ↓
#      get_meal()        ← Student A :  "20260827" → 급식 dict
#         ↓
#      format_meal()     ← Student B :  급식 dict → 읽기 좋은 문자열
#         ↓
#      make_kakao_response() ← Student C : 문자열 → 카카오 dict
#         ↓
#      카카오톡


# =========================================================
#  2. 다른 사람들이 만드는 함수 (이미 있다고 생각하고 쓰면 됩니다)
# =========================================================
#
#   parse_command("오늘 급식")
#       ->  "today"  또는  "tomorrow"  또는  "unknown"
#
#   get_meal("20260827")
#       ->  {"date": "2026-08-27",
#            "menu": ["현미밥", "김치찌개"],
#            "calories": "735 Kcal"}
#       ->  급식이 없으면 menu 가 빈 리스트 []
#
#   format_meal(급식dict)
#       ->  "🍚 8월 27일 신봉고 급식\n\n현미밥\n김치찌개\n\n735 Kcal"
#
#   make_kakao_response("아무 문자열")
#       ->  {"version": "2.0",
#            "template": {"outputs": [{"simpleText": {"text": "아무 문자열"}}]}}


# =========================================================
#  3. 내가 만들어야 하는 함수
# =========================================================

def handle_message(text: str) -> dict:
    """
    사용자가 보낸 말을 받아서, 카카오톡에 돌려줄 dict 를 만든다.

    Example input:
        "오늘 급식"

    Example output:
        {"version": "2.0",
         "template": {"outputs": [{"simpleText": {"text": "🍚 8월 27일 ..."}}]}}

    모르는 말이 들어오면 안내 메시지를 돌려준다:
        "'오늘 급식'이라고 입력해주세요!"
    """
    # TODO: Student D (Integration)
    #
    #  1. parse_command(text) 로 명령어를 알아낸다.
    #
    #  2. 명령어가 "unknown" 이면
    #     make_kakao_response("'오늘 급식'이라고 입력해주세요!") 를 return 한다.
    #
    #  3. 명령어에 따라 날짜를 정한다. NEIS 는 "20260827" 모양을 원한다.
    #
    #        오늘   : datetime.date.today()
    #        내일   : datetime.date.today() + datetime.timedelta(days=1)
    #        문자열로 바꾸기 : 날짜.strftime("%Y%m%d")
    #
    #  4. get_meal(날짜) 로 급식 데이터를 가져온다.
    #
    #  5. format_meal(급식) 으로 메시지를 만든다.
    #
    #  6. make_kakao_response(메시지) 를 return 한다.
    #
    raise NotImplementedError


# =========================================================
#  4. 내 코드 테스트하기
#
#     터미널에서:  python -m lunchbot.service
#
#     ✅ 가 전부 나오면 성공입니다.
#     이 아래는 고치지 마세요.
# =========================================================

def check(설명, 조건):
    if 조건:
        print("  ✅", 설명)
    else:
        print("  ❌", 설명)


if __name__ == "__main__":
    try:
        print("=== 1. '오늘 급식' 테스트 ===")
        결과 = handle_message("오늘 급식")
        print("  결과:", 결과)
        check("dict 를 돌려준다", type(결과) is dict)
        check("version 이 '2.0' 이다", 결과.get("version") == "2.0")
        check("template 키가 있다", "template" in 결과)

        outputs = 결과.get("template", {}).get("outputs", [])
        check("outputs 안에 내용이 있다", len(outputs) > 0)
        if len(outputs) > 0:
            메시지 = outputs[0].get("simpleText", {}).get("text", "")
            print("  실제로 보낼 메시지:")
            print("  ---------------------")
            print(메시지)
            print("  ---------------------")
            check("메시지가 비어있지 않다", len(메시지) > 0)

        print()
        print("=== 2. 모르는 말 테스트 ===")
        결과2 = handle_message("안녕")
        메시지2 = 결과2.get("template", {}).get("outputs", [{}])[0] \
                     .get("simpleText", {}).get("text", "")
        print("  결과:", 메시지2)
        check("안내 메시지를 돌려준다", "급식" in 메시지2)

        print()
        print("테스트 끝. ❌ 가 있으면 그 부분을 고쳐보세요.")

    except NotImplementedError:
        print("  ⏳ 아직 완성되지 않았습니다.")
        print()
        print("     이 파일은 A, B, C, D 네 사람의 함수가 모두 있어야 통과합니다.")
        print("     지금 이 메시지가 나오는 것은 정상입니다.")
        print()
        print("     Student D 는 먼저 app.py 로 서버를 띄워보세요:")
        print("         python app.py")
