# Router
- Routing
  - 네트워크에서 경로를 선택하는 프로세스
  - 사용자가 접속한 URL 주소에 따라 적절한 페이지(컴포넌트)를 보여주는 기능
  - 미리 정의된 경로에 따라 어떤 내용을 보여줄지 결정
- SSR에서의 Routing (SSR: 서버에서 완성된 HTML 페이지를 만들어, 브라우저에 보내는 방식)
  - SSR에서 routing은 서버 측에서 수행
  - 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
- CSR에서의 Routing (CSR: 서버는 뼈대만, 브라우저가 직접 페이지를 그리는 방식)
  - CSR에서의 routing은 클라이언트 측(브라우저)에서 수행
  - 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드 하지 않음
    - 일부 렌더링
- SPA에서 Routing이 없다면 (SPA: 하나의 페이지 안에서, 내용만 바꿔가며 보여주는 웹 앱)
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감
    - 링크를 공유할 시 첫 페이지만 공유 가능
  - 브라우저의 뒤로 가기 기능을 사용할 수 없음
  - 페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 됨

## Vue Router
- Vue 공식 라우터
  - SPA에서 페이지 이동 기능을 구현할 때 사용
  - 어떤 URL 경로에 어떤 컴포넌트를 보여줄지 정의만 하면 Vue Router가 연결
  - 핵심 컴포넌트
    - router-link: 페이지 새로고침하지 않는 링크
    - router-view: 현재 URL에 맞는 컴포넌트를 보여주는 링크
- index.js가 urls.py 느낌
  - 라우팅에 관련된 정보 및 설정이 작성 되는 곳
  - 각 주소로 접속했을 때, 어떤 Vue 컴포넌트(페이지 화면)를 보여줄 지 연결
  - path(주소): '/'
  - name(이름): 'home'
  - component(실행할 view함수 느낌): HomeView
- views
  - RouterView 위치(페이지 단위)에 렌더링 할 컴포넌트를 배치
  - 단순 분류의 의미로 구성
  - views: 큰 도화지
  - components: 도화지 안에 화면 구성 블록 조각들
- Routing 기본 동작 순서
  - index.js에 라우터 관련 설정 작성
  - RouterLink에 index에 정의한 주소 값 작성
  - RouterLink 클릭 시 경로와 일치하는 컴포넌트가 RouterView에서 렌더링
- Named Routers
  - 속성 값에 경로에 대한 이름을 지정
  - RouterLink에 v-bind를 사용해 'to' props 객체로 전달 가능
  - 하드 코딩된 URL을 사용하지 않아도 되며, 오타 방지 가능
    - RouterLink :to="{ name: 'home'}"

## Dynamic Route Matching
- URL의 일부를 변수로 사용하여 경로를 동적으로 매칭
  - 패턴은 같지만 ID 값만 다른 여러 URL을 하나의 라우트 설정으로 처리하는 기능
  - Django 에서는 <pk> 했지만 Vue에서는 :pk 해야 됨
  - Routerlink : params: {id: userId}
  - 컴포넌트(HTML): $route.params
  - 라우터: import {useRoute} from 'vue-router' 불러온 후 useRoute() 호출

## Nested Routes
- 중첩된 컴포넌트 구조에 맞춰 표현 가능
  - 일반적으로 '하위 경로에만 이름 지정'
- 부모 레이아웃은 유지한 채, 일부 영역만 다른 내용으로 교체하는 라우팅 방식
- components 폴더에 생성
- 자식 주소에 '/' 가 없으면 현 주소 뒤에 추가됨(있을 때 정상동작 안할 수 있음)

## Programmatic Navigation
- RouterLink 사용하는 대신(링크 클릭 대신), JavaScript 코드를 사용해 페이지 이동시키는 것
- router.push()와 같은 메서드 호출 -> 원하는 경로로 강제 이동 가능
- router의 인스턴스 메서드를 사용해 RouterLink로 <a> 태그를 만드는 것처럼 프로그래밍으로 네비게이션 관련 작업 수행 가능
- router 메서드
  - router.push()
    - 다른 위치로 이동 (이동 히스토리 마지막에 추가)
    - 뒤로 가기 버튼 클릭시 이전 URL로 이동 가능
  - router.replace()
    - 현재 위치 바꾸기 (이동 히스토리 마지막과 교체)
    - 뒤로 가기 시 이전 URL로 이동 불가
- route: 정보, (params.id)
- router: 행동 (push, replace)

## route 와 router
- route
  - router 객체
    - 현재 URL 상태를 보여주는 역할
      - route 객체 자체를 통해 페이지 이동(네비게이션)을 직접 제어 할 수는 없음
    - 읽기 전용, 현재 URL 라우트 정보 등을 담고 있음
      - 경로를 통해 현재 페이지 상태 확인 가능
    - 반응형, URL이 변경되면 route 객체도 자동으로 변경됨
      - route.params.id 참조중일 경우 URL이 바뀌어 id가 변경될 때 해당 값 자동으로 반영
  - useRoute()
    - 현재 활성화된 '경로 정보(route)'를 담은 route 객체를 반환
    - useRoute()는 컴포넌트의 setup 함수나 'script setup' 최상단에서만 호출해야 함
      - import {useRoute} from 'vue-router'

