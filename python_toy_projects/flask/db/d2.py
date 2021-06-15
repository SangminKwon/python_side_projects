import pymysql as psql

# 변수를 선언 -> 메모리에 올린다
# 초기값의 경우 판단이 어렵다면 None으로 세팅한다.
connection = None
try:
    # 접속이 정상이면 connection 객체가 생성되고, 비정상이면 None으로 유지된다.
    connection = psql.connect(host = 'localhost', 
                            user = 'root', 
                            password = '1234', 
                            database = 'python_db', 
                            )
except Exception as e:
    print('접속오류',e)
finally:
    # 접속이 정상일 때만 실행
    if connection:
        connection.close()
        print('종료')