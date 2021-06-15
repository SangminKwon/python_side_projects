""" 
    - 서버 코드 및 각종 html 내부에서 URL을 하드코딩하지 않는다.
    - URL 변경시 하드코딩된 모든 부분을 다 교체해야 한다
    - URL_for('url과 같이 세팅된 함수명') -> 차후에 URL로 대체
        - URL이 변경되어도 함수명은 바뀌지 않는다.
    - url_for('home') => url_for('home')

 """

from flask import Flask, request, render_template , redirect, session, url_for, jsonify
from db import selectUsers,selectBbs, selectKeyword

app = Flask(__name__)
app.secret_key = 'poweroverwhelming'

@app.route('/')
def home():
    # 세션체크
    if not 'uid' in session: 
        return redirect(url_for('login'))
    # 렌더링시 데이터를 키=값 형태로 자유롭게(개수도 무관) 전달가능
    return render_template('index.html', title = 'AI_Busan')

@app.route('/logout')
def logout():
    if 'uid' in session:
        session.pop('uid', None)
    if 'name' in session:
        session.pop('name', None)
    return redirect(url_for('home'))

@app.route('/login', methods = ['GET', 'POST']) 
def login():
    if request.method == 'GET':
        return render_template('login-v3.html')
    else: 
        uid = request.form.get('uid')
        upw = request.form.get('upw')
        
        row = selectUsers(uid, upw)
        if row:
            session['uid'] = uid
            # 회원정보 중 회원의 이름을 세션에 저장한다.
            session['name'] = row['name']
            return redirect(url_for('home'))
        else:
            return """ 
                <script>
                    // 경고창
                    alert('아이디나 이름이 누락되었습니다.')
                    // 이전페이지 이동
                    history.back()
                </script>
                """

# 게시판 페이지
@app.route('/bbs')
def bbs():
    # 쿼리 결과를 들고 바로 렌더링으로 진입
    return render_template('bbs.html', bbs = selectBbs(),title = 'AI_Busan')

# 검색
@app.route('/search')
def search():
    # 검색어 획득
    keyword = request.args.get('q')
    # 쿼리 결과 획득
    rows = selectKeyword(keyword)
    # 응답 -> Json으로 응답한다.
    if not rows:
        # rows가 None이면 json으로 변환할 수 없기 때문에
        # 결과가 없다는 것을 json으로 바꿀 수 있는 구조로 변경
        rows = []
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug = True)



    