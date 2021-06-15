# -*- coding: utf-8 -*-
import os
import sys
import urllib.request
import json

CLIENT_ID = '7vmeLsVv1PbrA_ToCPU4'
CLIENT_SECRET = 'OfsqxaTfOe'

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

  news_list = tmp['items']
  titles = [ news['title'].replace('<b>','').replace('</b>','').replace('&quot','').replace(';',',') for news in news_list]
  return titles

result1 = search_by_naver_api('한미정상회담')
print(result1)
result2 = search_by_naver_api('손흥민')
print(result2)
result3 = search_by_naver_api('아마존')
print(result3)