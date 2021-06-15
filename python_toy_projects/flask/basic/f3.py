'''
    - 라우트 추가
        - 라우팅 처리를 수행하는 함수의 이름은 고유해야 한다.(중복을 허용하지 않음)
        - 같은 URL이 중복되게 정의되어 있다면 먼저 정의된 라우트 함수가 처리된다.
        - 프로젝트 초기에 스토리보드가 완성되고, 페이지가 정의가 되면, 각 페이지에 해당되는 URL 정의하고, 각 페이지를 기본적으로 구성한다
    - url 이해
'''
from flask import Flask

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
def home(): 
    return '<h1>홈페이지</h1>'


# ~/users/login
@app.route('/users/login')
def login(): 
    return '<h1>로그인 페이지</h1>'

# ~/main/service
@app.route('/main/service')
def service(): 
    return '<h1>서비스 메인 페이지</h1>'



if __name__ == '__main__':
    app.run(debug = True)