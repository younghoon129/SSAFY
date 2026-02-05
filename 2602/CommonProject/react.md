# React
- useState
- useEffect
- api

## useState
- useState(상태)
    - 컴포넌트의 기억력
    - 컴포넌트 내부에서 변할 수 있는 데이터를 의미
    - 값이 변하면 리액트가 감지 후 화면을 자동으로 다시 그려줌(Re-render)
    - Hook: useState
    - 특징  
        - 변수처럼 직접 값을 수정해선 안됨, 반드시 **전용 수정 함수(Setter)를 사용해야 됨**
    - 예시
        - const [count, setCount] = useState(0); // [현재값, 수정함수]
    - 참고자료
        - https://ko.react.dev/learn/state-a-components-memory

## Effect
- Effect(렌더링 외의 작업)
    - 리액트 컴포넌트가 화면에 나타난 후(Mount), 사라질 때(Unmount), 혹은 특정 값이 바뀔 때 실행되는 **부수 효과(Side Effect)**를 말함
    - Hook: useEffect
    - 핵심
        - 의존성 배열
        - useEffect(fn, [])
            - 화면에 처음 나타날 때 딱 한번만 실행(API 호출에 주로 사용)
        - useEffect(fn, [data])
            - data 값이 바뀔 때마다 실행
    - 예시
        - 타이머 시작, 이벤트 리스너 등록, API 호출 등
    - 참고자료
        - [Effect와 동기화하기](https://ko.react.dev/learn/synchronizing-with-effects)

## API
- fetch나 axios 라이브러리를 사용해 데이터를 가져옴
- 흐름
    - 비어있는 State 생성
    - useEffect 안에서 API를 호출
    - 받아온 데이터를 setData로 State에 삽입
    - 화면 자동 반영