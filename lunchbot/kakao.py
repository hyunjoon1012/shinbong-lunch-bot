"""
============================================================
 Student C 담당 파일 — 카카오톡 질문 이해하기 + 답장 형식 만들기
============================================================

■ 이 파일에서 할 일 (함수 2개)
    1) parse_command("오늘 급식")        →  "today"
    2) make_kakao_response("안녕하세요")  →  카카오톡이 이해하는 dict

■ 실행해서 확인하는 방법
    터미널에서:  python -m lunchbot.kakao
    (VS Code 오른쪽 위 ▶ 버튼을 눌러도 됩니다)

  ★ 이 파일은 인터넷도, 카카오톡도 필요 없습니다. 혼자 만들 수 있습니다.

■ AI(ChatGPT 등)에게 물어보는 방법
    1) 이 파일 전체를 복사한다  (Ctrl+A → Ctrl+C, Mac은 Cmd+A → Cmd+C)
    2) AI 채팅창에 붙여넣는다
    3) 아래 문장을 이어서 보낸다

    ┌──── 복사해서 쓰는 질문 ────────────────────────┐
    │ 이건 고등학교 1학년 파이썬 프로젝트 파일이야.  │
    │ 파일 아래쪽 테스트를 통과하도록                │
    │ 두 함수의 TODO 부분만 채워줘.                  │
    │                                                │
    │ 규칙:                                          │
    │ - class, async 를 쓰지 마                      │
    │ - 새 라이브러리를 추가하지 마                  │
    │ - if / for / list / dict / f-string 만 사용해  │
    │ - 주석은 한국어로 써줘                         │
    │ - 코드를 한 줄씩 왜 그렇게 썼는지 설명해줘     │
    │ - 파일 전체를 다시 쓰지 말고 TODO 부분만 줘    │
    │ - 아래 테스트 코드는 고치지 마                 │
    └────────────────────────────────────────────────┘

    ※ AI가 준 코드를 붙여넣기 전에 설명을 먼저 읽으세요.
      발표 때 "이 줄은 무슨 일을 하나요?" 라는 질문을 받습니다.
"""


# =========================================================
#  1. 카카오톡은 우리 서버에 이런 데이터를 보냅니다
# =========================================================
#
#  사용자가 카카오톡에 "오늘 급식" 이라고 입력하면,
#  카카오 서버가 우리 서버로 아래와 같은 JSON 을 보냅니다. (줄인 것)
#
#      {
#        "userRequest": {
#          "timezone": "Asia/Seoul",
#          "utterance": "오늘 급식",          ← 사용자가 입력한 말
#          "user": {"id": "abc123", "type": "botUserKey"}
#        },
#        "bot": {"id": "...", "name": "급식 알리미"},
#        "action": {"name": "급식조회", "params": {}}
#      }
#
#  사용자가 입력한 말의 위치:   body["userRequest"]["utterance"]
#  (이 부분을 꺼내는 일은 Student D 가 app.py 에서 합니다.
#   Student C 는 꺼내진 문자열만 받으면 됩니다.)


# =========================================================
#  2. 카카오톡에게 이런 모양으로 답해야 합니다
# =========================================================
#
#  아래 모양이 아니면 카카오톡에 아무것도 안 보입니다.
#  "version" 과 "template" 이라는 이름은 카카오가 정한 것이라 바꿀 수 없습니다.
#
#      {
#        "version": "2.0",
#        "template": {
#          "outputs": [
#            {
#              "simpleText": {
#                "text": "여기에 보여줄 메시지가 들어갑니다"
#              }
#            }
#          ]
#        }
#      }
#
#  outputs 는 리스트([])이고, 그 안에 dict 가 들어간다는 점을 잘 보세요.


# =========================================================
#  3. 내가 만들어야 하는 함수 (1) — 사용자 말 이해하기
# =========================================================

