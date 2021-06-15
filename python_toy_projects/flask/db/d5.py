import pymysql as psql

# uid, upw가 고정되어 있다 => sql에서 뽑아서, 쿼리 수행시
# 인자로 전달되게 수정

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
    # 쿼리를 수행할 때, 파라미터를 전달할 수 있다.
    # 이때 전달되는 값은 ''를 자동으로 붙여주고, 형식은 tuple 사용
    cursor.execute(sql_query, ('admin','456'))
    row = cursor.fetchone()
    print(row)

except Exception as e:
    print('접속오류',e)
finally:
    if connection:
        connection.close()
        print('종료')