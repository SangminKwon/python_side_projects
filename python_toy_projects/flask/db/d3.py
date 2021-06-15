import pymysql as psql

connection = None
try:
    connection = psql.connect(host = 'localhost', 
                            user = 'root', 
                            password = '1234', 
                            database = 'python_db', 
                            )
    # 쿼리수행
    # 1. 커서 획득
    cursor = connection.cursor()

    # 2. sql 쿼리 생성
    sql_query = """ 
        SELECT 
            *
        FROM
            users_tbl
        WHERE
            uid = 'guest'
        AND
            upw = '123' 
     """

    # 3. sql 쿼리 실행
    cursor.execute(sql_query)

    # 4. 결과 패치
    row = cursor.fetchone()

    # 5. 결과 확인
    # 추가적으로 순서 의존성을 없앨 필요가 있음.
    print(row)
    
except Exception as e:
    print('접속오류',e)
finally:
    if connection:
        connection.close()
        print('종료')