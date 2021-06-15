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
        cursor = connection.cursor()
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


if __name__ == '__main__':
    # 회원 테스트
    row = selectUsers('guest','123')
    print('회원조회결과:', row)
    # 비회원 테스트 (회원이 아님, 비번이 틀림, 아이디 틀림)
    row = selectUsers( 'guest', '2' )
    print( '회원조회결과:', row )
