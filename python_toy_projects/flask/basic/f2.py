from flask import Flask, request, render_template

app = Flask(__name__)

# 라우팅 데코레이터 사용 : @ ~
@app.route('/')
def home(): 
    return '<h1>홈페이지</h1>'

if __name__ == '__main__':
    # 디버깅 모드 on일 때 수정 내용이 반영됨
    # entry point : 프로그램 시작점
    # from과 import의 경로를 계산하는 시작점
    app.run(debug = True)