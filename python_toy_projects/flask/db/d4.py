import pymysql as psql

connection = None
try:
    connection = psql.connect(host = 'localhost', 
                            user = 'root', 
                            password = '1234', 
                            database = 'python_db',
                            # 결과물이 dict객체로 온다. 기본값은 tuple
                            cursorclass = psql.cursors.DictCursor)
    # 일반적으로 연결해도 커서의 타입을 밑에처럼 지정하면 동일한 결과가 나온다.
    # cursor = connection.cursor(psql.cursors.DictCursor)
    cursor = connection.cursor()
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
    cursor.execute(sql_query)
    row = cursor.fetchone()
    print(row['name'])

except Exception as e:
    print('접속오류',e)
finally:
    if connection:
        connection.close()
        print('종료')