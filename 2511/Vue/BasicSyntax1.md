# BasicSyntax1
- Template Syntax
    - Vue는 DOM을 컴포넌트 인스턴스의 데이터에 선언적으로 바인딩할 수 있는, HTML 기반 템플릿 구문을 사용
    - 선언적 바인딩: JavaScript 데이터(상태)가 바뀌면 DOM(화면)이 알아서 업데이트되는 것
    - 템플릿 구문은 HTML에 Vue만의 특별한 문법을 추가해서 사용하는 것
- Text Interpolation
    - 데이터 바인딩의 가장 기본적인 형태(**v-text**)
    - 이중 중괄호 구문 (콧수염 구문)을 사용
    - 콧수염 구문은 해당 컴포넌트 인스턴스의 msg 속성 값으로 대체
    - msg 속성이 변경될 때마다 업데이트 됨
- Raw HTML
    - 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 **v-html**을 사용해야 함
    - 보안 위험(XSS-쿠키,세션 탈취할 수도 있음)이 있으므로 권장 안함
- Attribute Bindings
    - 콧수염 구문은 HTML 속성 내에서 사용할 수 없기 때문에 **v-bind**를 사용
    - HTML의 id 속성 값을 vue의 dynamicld 속성과 동기화 되도록 함
    - 바인딩 값이 null이나 undefind인 경우, 해당 속성은 렌더링 요소에서 제거됨
- JavaScript Expressions
    - Vue는 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
    - Vue 템플릿에서 JavaScript 표현식을 사용할 수 있는 위치
        - 콧수염 구문 내부
        - 모든 디렉티브의 속성 값('v-'로 시작하는 특수 속성)
- Expressions 주의 사항
    - 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음
        - 표현식은 값으로 평가할 수 있는 코드 조각(return 뒤에 사용할 수 있는 코드여야 함)
    - 작동하지 않는 경우

## Directive
- 'v-' 접두사가 있는 특수 속성
- DOM 요소에 특정 반응형 동작을 적용하는 명령어
- v-if, v-for
- JavaScript 로직을 HTML 템플릿 안에서 선언적으로 사용하여, 코드를 깔끔하고 직관적으로 유지
- 특징
    - Directive의 속성 값은 단일 JavaScript 표현식이어야 함(v-for, v-on 제외)
    - 표현식 값(ex: 'seen')이 변경될 때 DOM에 반응적으로 업데이트를 적용
- Directive 전체 구문
    - Name(이름): Directive의 핵심 이름으로, 어떤 종류의 기능을 수행할지를 의미('v-')
    - Argument(전달 인자): Directive가 '무엇에 대해' 동작할 지 알려주는 구체적인 대상
        - directive 뒤에 콜론 (:)으로 표시되는 인자
    - Modifiers(수식어): 점으로 표시되는 특별한 접미사로, Directive의 기본 동작을 수정할 수 있음
        - (.) 으로 표시되는 특수 접미사로, directive가 특별한 방식으로 바인딩되어야 함을 나타냄
        - 체이닝 가능
    - Value(값): Directive에 연결될 JavaScript 표현식

## v-bind
- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩
- 데이터 값에 따라 이미지, 스타일, 클래스 등 자유롭게 변경 가능
- v-bind: -> (:) 으로 생략 가능 (:)만 있으면 무조건 v-bind
- Dynamic attribute name(동적 인자 이름)
    - 대괄호([])로 감싸서 directive argument에 JavaScript 표현식을 사용할 수 있음
    - 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용됨
    - 대괄호 안의 값이 null이면 해당 속성, 이벤트 리스너 아예 제거됨

## Class and Style Bindings
- Class and Style Bindings(클래스와 스타일 바인딩)
    - class와 style은 모두 HTML 속성이므로 다른 속성과 마찬가지로 v-bind를 사용하여 동적으로 문자열 값을 할당할 수 있음
    - Vue는 class 및 style 속성 값을 v-bind로 사용할 때 객체 또는 배열을 활용하여 작성할 수 있도록 함
        - 단순히 문자열 연결을 사용하여 이러한 값을 생성하는 것은 번거롭고 오류가 발생하기가 쉽기 때문
    - Binding HTML Classes: Binding to **Objects**
        1. 객체를 :class에 전달하여 클래스를 동적으로 전환 가능
            - isActive -> Boolean 값에 의해 active 클래스의 존재 결정
            - const isActive = ref(ture), :class='{active:isActive}'
        2. 객체에 더 많은 필드를 포함하여 여러 클래스를 전환 가능
            - :class directive를 일반 클래스 속성과 함께 사용 가능
        3. inline 방식이 아닌 반응형 변수를 활용해 객체를 한번에 작성하는 방법
            - script 안에 class 정의할 때 안에 여러 객체 넣는거
    - Binding HTML Classes: Binding to **Arrays**  -> 이 파트 하면 다른 파트 이해하기 쉬움
        1. :class를 배열에 바인딩하여 클래스 목록을 적용 가능
            - :class='[값1, 값2]' -> :class='값1값2'  같은 의미
    - Binding inline styles: Binding to **Objects**
        1. :style은 HTML의 style 속성에 JavaScript 객체를 바인딩하는 것을 지원
            - kebab-cased 키 문자열도 지원 (단, camelCase 작성 권장)
            - :style='{color:activeColor, fontSize('font-size'): fontSize+'px'}'
            - -> style='color: crimson; font-size: 50px;'  같은 의미
        2. inline 방식이 아닌 반응형 변수를 활용해 객체를 한번에 작성하는 방법
            - script 안에서 const 변수 안에 여러 객체 넣고 :style='styleObj' 로 함
    - Binding inline styles: Binding to **Arrays**
        1. 여러 스타일 객체를 배열에 작성해서 :style을 바인딩할 수 있음
            - 작성한 객체는 병합되어 동일한 요소에 적용
            - style='[styleObj, styleObj2]'
            - -> style='color: crimson; font-size: 50px;'  같은 의미

