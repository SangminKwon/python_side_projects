'''
    상황) 클라이언트가 서버측에 페이지를 요청 시 데이터를 함께 전달하고 싶다.
        ex) 로그인, 검색, 게시판, 글 상세보기, 게시판 페이지 이동
    - 데이터를 서버로 보내는 방식 => 
        -method(메소드)
            - GET : 가장 일반적, 작은 양의 데이터 전송, 보안에 취약(주소 뒤에 ?키=값&키=값 형태로 드러남)
            - POST : 보안에 우수, 대량의 데이터 전송 가능, 데이터가 숨겨져서 전송됨
            - ...
        - 동적 파라미터 방식
            - URL에 실어서 전송, 보안에 취약, 간편하게 사용시
            - 동적 파라미터 방식은 메소드 방식과 혼용해서 사용가능하다
                - ex) GET + 동적 파라미터 / POST + 동적 파라미터
        - 데이터는 패킷 단위로 전송이 되며, 패킷의 헤더에 데이터가 세팅됨.
            - GET, 동적파라미터 방식
        - 대량의 데이터, 숨겨야할 데이터는 패킷의 body를 통해서 전달된다.
            - POST
    - 동적 파라미터 실습
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home(): 
    return '<h1>홈페이지</h1>'

# 동적 파라미터 적용 기본
# <news_id> : 여기에 뉴스 아이디를 넣어서 주소창에 넣으면 된다.
# ~news/safdsfwqefno12314
@app.route('/news/<news_id>')
def news(news_id): 
    return f'클라이언트가 전달한 데이터 [{news_id}]'

# 데이터를 1개 이상 서버측으로 전달 가능한가?
# ~/news2/123/제목
@app.route('/news2/<news_id>/<news_title>')
def news_two(news_id, news_title): 
    return f'클라이언트가 전달한 데이터 [{news_id}][{news_title}]'

# 타입 제한 -> int, float, path
# news_id는 정수값만 허용
# 형식에 어긋난다면 Not Found 처리
@app.route('/news3/<int:news_id>')
def news3(news_id): 
    return f'클라이언트가 전달한 데이터 [{news_id}]'

# path => 서버측으로 전달할 내용을 무한대로 가변적으로 확장할 수 있다.
@app.route('/news4/<path:news_id>')
def news4(news_id):
    datas = news_id.split('/')
    # 데이터를 추출하고 사용을 리스트의 인덱싱 형식으로 사용
    return f'클라이언트가 전달한 데이터 [{datas[0]}]'


if __name__ == '__main__':
    # 디버깅 모드 on일 때 수정 내용이 반영됨
    app.run(debug = True)