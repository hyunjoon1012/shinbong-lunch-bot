"""
============================================================
 준비 확인 — 가장 먼저 이 파일을 실행하세요
============================================================

■ 실행 방법
    터미널에서:  python check_setup.py

    ✅ 가 전부 나오면 개발 준비가 끝난 것입니다.
    ❌ 가 있으면 README.md 의 "1. 준비하기" 를 다시 해보세요.

  이 파일은 아무도 수정하지 않습니다. 확인용입니다.
"""

import os
import sys


def check(설명, 조건):
    if 조건:
        print("  ✅", 설명)
        return True
    else:
        print("  ❌", 설명)
        return False


print()
print("=" * 50)
print(" 신봉고 급식 알리미 — 준비 확인")
print("=" * 50)
print()

결과 = []

# ---------------------------------------------------------
print("[1] 파이썬")
print("   지금 쓰는 파이썬:", sys.version.split()[0])
결과.append(check("파이썬 3.9 이상이다", sys.version_info >= (3, 9)))
print()

# ---------------------------------------------------------
print("[2] 필요한 패키지")
try:
    import requests  # noqa: F401
    결과.append(check("requests 가 설치되어 있다", True))
except ImportError:
    결과.append(check("requests 가 설치되어 있다", False))

try:
    import flask  # noqa: F401
    결과.append(check("flask 가 설치되어 있다", True))
except ImportError:
    결과.append(check("flask 가 설치되어 있다", False))
print()

# ---------------------------------------------------------
print("[3] 프로젝트 파일")
for 파일 in [
    "app.py",
    "lunchbot/neis.py",
    "lunchbot/formatter.py",
    "lunchbot/kakao.py",
    "lunchbot/service.py",
    "samples/meal.json",
]:
    결과.append(check(f"{파일} 이 있다", os.path.exists(파일)))
print()

# ---------------------------------------------------------
print("[4] 연습용 데이터 읽기")
try:
    import json

    with open("samples/meal.json", encoding="utf-8") as f:
        샘플 = json.load(f)
    print("   읽은 내용:", 샘플)
    결과.append(check("samples/meal.json 을 읽을 수 있다", "menu" in 샘플))
except Exception as 오류:
    print("   오류:", 오류)
    결과.append(check("samples/meal.json 을 읽을 수 있다", False))
print()

# ---------------------------------------------------------
print("=" * 50)
if all(결과):
    print(" 🎉 준비 완료! 이제 자기 담당 파일을 열어보세요.")
    print()
    print("   Student A  →  lunchbot/neis.py       (python -m lunchbot.neis)")
    print("   Student B  →  lunchbot/formatter.py  (python -m lunchbot.formatter)")
    print("   Student C  →  lunchbot/kakao.py      (python -m lunchbot.kakao)")
    print("   Student D  →  app.py                 (python app.py)")
else:
    print(" ⚠️  ❌ 가 있습니다. README.md 의 '1. 준비하기' 를 다시 해보세요.")
print("=" * 50)
print()
