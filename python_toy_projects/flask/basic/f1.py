# 기본 템플릿 준비
# 1. 모듈 가져오기
from flask import Flask

# 2. 앱 생성(플라스크 객체 생성)
app = Flask(__name__)
# 3. 라우팅(사용자가 요청한 페이지의 주소(url)을 누가 처리할 것인지 연결)
# http : 웹 상에서 상호 통신하는 프로토콜
# 127.0.0.1 : 로컬 PC상의 loopback ip 주소 == localback
# 5000 : 포트, flask의 기본 포트
# URL : http://127.0.0.1:5000/
@app.route('/') # 요청
def home(): # 응답
    # 응답처리가 결론
    # return => 요청에 대한 응답
    return '<h1>홈페이지</h1>'

# 4. 웹 서비스를 제공하는 서버가동
if __name__ == '__main__':
    app.run()