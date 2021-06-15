from flask import Flask, request, render_template
from werkzeug.utils import redirect
from db.d7 import selectUsers

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>홈페이지</h1>'

@app.route('/login', methods = ['GET', 'POST']) 
def login():
    # 분기
    if request.method == 'GET':
        return render_template('login.html')
    else: 
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        
        # 데이터 베이스 쿼리 수행(아이디, 비번 확인) 및 결과를 받는다.
        row = selectUsers(uid, upw)

         # 4. 회원이면 -> 서비스 페이지로 이동 (리다이렉트)
        if row:
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



    