def parse_command(text: str) -> str:
    """
    사용자가 입력한 말을 우리 프로그램이 쓰는 명령어로 바꾼다.

    Example:
        parse_command("오늘 급식")     ->  "today"
        parse_command("오늘급식")      ->  "today"
        parse_command("내일 급식")     ->  "tomorrow"
        parse_command("안녕")          ->  "unknown"

    돌려줄 수 있는 값은 이 세 가지뿐이다:
        "today"  /  "tomorrow"  /  "unknown"

    이 세 단어는 Student D 의 service.py 와 맞춘 약속이라 바꾸면 안 된다.
    """
    # TODO: Student C
    #
    #  1. "내일" 이라는 글자가 text 안에 있으면 "tomorrow" 를 return 한다.
    #     힌트:  if "내일" in text:
    #
    #  2. "오늘" 이라는 글자가 있으면 "today" 를 return 한다.
    #
    #  3. 둘 다 아니면 "unknown" 을 return 한다.
    #
    #  ※ 순서에 주의하세요. "내일" 을 먼저 확인해야 합니다.
    #  ※ "급식" 이라는 글자만 있어도 today 로 볼지는 자유롭게 정해도 됩니다.
    #
    raise NotImplementedError


# =========================================================
#  4. 내가 만들어야 하는 함수 (2) — 카카오 답장 형식 만들기
# =========================================================

def make_kakao_response(message: str) -> dict:
    """
    보통 문자열을 카카오톡이 이해하는 dict 로 바꾼다.

    Example input:
        "오늘 급식은 돈까스입니다."

    Example output:
        {
            "version": "2.0",
            "template": {
                "outputs": [
                    {"simpleText": {"text": "오늘 급식은 돈까스입니다."}}
                ]
            }
        }
    """
    # TODO: Student C
    #
    #  1. 위 2번에 있는 모양 그대로 dict 를 만든다.
    #  2. "text" 자리에 message 를 넣는다.
    #  3. 만든 dict 를 return 한다.
    #
    #  ※ dict 안에 list 가 있고, 그 안에 또 dict 가 있습니다.
    #    괄호를 잘 맞춰서 써보세요.
    #
    raise NotImplementedError


# =========================================================
#  5. 내 코드 테스트하기
#
#     터미널에서:  python -m lunchbot.kakao
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
        print("=== 1. parse_command 테스트 ===")
        print("  '오늘 급식' ->", parse_command("오늘 급식"))
        print("  '내일 급식' ->", parse_command("내일 급식"))
        print("  '안녕'      ->", parse_command("안녕"))
        check("'오늘 급식' 은 today", parse_command("오늘 급식") == "today")
        check("'오늘급식' 은 today", parse_command("오늘급식") == "today")
        check("'내일 급식' 은 tomorrow", parse_command("내일 급식") == "tomorrow")
        check("'안녕' 은 unknown", parse_command("안녕") == "unknown")

        print()
        print("=== 2. make_kakao_response 테스트 ===")
        응답 = make_kakao_response("테스트 메시지")
        print("  결과:", 응답)
        check("dict 를 돌려준다", type(응답) is dict)
        check("version 이 '2.0' 이다", 응답.get("version") == "2.0")
        check("template 키가 있다", "template" in 응답)
        check("outputs 가 list 다", type(응답.get("template", {}).get("outputs")) is list)

        outputs = 응답.get("template", {}).get("outputs", [])
        if len(outputs) > 0:
            check("outputs 안에 simpleText 가 있다", "simpleText" in outputs[0])
            check(
                "메시지가 text 에 들어있다",
                outputs[0].get("simpleText", {}).get("text") == "테스트 메시지",
            )
        else:
            check("outputs 안에 내용이 있다", False)

        print()
        print("테스트 끝. ❌ 가 있으면 그 부분을 고쳐보세요.")

    except NotImplementedError:
        print("  ⏳ 아직 구현하지 않았습니다. 위의 TODO 부분을 채워주세요.")
        print("     (지금 이 메시지가 나오는 것은 정상입니다)")
