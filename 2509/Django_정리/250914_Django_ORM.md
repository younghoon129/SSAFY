# ORM
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간 데이터 변환 기술
- django 에서의 ORM = queryset API
  * 사용 이유
    * 데이터베이스 추상화
    * 생산성 향상
    * 객체 지향적 접근

## Queryset API
- python의 모델 클래스와 인스턴스를 활용하여 DB에 데이터를 수정, 저장 등 하는 것
- Query
  * 파이썬코드 -> ORM -> SQL 변환 -> QuerySet 자료형 형태로 우리에게 전달
- QuerySet
  * 전달 받은 객체 목록
  * 사용 목적 : 지연 평가, 체이닝

## CRUD
- 소프트웨어가 가지는 기본적인 데이터 처리 기능
- CREATE
- READ
  * return QuerySets
    * all(), filter()
  * return instance
    * get()
      * 1개 아니면 error
      * 고유성을 보장하는 조회에서 사용(예시- pk)
- UPDATE
- DELETE


