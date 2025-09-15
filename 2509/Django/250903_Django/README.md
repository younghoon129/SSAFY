1. Django 프로젝트를 만든다.
2. index url에 접근하면 기본 페이지가 나오도록 한다.
'================================================'

3. form을 통해 검색을 입력받고, 입력한 값이 화면에 나오도록 한다. 검색입력 화면 하나, 결과 화면 하나 총 두개의 페이지가 필요하기 때문에 views 함수를 두개 작성해야됨, 앱의 url을 settings에 포함시켰는데 앱의 url이 없는 상태이므로 새로 만들어줘야 됨
  3-1 클라이언트가 작성한 걸 서버로 넣는 작업 = search.html

4. variable routing을 연습하기 위해서, 특정 detail/1 이런식으로 입력하면 해당 '1'을 보여주는
    페이지를 반환한다.


생성순서
1. 장고 설치
2. .gitignore, venv, requirements.txt 생성
3. source venv/Scripts/activate
3. 프로젝트 생성(django-admin startproject firstproject .)
4. 앱 생성(python manage.py startapp articles)
    * 4-1 프로젝트 안에서 앱들을 컨트롤해야되는데 현재 프로젝트와 앱들이 동일선상에 있어서
          프로젝트 안에 앱폴더를 세팅해야됨
    * 4-2 urls 세팅 해야됨
    * 4-3 views에 함수 작성
            def index(request):
                return render(request, 'articles/index.html')
5. 템플릿 구조는 미리 생성해주지 않는다.(사용자가 직접 해야됨)
    templates/articles/index.html
6. 실행해보는데 에러나면 재실행 해볼 것
