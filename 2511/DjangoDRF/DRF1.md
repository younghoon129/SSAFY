# DRF1
## DRF
- DRF
    - Django REST framework
    - Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- API
    - 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
- REST
    - API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- RESTful API
    - 데이터를 정의하고, 데이터에 대한 주소를 지정하는 전반적인 방법을 서술
    - 각각 API 서버 구조를 작성하는 모습이 다름으로, 어느정도 약속을 만들어서 다같이 통일해서 쓰자는 의의

- REST에서 자원(데이터)을 정의하고 주소를 지정하는 방법
    - 개발 시 항상 '자원 중심 + 동작 명확화 + 일관된 응답 포맷' 을 기준으로 설계할 것
    - 자원의 '식별'
        - URL
    - 자원의 '행위'
        - HTTP Methods
    - 자원의 '표현'
        - JSON 데이터
        - 표현되는 데이터 결과물

- 자원의 '식별'
    - Schema or Protocol
        - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지 나타냄
        - http(s)
    - Domain Name(구입)
        - 요청 중인 웹 서버
        - IP 주소 쓰는데 사람이 쓰기 어려우니 www.google.com 같은거 씀
    - Port
        - 문 같은 개념 (HTTP-80, HTTPS-443)
        - 표준 포트는 생략 가능
    - Path
        - 웹 서버의 리소스 경로
        - 초기에 물리적 위치를 나타냇지만, 오늘날 추상화된 형태의 구조를 표현
    - Parameters
        - 웹 서버에 제공하는 추가적인 데이터
        - '&' 기호로 구분되는 key-value 쌍 목록
        - 서버는 리소스 응답 전 파라미터를 사용하여 추가 작업 수행 가능
    - Anchor
        - '북마크' 개념
        - 서버에 전송 안되고 브라우저에게 해당 지점으로 이동할 수 있도록 함
- Serialization
    - 직렬화 해줌
    - 데이터 구조나 객체 상태를 재구성할 수 있는 포맷으로 변환하는 과정
    - 어떠한 언어나 환경에서도 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
- Serializer
    - 변환해주는 클래스
- ModelSerializer
    - Django 모델과 연결된 Serializer 클래스
    - 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 직렬화 진행

## CRUR with ModelSerializer
- ModelSerializer 쓸 때 받는 인자가 queryset 일 경우(데이터가 2개 이상일 경우) many=True 해야됨
- api_view
    - DRF view 함수에서 필수로 작성
    - 허용한 메서드에만 응답
    - 추가 안됨 메서드 요청엔 405 Method Not Allowed로 응답
- 생성
    - 성공: 201 Created 응답
    - 실패: 400 Bad request 응답
- 수정
    - 부분 수정 하려해도 다른 필수 필드들도 함께 전송해야 됨
    - partial=False: 일부 필드만 전달 허용하게함
    - PATCH: 권장(일부 수정)
from django.framework import status
from django.framework.decorators import api_view
from django.framework.response import response
