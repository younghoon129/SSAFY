# TIL

- python 이용 클래스와 객체 지향 프로그래밍
- panda를 활용한 데이터 분석 및 가공
- 조건문, 반복문, 그룹 연산 등 데이터 처리 로직 구현
- pandas의 groupby, pivot, melt 등을 활용해 데이터를 변환
- groupby: 특정 기준에 따라 데이터를 그룹화하여 집계하는 pandas 기능
- melt: wide-format 데이터를 long-format으로 변환하는 데이터 정리 기법
  - wide-format(넓은 형식)
    - 여러 개의 측정값/변수가 각각 열로 표현
    - 읽기는 편하나, groupby나 시각화에 비효율적
  - long-format(길게 늘어진 형식)
    - 측정 항목을 하나의 열(item)에 모으고, 값은 별도 열(amount)로 표현
    - groupby, pivot, 시각화 등에 유용