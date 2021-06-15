import pymysql as psql

# MVC 모델로 웹, M:모델/디비, V:뷰/화면/화면, C:비즈니스로직/커맨드
# d7은 쿼리만 수행하고, 결과만 돌려준다. 그 의미는 판단하지 않는다
# 함수화, 기능 테스트
# 회원이면 dict 형태로 전달(리턴)
# 회원아니면 None으로 전달(리턴)
def selectUsers(uid, upw):
    row = None # 쿼리 결과
    connection = None
    
    try:
        connection = psql.connect(host = 'localhost',
                                user = 'root', 
                                password = '1234', 
                                database = 'python_db',
                                cursorclass = psql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql_query = """ 
                SELECT 
                    *
                FROM
                    users_tbl
                WHERE
                    uid = %s
                AND
                    upw = %s; 
            """
            cursor.execute(sql_query, (uid,upw))
            row = cursor.fetchone()
        # print(row)

    except Exception as e:
        print('접속오류',e)
    finally:
        if connection:
            connection.close()
        print('종료')
    return row

# 게시판 목록 가져오기
def selectBbs(pageNo = 1 , pageAmt= 10):
    """ 
        selectBbs : 게시판 목록 가져오는 함수, news_tbl 테이블 조회
        pageNo : 페이지 번호, 1,2,3 등등. 기본값 1
        pageAmt : 페이지당 몇 개의 목록을 보여줄것인가. 기본값 10
     """
    rows = None # 쿼리 결과
    connection = None
    
    try:
        connection = psql.connect(host = 'localhost',
                                user = 'root', 
                                password = '1234', 
                                database = 'python_db',
                                cursorclass = psql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql_query = f'SELECT * FROM news_tbl ORDER BY id DESC LIMIT {(pageNo-1)*pageAmt}, {pageAmt}; '
            cursor.execute(sql_query)
            rows = cursor.fetchall()

    except Exception as e:
        print('접속오류',e)
    finally:
        if connection:
            connection.close()
        print('종료')
    return rows


# 검색
def selectKeyword(keyword):
    """ 
        selectKeyword : 뉴스 테이블에서 검색결과를 가져오는 함수
        keyword : 검색어
     """
    rows = None # 쿼리 결과
    connection = None
    
    try:
        connection = psql.connect(host = 'localhost',
                                user = 'root', 
                                password = '1234', 
                                database = 'python_db',
                                cursorclass = psql.cursors.DictCursor)
        with connection.cursor() as cursor:
            sql_query = f"SELECT * FROM news_tbl WHERE title LIKE '%{keyword}%';"
            cursor.execute(sql_query)
            rows = cursor.fetchall()

    except Exception as e:
        print('접속오류',e)
    finally:
        if connection:
            connection.close()
        print('종료')
    return rows

if __name__ == '__main__':
    if False:
        # 회원 테스트
        row = selectUsers('guest','1')
        print('회원조회결과:', row)
        # 비회원 테스트 (회원이 아님, 비번이 틀림, 아이디 틀림)
        row = selectUsers( 'guest', '2' )
        print( '회원조회결과:', row )
    print(selectBbs())