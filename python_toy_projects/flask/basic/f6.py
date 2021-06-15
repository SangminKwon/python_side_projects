'''
    상황) 클라이언트가 서버측에 페이지를 요청시 데이터를 함께 전달
    - POST
        - 데이터를 숨겨서 서버로 전달한다.
        - 보안에 우수, 대량의 데이터 전송 가능
    - API 소개
        - render_template('xx.html')
            - html은 디자이너가 작업하는 내용이다. 웹 프로그래밍 영역에서 분리해서 관리
            - py 파일이 커지는 것을 막고, 수정을 용이하게 하기 위함이다. 이를 render_template가 지원해주는 것.
            - html을 읽어서 추가된 데이터가 있다면 최종 html로 생성하여 응답한다.
                - 서버 사이드 렌더링 -> 템플릿 엔진 필요
                    - 템플릿 엔진으로 JinJa를 사용한다
                        - html을 해석하고, 데이터를 버무려서 동적으로 다시 html 파일을 생성하는 도구
                    - flask 설치시 자동으로 같이 설치
                    - /templates에 login.html이 존재해야 한다.
'''

from flask import Flask, request, render_template
from db.d6 import selectUsers

# f6.py에서 ./db/d6.py를 가져와서 selectUsers()함수를 사용하고자 한다.
''' from 패키지.패키지...모듈 import 변수, 함수, 클래스 , *
from 패키지.패키지...패키지 import 모듈.변수, 함수, 클래스 '''

app = Flask(__name__)

# 현재는 GET만 허가됨
# @app.route('/login') <- GET만 허가된 상태
# POST를 허용하기 위해 추가 코드 필요
# 1rodml url에서 GET, POST 방식 모두 지원 -> restful 방식 : 사용 URL 개수 최소화 목적
@app.route('/login', methods = ['GET', 'POST']) # GET과 POST 모두 허가됨 
def login():
    # 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        # POST
        # 1. 전달된 데이터 획득 : 아이디 비번 획득
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        print(uid, upw)
        return 'post방식으로 잘 전달 되었다.'
        # 2. 데이터 베이스 쿼리 수행(아이디, 비번 확인)
        # 3. 수행결과를 받는다
        # 4. 회원이면 -> 서비스 페이지 이동
        # 5. 회원 아니면 -> 아이디 혹은 비번이 틀리다 -> 회원가입유도, 재로그인 유도
        
if __name__ == '__main__':
    # 디버깅 모드 on일 때 수정 내용이 반영됨
    # 브라우저 새로고침으로 수정내용 확인
    # entry point : 프로그램 시작점
    app.run(debug = True)



    