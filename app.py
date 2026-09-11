"""
============================================================
 Student D 담당 파일 (2/2) — 카카오톡이 접속할 웹 서버
============================================================

■ 이 파일에서 할 일
    카카오톡이 보낸 요청(POST /kakao)을 받아서 handle_message() 에 넘긴다.

■ 실행해서 확인하는 방법
    터미널에서:  python app.py
    그러면 서버가 켜집니다. 브라우저에서 아래 주소를 열어보세요.

        http://localhost:8000

    "급식 알리미 서버가 동작 중입니다" 가 보이면 성공입니다.
    서버를 끌 때는 터미널에서 Ctrl + C 를 누르세요.

■ AI(ChatGPT 등)에게 물어보는 방법
    1) 이 파일 전체를 복사한다  (Ctrl+A → Ctrl+C, Mac은 Cmd+A → Cmd+C)
    2) AI 채팅창에 붙여넣는다
    3) 아래 문장을 이어서 보낸다

    ┌──── 복사해서 쓰는 질문 ────────────────────────┐
    │ 이건 고등학교 1학년 파이썬 프로젝트 파일이야.  │
    │ Flask 로 만든 웹 서버야.                       │
    │ kakao 함수의 TODO 부분만 채워줘.               │
    │                                                │
    │ 규칙:                                          │
    │ - class, async 를 쓰지 마                      │
    │ - Flask 외에 새 라이브러리를 추가하지 마       │
    │ - 주석은 한국어로 써줘                         │
    │ - 코드를 한 줄씩 왜 그렇게 썼는지 설명해줘     │
    │ - 파일 전체를 다시 쓰지 말고 TODO 부분만 줘    │
    └────────────────────────────────────────────────┘
"""

from flask import Flask, jsonify, request

from lunchbot.service import handle_message

app = Flask(__name__)

# 응답에 한글이 그대로 보이게 해줍니다. 건드리지 마세요.
app.json.ensure_ascii = False


# =========================================================
#  1. 카카오톡은 우리 서버에 이렇게 요청합니다
# =========================================================
#
#      POST /kakao
#      Content-Type: application/json
#
#      {
#        "userRequest": {
#          "utterance": "오늘 급식",        ← 사용자가 입력한 말
#          "user": {"id": "abc123"}
#        },
#        "action": {"name": "급식조회"}
#      }
#
#  사용자가 입력한 말의 위치:  body["userRequest"]["utterance"]
#
#  우리 서버는 아래 모양으로 답해야 합니다.
#
#      {
#        "version": "2.0",
#        "template": {"outputs": [{"simpleText": {"text": "메시지"}}]}
#      }
#
#  이 dict 를 만들어주는 함수가 handle_message() 입니다. (lunchbot/service.py)


# =========================================================
#  2. 서버가 살아있는지 확인하는 주소 (이미 만들어져 있습니다)
# =========================================================

@app.route("/")
def home():
    return "급식 알리미 서버가 동작 중입니다. 🍚"


# =========================================================
#  3. 카카오톡이 실제로 부르는 주소 — 여기를 만들어야 합니다
# =========================================================

@app.route("/kakao", methods=["POST"])
def kakao():
    # 1. 카카오가 보낸 데이터를 받는다.
    body = request.get_json()

    # 2. 사용자가 입력한 말을 꺼낸다.
    text = body["userRequest"]["utterance"]

    # 3. 답장 dict 를 만든다. (service.py 의 함수)
    답장 = handle_message(text)

    # 4. 카카오톡에 돌려준다.
    return jsonify(답장)


# =========================================================
#  4. 서버 켜기
# =========================================================
#
#  ● 카카오톡 없이 /kakao 를 테스트해보고 싶다면?
#    서버를 켜둔 채로 터미널 창을 하나 더 열고 아래를 실행하세요.
#
#    [Mac / Linux]
#      curl -X POST http://localhost:8000/kakao \
#           -H "Content-Type: application/json" \
#           -d '{"userRequest": {"utterance": "오늘 급식"}}'
#
#    [Windows PowerShell]
#      Invoke-RestMethod -Uri http://localhost:8000/kakao -Method Post `
#        -ContentType "application/json" `
#        -Body '{"userRequest": {"utterance": "오늘 급식"}}'

if __name__ == "__main__":
    print()
    print("=" * 50)
    print(" 급식 알리미 서버를 켭니다")
    print("=" * 50)
    print(" 브라우저에서 열어보세요 :  http://localhost:8000")
    print(" 서버를 끄려면          :  Ctrl + C")
    print("=" * 50)
    print()
    app.run(host="0.0.0.0", port=8000, debug=True)
