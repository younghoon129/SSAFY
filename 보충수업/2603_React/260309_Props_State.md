# Props, State
- 컴포넌트에서 사용되는, 값이 유지되는 데이터

- import / export
  - es6에서 모듈을 내보내고 불러오는 방법
- 컴포넌트 생성 시 컴포넌트 이름이 Pascalcase 아닐 경우 에러 발생

## Props
- 부모 컴포넌트에서 자식 컴포넌트로 내려주는 데이터
- 컴포넌트 태그로 감싼 값이 props.children으로 전달됨
- 활용 팁
  - 구조 분해 할당 구문을 잘 활용할 것
  - 특정 props에 기본 값을 줄 수 있다
    - defaultProps(요즘 잘 안쓰임), 구조 분해 할당의 기본값
  - props는 읽기 전용

## State
- 컴포넌트에서 사용되는, 값이 유지되는 데이터

## 클래스형 컴포넌트 vs 함수형 컴포넌트
- 클래스형 컴포넌트는 이제 안쓰임
- useState(Hooks)는 React v16.8 부터 등장
  - 즉, 그 전에는 함수형 컴포넌트는 state를 가질 수 없었고, 클래스형 컴포넌트만 state를 가질 수 있었음
- 함수형 컴포넌트 사용하는 이유
  - 클래스형 컴포넌트는
    - 상태 로직의 재사용 어려움
    - 코드가 이해하기 어려움(복잡함)
    - JS Class의 독특한 this 바인딩

## Hook
- Hook은 함수 컴포넌트에서 state와 lifecycle 기능을 사용할 수 있게 도와주는 함수

## React Lifecycle
- 렌더링 과정
  - Class는 더 이상 사용하지 않음
  - Function