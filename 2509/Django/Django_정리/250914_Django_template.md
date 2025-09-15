# Template System

## Django Template system
- 데이터 표현을 제어하면서, 표현과 관련된 부분을 담당


## Django Template Language
- Template에서 프로그래밍적 기능을 제공하는 시스템
    * 변수, 필터, 태그, 코멘트 등


## 템플릿 상속
- 기본 템플릿 구조의 한계
    * 모든 템플릿에 bootstrap 적용할 때 귀찮
- 템플릿 상속
    * 페이지의 공통요소를 포함하고, 하위 템플릿이 재정의 할 수 있는 공간을 정의하고 상속 구조 구축
- extends
    * 자식이 부모 템플릿을 확장한다는 것을 알림
    * 반드시 최상단, 2개 이상 사용 불가
- block
    * 하위에서 재정의


## 요청과 응답
- form을 통해 사용자와 애플리케이션 간의 상호작용
- form = client로부터 데이터를 서버로 전송, http 요청을 서버에 보내는 방법
    * action(어디로)
    * method(어떤 방식으로)
      * GET(조회)
      * POST(생성, 수정, 삭제 등)
- input
    * 입력 받을 수 있는 요소
    * name
      * 사용자가 입력한 데이터에 붙는 이름(key 값)
    * query string parameters(GET)
      * 사용자 입력 데이터를 url 주소에 파라미터를 통해 보냄
      * 보안 취약


## DTL 주의사항
- python 코드로 실행되는 것 아님
- 프로그래밍적 로직이 아니라 표현임
