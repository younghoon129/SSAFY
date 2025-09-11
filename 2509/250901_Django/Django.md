# Template System

- DTL
    * 일반

- template 상속
    * extends
    * block

- form
    *  client -> server
    * action, Get

- URL 관리
    * project/urls.py
    * app/urls.py




- 서치(form)
    * 같은 폴더 안에 각자 다른 폴더 안에 같은 이름의 파일이 있으면 별명 지어줘야됨
    * 별명도 같으면 app_name = '여기에 앱 이름 넣는다'
    * extends, block 쓰고 a 태그 써서 페이지 넘어가는 거

- 모델
    * 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것(상속)

- 모델 필드
    * DB 테이블의 필드(열)을 정의
    * 데이터 타입, 제약조건을 정의 (시험의 경우 점수가 정수형, 100점 이하)
        * 데이터 타입
            * 문자열
                * (Charfield)
                    * 제한된 길이의 문자열 저장
                    * max_length가 필수 옵션
                * TextFiled()
                    * 길이 제한 없는 대용량 텍스트 저장
                    * 무한대는 아님('일기' 이런 단어로 씀)
            * 숫자
            * 파일
            * 날짜
    * 제약조건(Field option)
        * null
        * blank
        * default
    * DateTimeField의 필드 옵션(변경사항도 들어가고 requirements.txt 와 같은 역할도 함)
        * update_at = (auto_now = True)
        * create_at = (auto_now_add =True)

    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
        author = models.CharField()
        creaeted
=====================================================
    python manage.py makemigrations, (설계도 작성)
    python manage.py migrate (최종 설계도를 DB에 전달하여 반영)
=====================================================
에러 메세지 mygrate 셤 나올 법 한데?


- admin site
    * python manage.py createsupoeruser
    * admin.site.register(Article)


- DB 초기화 
    - mygration  

- SQL 얘기하면서 postrgreSQL 얘기나옴
    * 한번 공부해보길 권장

- 마지막 정리 한번 보기