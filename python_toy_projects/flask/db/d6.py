import pymysql as psql

def selectUsers():
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
        
        cursor.execute(sql_query, ('admin','456'))
        row = cursor.fetchone()
        print(row)

    except Exception as e:
        print('접속오류',e)
    finally:
        if connection:
            connection.close()
        print('종료')

# 테스트
selectUsers()