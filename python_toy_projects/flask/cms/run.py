# 세션 : 접속자 정보를 서버측에서 관리, 서버측 메모리 사용, 자원 리스크가 있음
#       데이터베이스 형태, NO-SQL 형태로 서드파트 제품(혹은 패키지)들을 사용하여 처리
#       - 세션 생성(로그인 성공), 세션 체크(홈페이지, 세션을 가진자만 진입 허용), 세션 해제(로그아웃)
# 쿠키 : 접속자의 브라우저에 정보를 저장하여, 사용자를 특정하는 장치
#       아이디 기억, 기타 데이터 저장. 


from flask import Flask, request, render_template , redirect, session
from db import selectUsers

app = Flask(__name__)
# 세션 관련 작업 - 세션키 저장
# 해시 사용
app.secret_key = 'poweroverwhelming'

@app.route('/')
def home():
    # 세션체크
    if not 'uid' in session: # 세션 안에 uid라는 키가 존재하지 않는다면
        # 로그인 절차를 거치지 않고, 다이렉트로 서비스에 진입하였다.
        # 로그인 화면으로 다이렉트 이동
        return redirect('/login')

    return render_template('index.html')

@app.route('/logout')
def logout():
    # 1. 세션 제거
    if 'uid' in session: # uid가 세션의 키로 존재한다면? -> 세션이 있다.
        session.pop('uid', None)
    # 2. 홈페이지 이동 -> 로그인 이동
    return redirect('/')

@app.route('/login', methods = ['GET', 'POST']) 
def login():
    # 분기
    if request.method == 'GET':
        return render_template('login-v3.html')
    else: 
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        
        # 데이터 베이스 쿼리 수행(아이디, 비번 확인) 및 결과를 받는다.
        row = selectUsers(uid, upw)
        if row:
            # 4. 회원이면 -> 서비스 페이지로 이동 (리다이렉트)
            # -> 세션 생성(사용자의 어떤 정보를 저장할 것인가?)
            session['uid'] = uid
            # -> 서비스 페이지 이동 -> 리다이렉트
            return redirect('/')
        else:
            return """ 
                <script>
                    // 경고창
                    alert('아이디나 이름이 누락되었습니다.')
                    // 이전페이지 이동
                    history.back()
                </script>
                """

if __name__ == '__main__':
    app.run(debug = True)



    