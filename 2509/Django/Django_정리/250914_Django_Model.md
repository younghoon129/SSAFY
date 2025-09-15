# Model

## Django Model
- DB의 테이블을 정의, 데이터를 조작할 수 있는 기능 제공
- 테이블 구조를 어떻게 설계할지에 대한 코드만 작성해도 됨
  

## Model field
- DB테이블의 필드(열), 데이터 타입, 제약 조건을 정의
    * Type
      * 문자열
        * CharField
          * 제한된 길이의 문자열
        * TextField
          * 제한 없이 문자열
      * 숫자
        * IntegerField, FloatField
      * 날짜/시간
        * DateTimeField, TimeField, DateField
        * auto_now(update)
        * auto_now_add(create)
      * 파일
        * FileField, ImageField
    * 제약사항
      * null
      * blank
      * default


## Migrations
- id는 자동으로 생성
- 이미 생성된 테이블에 필드를 추가하고 싶을 때, model class에 변경사항 생겼을 때
  - 필드 추가하고 migrations, migrate 또 하면 됨
  - 단 기존 데이터가 있을 경우 추가할 필드의 기본 값 설정 필요
    1. 직접 기본 값 입력, timefield일 경우 입력 없이 엔터치면 현재 시간 업로드
    2. 필드 추가할 때 default로 지정


## automatic admin interface
- admin.py
    * model 상속 후
    * admin.site.register(model명)


## DB 초기화
- db, migrations 파일 삭제 해야됨


## migrations 기타 명령어
- python manage.py showmigrations
    * migrate 됐는 지 확인여부 명령어
    * X 표시일 경우 적용 완료 의미
- python manage.py sqlmigrate articles 0001
    * 해당 파일이 어떻게 sql언어로 번역되어 db에 전달하는 지 확인가능