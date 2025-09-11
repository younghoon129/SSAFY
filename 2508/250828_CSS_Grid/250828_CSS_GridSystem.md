# Bootstrap Grid System

- 레이아웃 조정하는데 12개(약수가 많음)의 컬럼으로 구성된 시스템
    * 반응형 디자인을 지원
- 반응형 웹 디자인
    * 일관된 디자인

- nesting
    * 컬럼 중첩

- 상쇄(offset)
    * 
- gutters
    * 가로는 padding
    * 세로는 margin
        * 행이 컨트롤 row
        * grid card는 열이 컨트롤 column
    * 이유
        * 가로는 12칸으로 제한 돼있어서 padding으로 컨텐츠를 줄여 제한된 크기를 넘지 않음 margin은 넘으려하기 때문에 안됨
        * 세로는 굳이 컨텐츠를 안줄이고 margin으로 얼마든지 넘겨도 됨
- Responsive Web Design
    * 12개의 column과 6개의 breakpoints를 사용하여 반응형 웹 디자인 구현
    * 사이즈는 항상 본인 이상 그래서 건너뛰어도 됨
    * offset도 이상으로 표현되기 때문에 offset-(사이즈)-0 으로 초기화 해줘야됨



- CSS Layout 총 정리
    * 서로 상호 보완적인 시스템
    * position
        * absolute, fixed
    
    * flex
        * 이미지 세워서(주 축을 column으로) 위에서부터 그림,글 순서 한거 같음
    * grid system
        * 화면크기에 따라 줄어들고 늘어나고
        * 12개 나눠서 하는거

- UX, UI
    * 
    * UX
        * 사람들의 마음과 생각을 이해하고 정리해서 제품에 녹여내는 과정
        * 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계
    * UI
        * 서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소
        * 리모콘, ATM, 웹 사이트
        * 예쁜 디자인 보다는 사용자가 더 쉽고 편리하게 사용할 수 있도록 고려

- 기업별 UI
    * 

- cantunsee.space
    * 더 나은 UI/UX를 고민해볼 수 있는 게임