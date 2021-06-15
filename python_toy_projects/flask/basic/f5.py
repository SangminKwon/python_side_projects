'''
    상황) 클라이언트가 서버 측에 페이지를 요청할 시 데이터를 함께 전달하고 싶다.
    - GET
        - 데이터를 전달하지 않아도, 일반적인 모든 페이지는 GET방식으로 페이지를 요청
        - 아무런 표시가 없다면 모두 get방식
            - 다른 방식은 명시적 표기가 필요(POST, PUT, HEAD, DELETE, ...)
        - 형식
            - 주소(URL)뒤에 ?키=값&키=값 : 주소형식(모든 웹 프로그래밍 공통)
    - 클라이언트가 서버측으로 데이터를 전달할때 request 라는 객체를 타고 서버에 전달된다
'''


from flask import Flask, request

app = Flask(__name__)

# ~/login
# 데이터 전달
# ~/login?uid=guest&name=게스트
@app.route('/login')
def login():
    # step 1 : 클라이언트가 보낸 데이터를 추출
    uid = request.args.get('uid')
    name = request.args.get('name')
    print(uid, name)
    if not (uid and name): # 부정상황을 잡는 조건식
        return '''
            <script>
                alert('아이디나 이름이 누락되었습니다.')
            </script>
        '''
    return f'<h1>로그인 페이지 {uid} {name}</h1>'

if __name__ == '__main__':
    # 디버깅 모드 on일 때 수정 내용이 반영됨
    app.run(debug = True)