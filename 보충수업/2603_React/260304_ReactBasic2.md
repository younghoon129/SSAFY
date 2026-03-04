# 딱 필요한 만큼의 TypeScript 기초
- Typescript 특징
  - 대규모 프로젝트에서 JS의 불편함을 극복하기 위해 출시
  - JavaScript의 상위 집합
  - 최종적으로는 순수 JavaScript로 컴파일되어 실행됨
  - 정적 타입 검사
  - 풍부한 IDE 지원(자동완성, 타입 추론, 오류 표시)

- as const
  - 타입을 더 정확하고, 좁게 생성

- any는 웬만하면 지양

## React란?
- 사용자 인터페이스를 만들기 위한 JavaScript 라이브러리(SPA 라이브러리)
- 장점
  - 트렌드
    - 많이 쓰임
    - 생태계가 굉장히 큼
    - 수요 많음
  - 편함
    - 화면을 여러 단위로 쪼개고, 재사용하는 식으로 코드 관리가 용이함
    - 기본적인 틀이 있고 유용한 라이브러리들이 많음
- 특징
  - 컴포넌트 기반 설계
    - 스스로 상태를 관리하는 캡슐화된 코드 조각
    - 의미단위로 컴포넌트를 구성하여 사용
    - 코드의 재사용성과 유지보수성 증가
    - 컴포넌트는 부모, 자식 관계를 갖음
  - Virtual DOM
    - 데이터만 그대로 복사해서 가상에서 데이터 변화를 반영(빠름)하고 최종적으로 DOM에 반영(이때만 느림)
    - 실제 DOM의 복사본으로 SPA에서의 동적인 변화를 효율적으로 관리하기 위해 사용됨
  - CSR
    - Client Side Rendering, Single Page Application
    - Server Side Rendering, Multi Page Application
  - 풍부한 생태계

- React Component
  - 스스로 상태를 관리하는 캡슐화된 코드 조각
  - 하나의 JSX 값을 반환하는 함수 (또는 클래스)
  - 컴포넌트를 통해 화면 구성
  - 컴포넌트를 잘 나눠야 좋은 React 코드가 됨

- Component vs JSX
  - 컴포넌트는 JSX를 생성하는 함수
  - 컴포넌트는 기본적으로 함수이기 때문에 자신만의 고유한 로직이 들어갈 수 있다
  - 스스로 상태를 가질 수 있다(상태가 변하면 알아서 반영된다.)

- import / export
  - es6에서 모듈을 내보내고 불러오는 방법
  - named export 확인 해보면 좋음

- 컴포넌트 생성 시, 주의사항
  - 컴포넌트 이름은 PascalCase
  - 의미단위로 쪼개서 파일을 분리
  - 최상위 컴포넌트 이름은 일반적으로 App
    - index.js : entry point, 최종 컴포넌트를 DOM에 render(ReactDOM.render)
    - App.js: 모든 컴포넌트들의 root 컴포넌트, 이걸 기준으로 하위에 트리구조로 생성