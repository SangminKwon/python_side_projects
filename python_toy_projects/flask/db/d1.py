# 파이썬에서 mysql 계열 데이터베이스에 액세스하여 쿼리를 수행할 수 있는 모듈 준비
# 최종 산출물
# uid, upw를 입력받아서 쿼리를 수행하고 그 결과를 돌려주는 함수
# DB를 연결하고, 해제하는 부분은 통상 풀링, ORM 방식으로 처리(동접)하는 것이 정석이나,
# 본 모듈에서는 심플하게 함수 내에서 해결하겠다.
# 설치
# pip install pymysql

import pymysql as psql

# 1. 데이터베이스 접속 정보 구성 및 접속
connection  = psql.connect(host = 'localhost', # 데이터베이스의 주소 
                        user = 'root', # 사용자 계정명
                        password = '1234', # 사용자 계정 비밀번호
                        database = 'python_db',  # 데이터베이스 명
                        )
                        # port = 3306,  # 기본 포트는 3306

# 2. 접속 종료
connection.close()