## v-on
- DOM 요소에 이벤트 리스너를 연결 및 수신
- 약어 : @
- handler 종류
    1. inline handlers: 이벤트가 트리거 될 때 실행 될 JavaScript 코드
        - 주로 간단한 로직에 사용(주로 한번만 쓰는 로직)
        - 복잡한 표현식이 들어가면 템플릿이 지저분해지고 코드 이해하기 어려움
        - 재사용이 불가능해 유지보수 어려움
        - event 인자 접근
            1. inline Handlers에서 원래 DOM 이벤트에 접근하기
                - $event 변수를 사용하여 메서드에 전달
                - %event 변수를 전달하는 위치는 상관 없음
    2. Method handlers: 컴포넌트에 정의된 메서드 이름
        - 메서드 핸들러는 setup에 정의된 메서드를 호출하는 방식
        - 로직이 복잡할 경우, Method를 분리하면 템플릿이 간결해지고 코드를 재사용하기 좋음
        - inline handlers로는 불가능한 대부분의 상황에서 사용
        - **@click='myFunc'**처럼 괄호 없이 메서드 이름만 연결하면, 핸들러의 첫 번째 인자로 DOM의 event 객체가 자동으로 전달 됨
            - @click='greeting'
        - 기본 이벤트 대신 사용자 지정 인자를 전달할 수도 있음
            - @click='greeting('hello')'

## Modifiers
- Event Modifiers
    - 디렉티브 뒤에 (.)으로 붙여, 특별한 동작을 추가하는 기능(체이닝 가능)
    - event.preventDefault()와 같은 코드를 메서드 안에 직접 작성할 필요가 없도록 한다.
    - 대신 stop, prevent, self 등 다양한 modifiers를 제공
        - prevent -> 버블링 일어남(기본 동작 취소)
        - stop -> 버블링 안일어남(기본 동작 취소)
    - 메서드 로직을 순수하게 데이터 관련 처리에만 집중시키기 위함
- Key Modifiers
    - 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음
        - Enter 키가 입력 되었을 때만 onSubmit 이벤트를 호출하기
            - @keyup.enter
        - Ctrl + Enter로 댓글 등록하기
            - @keyup.ctrl.enter
            
## Form Input Bindings
- form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태(데이터)에 동기화해야하는 경우(양방향 바인딩)
- 사용자가 입력할 때 사용가능
    - 태그: input, textArea, select
- 양방향 바인딩 방법 (사용자의 입력이 있어야지만 사용가능)
    1. v-bind({:},JS에서 HTML로 바인딩하는 것), v-on({@},HTML에서 JS로 인자를 전달하는 것)을 함께 사용
        1. v-bind로 input 요소의 value 속성을 반응형 변수에 연결
        2. v-on으로 input 이벤트가 발생할 때마다, input의 현재 값을 반응형 변수에 저장
    2. v-model 사용
        - IME가 필요한 언어(한국어, 중국어, 일본어 등)의 경우 v-model이 제대로 업데이트되지 않음
            - v-bind, v-on 방법 사용해야 함
        - form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
        - 사용자 입력 데이터와 반응형 변수를 실시간 동기화
        - 무조건 ref()로 감싸줘야 됨
        - 다양한 입력(input) 양식
            - v-model은 단순 Text input 뿐만 아니라 다양한 타입의 사용자 입력 방식과 함께 사용가능
            - Checkbox
                - 단일 체크박스, boolean 값 활용
                - 여러 체크박스, 배열 활용
                    - 초기 반응형 변수를 배열로 초기화
                    - 해당 배열에는 현재 선택된 체크박스의 값이 포함됨
                        - checkedNames=ref([1,2,3,4,5])
            - Select
                - select에서 v-model 표현식의 초기 값이 어떤 option과도 일치하지 않는 경우, select 요소는 '선택되지 않은(inselected)' 상태로 렌더링 됨
                - 선택안됐을 때 안내해주기 위한 보여주기 식 글자(이 글자는 선택할 수 없음) 설정
            - Radio
            - textarea

## 접두어 $
- '$' 붙은 변수
    - 주로 Vue 인스턴스 내부 상태를 다룰 때 사용
    - Vue 인스턴스 내에서 사용할 수 있도록 Vue가 제공하는 공용 프로퍼티
    - 사용자가 지정한 반응형 변수나 메서드와 구분하기 위함
    - '_' -> 내부용이므로 직접 사용 하면 안됨(예고 없이 변경될 수 있음)
    - 내가 만드는 데이터와 메서드 이름에 $나 ``접두사를 사용하지 않는 것이 좋음

## IME(Input Method Editor)
- 사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자(비영어권 언어)를 입력할 수 있도록 하는 운영 체제 구성 프로그램
    - 일반적으로 키보드 키보다 자모가 더 많은 언어에서 사용해야 함
    - IME가 활성화된 상태(예: 한글 조합 중)에서 input 이벤트가 발생하는 방식과 v-model의 업데이트 방식이 충돌하여, 의도치 않은 동작 발생할 수 있음
    - v-model에 **.lazy** 수식어를 붙이면 문제 해결할 수 있지만 데이터가 실시간 반영하지 않고, 사용자가 입력을 마친 후 다른 곳을 클릭하는 등 포커스를 잃었을 때 한 번에 반영됨
     