- router
  - useRouter()
    - 라우터 인스턴스 router 객체를 반환
    - useRouter는 페이지 이동 등 액션용, useRoute는 경로 정보 읽기용으로 역할이 다름
  - router 객체
    - 라우팅 로직(동작)을 제어할 수 있는 핵심 객체
    - 페이지 이동, 네비게이션 관련 메서드 제공
      - router.push('~'), router.replace('~') 등을 통해 프로그래밍적으로 라우트를 변경할 수 있음
    - 네비게이션 가드 등록, 히스토리 제어 같은 기능 사용 가능

## Navigation Guard
- Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 내비게이션을 보호
- 사용자의 로그인 상태나 권한을 확인하여, 내비게이션을 허용하거나, 취소하거나, 다른 페이지로 리다이렉트시킬 수 있음
- 주로 로그인하지 않은 사용자가 '마이페이지'에 접근하는 것을 막고 로그인 페이지로 보내는 등, 인증 기반의 라우팅 로직을 구현할 때 사용됨
- 종류
  - Globally(전역 가드)
    - 애플리케이션 전역에서 모든 라우트 전환에 적용되는 가드(모든 url)
  - Per-route(라우터 가드)
    - 특정 라우트에만 적용되는 가드(특정 url)
  - In-component(컴포넌트 가드)
    - 컴포넌트 내에서만 적용되는 가드

## Globally Guard
- 애플리케이션 전역에서 동작(**작성 위치: index.js**)
- Globally Guard 종류
  1. beforeEach() (로그인 유무에 따른 페이지 변환)
    - 콜백함수로 작성
    - 다른 URL로 이동하기 직전에 실행되는 함수(Global Before Guards)
    - 모든 가드의 콜백 함수는 2개의 인자를 받음
      - to: 이동 할 URL 정보가 담긴 Route 객체
      - from: 현재 URL 정보가 담긴 Route 객체
    - return false: 이동 불가
      - 현재 내비게이션 취소
    - return { name: 'About'}: About으로 보냄
      - 경로 위치를 전달하여 다른 위치로 redirect
      - return 없으면 자동으로 'to' URL Route 객체로 이동
  2. beforeResolve()
    - beforEach와 모든 컴포넌트 단위 가드가 실행된 후, 내비게이션이 확정되기 직전에 호출
    - 모든 비동기 컴포넌트가 로드되고, 모든 가드가 통과된 상태에서 **마지막으로 무언가를 확인하고 싶을 때** 사용
    - 주로 사용 예시
      - 페이지에 진입하기 전에, 사용자의 권한과 관련된 데이터를 미리 가져오는 등의 작업에 사용
    - 비교적 사용 빈도가 beforeEach보다 낮음
  3. afterEach()
    - 내비게이션이 완전히 확정된 후, 즉 URL이 변경되고 화면 렌더링이 끝난 뒤에 호출
    - 이미 이동이 완료된 상태이므로, 내비게이션을 중단시키거나 변경할 수 없음
    - 주로 사용 예시
      - 페이지 이동 기록을 로깅(logging)하거나, 이동한 페이지에 맞춰 문서의 제목(document.title)을 변경하는 등 **후처리 작업**에 적함

## Per-route Guard
- 작성위치 : **index.js의 각 routes**
- 특정 라우트(경로)에 진입할 때만 실행되도록 라우트 설정 객체에 직접 정의하는 가드
- 주로 beforeEnter 가드를 많이 사용
  - beforeEnter()
    - 특정 route에 진입했을 때만 실행되는 함수
    - 단순히 URL의 매개변수나 쿼리 값이 변경될 때는 실행되지 않고, **다른 URL에서 탐색해 올 때만 실행**됨
    - 활용 
      - 이미 로그인 한 상태라면 LoginView 진입을 막고 HomeView로 이동
      - 로그인 상태라면 HomeView로 이동, 로그인 상태가 아니라면 LoginView로 이동

## IN-component Guard
- 특정 컴포넌트 내에서만 동작하는 가드 (**작성위치: 각 컴포넌트의 script 내부**)
- In-component Guard 종류
  - onBeforeRouteLeave()
    - 현재 라우트에서 다른 라우트로 이동하기 전에 실행
    - 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리
      - 떠날 시 팝업 창 출력 등(떠나실 건가요?)
  - onBeforeRouteUpdate()
    - 이미 렌더링 된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전에 실행
    - 라우트 업데이트 시 추가적인 로직을 처리

## Lazy Loading Routes
- Vue 애플리케이션 첫 빌드 시 해당 컴포넌트를 로드하지 않고, '해당 경로를 **처음으로 방문할 때** 컴포넌트를 로드'하는 것
  - 빌드할 때 처음부터 모든 컴포넌트를 준비하면 컴포넌트의 크기에 따라 페이지 로드 시간이 길어질 수 있기 때문