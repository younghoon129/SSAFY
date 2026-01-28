# Spark 기본 구조와 세팅
- Spark 개요 및 실행 구조
- Spark 설치 및 환경설정

## Spark 개요 및 실행 구조
- 데이터 처리의 필요성 증가
    - 배치 처리
    - 스트림 처리
- 기존 데이터 처리 방식의 한계점
    - 단일 서버의 확장성 부족
        - 기존 데이터 처리는 주로 단일 서버로 이루어짐
        - 데이터가 증가하면 서버 성능을 높이는 방식(수직 확장, Scale-Up)을 사용
        - 그러나 단일 서버는 하드웨어의 물리적 한계로 인해 무한정 성능을 높일 수 없음
        - Scale up: 서버 크기 자체를 키우는 것
        - Scale Out: 서버 수평 확장(서버 갯수 늘리기)
    - 디스크 기반 처리로 인한 속도 문제
        - Spark 이전의 기술은 데이터를 처리할 때 **디스크 기반의 저장장치**를 사용
        - 디스크는 메모리(RAM)보다 데이터 읽기/쓰기 속도가 현저히 느리기 때문에 데이터 처리 과정에서 속도 저하 현상이 발생

- Spark 탄생 배경 설계 목적
    - 기존 Hadoop MapReduce는 느린 속도와 반복 작업의 비효율성이라는 구조적 한계 존재
    - 특히 머신러닝, 스트리밍 분석처럼 반복적이고 실시간성이 요구되는 작업에 부적합
    - Spark는 UC Berkeley AMP Lab에서 이러한 문제를 해결하고자 개발됨
    - 2009년 개발 시작 -> 2010년 오픈소스 공개 -> 2014년 Apache 프로젝트로 채택

- Hadoop ecosystem
    - 하둡의 코어 프로젝트는 HDFS, MapReduce, YARN이지만 이들의 역할을 수행해내는 다양한 서브 프로젝트들로 구성된 환경
    - 분석과 처리를 Spark로 활용하는 경우 증가

### Spark가 기존 기술의 한계를 극복한 방법
- Spark가 기존 기술의 한계를 어떻게 극복했는지?
    - 기존 시스템의 단점들을 보완해, 빠르고 통합적인 분석 환경을 제공
    - Hadoop
        - 문제점: 느림 처리속도, 반복 작업 비효율
        - Spark의 접근 방식: 메모리 기반 연산(In-memory)
    - RDBMS
        - 문제점: 확장성 부족, 비정형 데이터 처리 어려움
        - Spark의 접근 방식: 분산 클러스터 기반, 유연한 스키마
    - 특화 시스템
        - 기능 분산, 통합 어려움
        - Spark의 접근 방식: 하나의 플랫폼에서 배치 + 실시간 + ML
    - 디스크 기반 처리
        - 문제점: 입출력 병목
        - Spark의 접근 방식: DAG(방향성 있고 순환하지 않는 그래프) 기반 최적화 실행, Lazy 평가

- Spark 사용 이유
    - 반복 연산에서 Hadoop MapReduce보다 빠른 처리 성능
    - 메모리 기반의 데이터 처리로 빠른 속도
    - Hadoop과의 유연한 연동성
    - RDD의 계보(lineage)를 기반으로 장애 발생 시 연산을 자동으로 재실행하여 복구

- Spark 설계 철학
    - 속도
        - 메모리 기반 연산(In-Memory Computation)으로 디스크 I/O 최소화
        - DAG 기반 스케줄링으로 병렬 처리 최적화(방향성, 비순환 그래프, 실행 계획 세움)
        - Tungsten 엔진을 통한 코드 생성 최적화
    - 사용 편리성
        - 단일 PC와 클러스터 간 코드 차이가 최소화된 추상화 구조
        - RDD(데이터 처리하는 최소한의 단위) -> DataFrame -> Dataset(JVM기반 언어에서만 지원)의 계층적 API 제공
        - Scala, Python, Java, R 등 다중 언어 지원
    - 모듈성
        - SparkSQL, Streaming, MLlib, GraphX 등 다양한 워크로드를 하나의 엔진(목적이 다른 라이브러리)에서 처리
        - 별도의 시스템(Hive, Storm, Mahout 등) 통합 불필요
    - 확장성
        - 다양한 데이터 소스(HDFS, Cassandra, MongoDB, RDBMS, S3 등) 연동
        - 여러 파일 포맷(csv, parquet 등) 지원
        - 수많은 서드파티 패키지와 통합 가능

- Spark의 주요 컴포넌트
    - 모든 컴포넌트는 Spark Core 위에서 실행됨, 공통된 실행 엔진 및 스케줄러 공유
    - Spark Core
        - 핵심 실행 플랫폼
    - Spark SQL
        - 구조적 데이터 처리 및 SQL 기반 쿼리 실행
    - Spark Streaming
        - 실시간 데이터 분석을 위한 스트리밍 처리(마이크로 배치 방식)
    - MLlib
        - 머신러닝 알고리즘 라이브러리 (분류, 회귀, 군집 등)
    - GraphX
        - 그래프 기반 데이터 처리와 분석 지원(PageRank 등)
    
- Spark 활용 시 주의점
    - 엄밀한 실시간 처리 불가 (Micro-batch 기반)
        - 짧은 주기 데이터 묶어서 처리
    - 작은 데이터 파일 처리의 비효율성
        - 대규모 병렬 처리를 위해 설계 되어 있기 때문
    - 자체 파일 관리 시스템 부재(HDFS, S3 등 사용)
        - 분석 처리에 집중된 프레임워크이기 때문
        - Spark 만으론 데이터 저장소 대체하기 어려움
    - 높은 메모리 비용
        - 빠른 만큼 메모리 많이 사용함
    
