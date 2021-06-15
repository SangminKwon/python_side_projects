# 파이썬 기반 웹 프로그래밍
    - 목적
        - 웹 프로그래밍의 이해
        - 파이썬을 이용한 SW 개발 능력 향상
        - Final Project 산출물에 사용하는 기술
        - 모든 플랫폼(windows, MacOS ...)에 사용되는 범용적인 웹 환경 구축
    - 과목
        - 파이썬
        - 웹 서비스 구성
            - 클라이언트 사이드
                - 구성 요소
                    - html5 : 구조, 컨텐츠, 뼈대 역할
                    - css3 : 디자인, 프레젠테이션, 레이아웃, css selector,
                            애니메이션, 반응형 UI 구성
                        - 부트스트랩 기반 템플릿들을 활용하여서 UI 구성
                    - javascript(ECMA 2020, 브라우저마다 지원여부가 달라짐)
                        : 이벤트 처리, ajax 처리, 통신 처리, DOM 조작(화면 동적 구성)
                            사용자와 브라우저간의 인터렉션(상호작용) 담당
                            - jQuery 사용
                    - 최신 트렌드(4~5년 전부터 진행)
                        - 웹 서비스의 무게중심이 서버 -> 클라이언트로 이동
                        - SPA(single page application)
                            - Anglar (구글) : 가장 오래 되었음. TypeScript
                            - React  (페이스북) : 웹, 앱(react-native). TypeScript  or javascript
                                                    PC용 애플리케이션(+일렉트론)
                            - Vue    (커뮤니티) : 
                                                    PC용 애플리케이션
            - 서버 사이드
                - 웹 프로그래밍
                - 결과물
                    - UI 有 (일반적인 웹 프로그래밍, 화면구성, 서버측 렌더링)
                    - UI 無 (미들웨어 , 업무만 수행 , json or xml 전송)
                - 개발도구
                    - asp, servlet/jsp, php
                    - ejb -> spring (java, 2000년대)
                    - node.js, .net 기반, 파이썬웹, ...(~ 현재까지)
                    - 현재 : node.js(js), spring(java), 파이썬웹(python), 닷넷기반(C#), php, ...
                    - 파이썬웹
                        - flask
                            - 자유도가 높다.
                            - ex) 주피터 노트북
                            - 마이크로 에디션, node.js와 유사
                        - Django
                            - 프레임워크(프레임워크의 규칙에 따라 개발) 기반
                            - spring과 유사
            - 데이터베이스
                - RDBMS
                    - 관계형 데이터베이스
                        - 사용언어 : SQL

                    - light
                        - MySQL
                        - MariaDB
                    - enterprise
                        - Aurora
                        - Oracle
                        - MS-SQL
                        - IBM
                - No-SQL
                    - 빅데이터 출현으로 등장
                    - JSON 형태
                    - 실시간 데이터베이스
                        - MongoDB, 하둡
                        - Realm, Firebase(google)
    - 개발환경구축
        - python 설치
        - 필요한 패키지 설치
            - pip install 패키지이름 (일반)
            - conda install 패키지이름 (콘다)
        - VScode 설치
        - 구동
            - python xx.py
            - 삼각형 Run 버튼 클릭
            
# 데이터베이스 쿼리

    - 회원정보 입력 쿼리 예제
        - INSERT INTO python_db.users_tbl (uid, upw, name, regdate) VALUES ('guest', '123', '게스트', '2021-06-10 10:23:16');
    - 로그인 처리
        - SELECT * FROM users_tbl WHERE uid = 'guest' AND upw = '123';

# 추가 사항
    - 파이썬 연습용 자료
    - 플라스크 뒤쪽 고급 내용
        - 블루프린트를 통한 구조 고도화
        - 라이프사이클을 통한 요청과 응답처리(세션 처리)
        - 채팅

    - 배포
        - AWS에서 배포하는 절차
            - febric 기술 이용
            - 로컬에서 리눅스로 직접 붙어서 자동 세팅, flask 배포
    
