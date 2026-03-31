# 가비지컬렉션(GC)
- 프로그램에서 더 이상 사용되지 않는 메모리를 자동으로 해제하는 메커니즘
- 참조되지 않는 객체를 찾아 자동으로 제거

## 힙 구조와 GC
- Hotspot Heap Structure
    - young generation
        - eden, s0, s1
    - old generation
        - tenured
    - metaspace
        - metaspace
    
- 과정 1
    - survivor 두 영역 중 하나는 반드시 비어있는 상태
    - 만약 두 영역에 모두 데이터가 존재하거나, 사용량이 0이라면 정상적인 상황이 아님
- 과정 2
    - Major GC는 속도가 매우 느리고, 발생하는 순간, 어플리케이션이 멈춰 성능과 안정성에 아주 큰 영향을 미침
    - STW
        - 가비지 컬렉션이 동작하는 동안에는 다른 동작을 멈추기 때문에 오버헤드가 발생
        - GC가 작동하는 동안 GC 관련 Thread를 제외한 모든 Threaad는 멈추게 되어 서비스 이용에 차질이 생김