### Spark의 실행구조
- 애플리케이션 구성 요소
    - 클러스터 매니저
    - 드라이버
    - 실행기
    - 스파크 세션
    - 잡
    - 스테이지
    - 태스크

- 클러스터 매니저
    - 애플리케이션의 리소스 관리
        - 드라이버가 요청한 실행기 프로세스 시작
        - 실해 중인 프로세스를 중지하거나 재시작
        - 실행자 프로세스가 사용할 수 있는 최대 CPU 코어 개수 제한 등
    - 종류
        - Standalone
        - Hadoop Yarn
        - Kubernetes
- 드라이버
    - 스파크 애플리케이션의 실행을 관장하고 모니터링
        - 클러스터 매니저에 메모리 및 CPU 리소스를 요청
        - 애플리케이션 로직을 스테이지와 태스크로 분할
        - 여러 실행자에 태스크를 전달
        - 태스크 실행 결과 수집
        - 1개의 스파크 애플리케이션에는 1개의 드라이버만 존재
        - 드라이버 프로세스가 어디에 있는지에 따라, 스파크에는 크게 두 가지 모드가 존재
            - 클러스터 모드 - 드라이버가 클러스터 내의 특정 노드에 존재
            - 클라이언트 모드 - 드라이버가 클러스터 외부에 존재
- 실행기
    - 드라이버로부터 전달받은 태스크를 실행하는 프로세스
    - 스파크 드라이버가 요청한 태스크들을 받아서 실행하고, 그 결과를 드라이버로 반환
    - 각 프로세스는 드라이버가 요청한 태스크들을 여러 태스크 슬롯 (스레드)에서 병렬로 실행
    - JVM 프로세스
- 스파크 세션
    - 스파크 기능을 사용하기 위한 진입점
        - Spark Core 기능들과 상호 작용할 수 있는 진입점 제공
        - API로 프로그래밍을 할 수 있게 해주는 객체
        - spark-shell에서 기본적으로 제공
        - 스파크 애플리케이션에서는 사용자가 SparkSession 객체를 생성해 사용해야 함
- 잡
    - 사용자가 실행한 액션(collect(), count()등)에 의해 생성되는 작업 단위
        - 스파크 액션(save(), collect() 등)에 대한 응답으로 생성되는 여러 태스크로 이루어진 병렬 연산
- 스테이지
    - 잡을 셔플(데이터 이동, 데이터 합칠 때?) 기준으로 나눈 실행 단위
        - 스파크 각 잡은 스테이지라 불리는 서로 의존성을 가지는 다수의 태스크 모음으로 나뉨
- 태스크
    - 스테이지를 구성하는 실제 실행 단위
        - 스파크 각 잡별 실행기로 보내지는 작업 할당의 가장 기본적인 단위
        - 개별 task slot에 할당 되고, 데이터의 개별 파티션을 가지고 작업
- 스파크 연산의 종류
    - 트랜스포메이션
        - 실행되지 않다가(DAG, 실행계획을 세운거)
    - 액션
        - 잡, 스테이지, 태크스 과정 거치며 실행

- Transformation
    - immutable(불변)인 원본 데이터를 수정하지 않고, 하나의 RDD나 Dataframe을 새로운 RDD나 Dataframe으로 변형
    - (input, output) 타입: (RDD, RDD), (DataFrame, DataFrame)인 연산
        - map(), filter(), flatMap(), select(), groupby(), orderby() 등
    - Narrow, Wide Transformation 존재

- Narrow Transformation
    - Narrow transformation
        - input: 1개의 파티션
        - output: 1개의 파티션
        - 파티션 간의 데이터 교환이 발생하지 않음
        - ex) filter(), map(), coalesce()
    
- Wide transformation
    - Wide transformation
        - 연산 시 파티션끼리 데이터 교환 발생
        - ex) groupby(), orderby(), sortByKey(), reduceByKey()
        - 단, join의 경우 두 부모 RDD/Dataframe이 어떻게 파티셔닝 되어 있냐에 따라 narrow일 수도 wide일 수도 있음
    
- Action
    - immutable(불변)인 인풋에 대해, Side effect(부수 효과)를 포함하고, 아웃풋이 RDD 혹은 Dataframe이 아닌 연산
    - count() -> 아웃풋: int
    - collect() -> 아웃풋: array
    - save() -> 아웃풋: void

- Lazy evaluation
    - 모든 transformation은 즉시 계산되지 않음
    - 계보(lineage)라 불리는 형태로 기록
    - transformation이 실제 계산되는 시점은 action이 실행되는 시점
    - action이 실행될 때, 그 전까지 기록된 모든 transformation들의 지연 연산이 수행됨
    - 장점
        - 스파크가 연산 쿼리를 분석하고, 어디를 최적화할지 파악하여, 실행 계획 최적화가 가능
            - eager evaluation(즉시 평가)이라면, 즉시 연산이 수행되기 때문에 최적화 여지가 없음
        - 장애에 대한 데이터 내구성을 제공
        - 장애 발생 시, 스파크는 기록된 lineage를 재실행 하는 것만으로 원래 상태를 재생성할 수 있음

## Spark 설치 및 실행 환경설정
- Pyspark 실행
    - Python 코드(PySpark API) -> Py4J
    - JVM: SparkSession / SparkContext(Driver) ->
    - Cluster Manager -> Executors ->
    - 분산 데이터 처리
