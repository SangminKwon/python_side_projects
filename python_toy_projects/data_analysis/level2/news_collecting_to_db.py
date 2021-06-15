# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json

CLIENT_ID = '7vmeLsVv1PbrA_ToCPU4'
CLIENT_SECRET = 'OfsqxaTfOe'

# 문자열에서 가비지를 제거하는 함수 선언
def remove_noise(raw_string):
  '''
    raw_string : 특정 기호를 제거하고 싶은 문자열
  '''
  return raw_string.replace('<b>','').replace('</b>','').replace('&quot','').replace(';',',')


# 함수는 재사용성, 유지 보수의 용이함 등을 위해 사용
# 클로저 : 자신을 둘러싼 스코프의 환경변수, 설정값 등을 기억하고 있는 함수

def search_by_naver_api(searchKeyword):
  
  encText = urllib.parse.quote(searchKeyword)
  url = 'https://openapi.naver.com/v1/search/news.json'
  url = f'{url}?query={encText}&display=10&start=1'

  request = urllib.request.Request(url)
  request.add_header("X-Naver-Client-Id",CLIENT_ID)
  request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
  response = urllib.request.urlopen(request)


  rescode = response.getcode()
  if(rescode == 200):
    tmp = json.load( response )
    response_body = response.read()
    print(response_body.decode('utf-8'))
      
  else:
    print("Error Code:" + rescode)



  # news_list = tmp['items']
  # titles = [ news['title'].replace('<b>','').replace('</b>','').replace('&quot','').replace(';',',') for news in news_list]
  # print(tmp)
  # return titles

  # 데이터를 재구성하여 리턴한다. 구조는 동일하지만, <br>등 가비지를 제거해야 한다.
  # 리스트 컴프리헨션을 사용

  return [{
      'title'       : remove_noise(item['title']),
      'originallink': item['originallink'],
      'link'        : item['link'],
      'description' : remove_noise(item['description']),
      'pubDate'     : item['pubDate'],
  } for item in tmp['items']]

#함수 호출

result = search_by_naver_api('아마존')


# [  {}  ] => DataFrame으로 변경
import pandas as pd

df = pd.DataFrame.from_dict(result)

# 파이썬에서 MariaDB를 액세스 할 수 있게 해주는 드라이버.
import pymysql
# 대량으로 데이터를 디비에 편하게 밀어넣고 싶다 -> 고차원 모듈이 필요
from sqlalchemy import create_engine
# DataFrame을 DB에 넣도록 SQL을 전송하는 기능
import pandas.io.sql as pSql

# 1. DB 연결 문자열 생성
id = 'root'
pw = '1234'
host = '127.0.0.1'
port = '3306'
database = 'python_db'
db_url = f'mysql+pymysql://{id}:{pw}@{host}:{port}/{database}'

# 2. 연결 엔진 생성
engine = create_engine(db_url, encoding = 'utf-8')

# 3. 실제 데이터베이스에 연결
conn = engine.connect()

# 4. 데이터 입력

df.to_sql(name ='news_tbl', con =conn, if_exists ='append', index = False)

# 5. 연결했으면 연결종료 => I/O을 수행하면 반드시 닫는다.
conn.close()