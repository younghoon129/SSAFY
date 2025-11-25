# 비동기 JS with Django
- 실습

## Ajax 복습
- 동기: 프로그램을 순차적으로 실행
- 비동기: 기다리지 않고, 다른 작업을 실행
- JS => 싱글 스레드 => 어떻게 비동기를 처리할까요?
    - Call Stack: 함수 호출이 쌓이고, 코드가 동작하는 영역
    - Web API: 비동기 작업이 처리되는 곳 (브라우저가 담당)
    - Task Queue: 처리가 끝난 작업들이 대기하는 곳
    - Event Loop: Call Stack 비어있는 지를 확인하고, 비어있으면 Task Queue에 있는 작업을 옮겨서 마무리한다.
- Ajax: 비동기 통신 기술
- axios: Promise 기반의 HTTP 요청을 처리하는 JS 라이브러리
- 비동기 함수를 동기적으로 처리하고 싶을 때
    - 비동기 콜백 => 콜백 지옥
    - Promise 객체 => 비동기 작업 결과를 반환(then, catch)
    - async / await 를 이용해서 더욱 간결하게 사용이 가능하다.