# Airflow 기본 구조와 세팅
- 워크플로우 오케스트레이션
- Airflow 개요 및 아키텍처
- Airflow 주요 컴포넌트
- DAG 실행
- Airflow DAG 기본 구조

## 워크플로우 오케스트레이션이란?
- 작업(Task)을 정해진 순서에 따라 실행하고 자동화하는 기술
- 데이터 파이프라인, 머신러닝, CI/CD 등 다양한 분야에서 활용
    - 작업 자동화 -> 반복적인 수작업 제거
    - 의존성 관리 -> 특정 작업이 완료된 후 다른 작업 실행 가능
    - 실패 처리 및 모니터링 -> 장애 발생 시 재시도 및 알림 제공
    - 스케줄링 기능 -> 특정 시간 또는 이벤트 기반 실행 가능

- Apache Airflow란?
    - Python를 기반의 데이터 파이프라인 자동화 및 스케줄링 도구
    - 배치 프로세스를 효율적으로 관리하는 워크플로우 오케스트레이션 도구
    - 다양한 시스템 및 데이터베이스와 통합 가능(ETL, MLOps, 클라우드 등)

- Apche Airflow 역할
    - 데이터 파이프라인 자동화
    - DAG(Directed Acyclic Graph)로 작업 정의
    - 실행 및 장애 관리, 모니터링 기능 제공

- Apche Airflow의 주요 활용 사례
    - Business Operations - 기업의 핵심 비즈니스 데이터 애플리케이션 자동화
    - ETL/ELT - 데이터 파이프라인 구축 및 관리
    - Infrastructure Management - 인프라 자동 배포 및 관리
    - MLOps - 머신러닝 모델 개발 및 운영 자동화

    - Business Operations
        - Airflow를 활용한 기업 비즈니스 운영 자동화
            - 데이터 중심 애플리케이션 및 업무 자동화
            - 정기적인 리포트 생성 및 배포
            - 고객 데이터 파이프라인 및 CRM 연동
    - ETL / ELT
        - Airflow를 활용한 데이터 파이프라인 구축 및 관리
            - 데이터 수집(Extract), 변환(Transform), 적재(Load) 자동화
            - 여러 데이터 소스를 통합하여 분석 가능
            - Data Warehouse(BigQuery, Snowflake 등)와 연계하여 최적화
    - Infrastructure Management
        - Airflow를 활용한 인프라 배포 및 운영 자동화
            - 클라우드 리소스 자동 프로비저닝Airflow를 활용한 인프라 배포 및 운영 자동화
            - (AWS, GCP, Azure 등)
            - CI/CD 파이프라인 자동 실행
            - Kubernetes 및 서버 배포 자동화
    - MLOps
        - Airflow를 활용한 머신러닝 파이프라인 자동화
            - 데이터 수집 -> 모델 학습 -> 평가 -> 배포 과정 자동화
            - 머신러닝 워크플로우 오케스트레이션
            - 모델 재학습 및 모니터링 자동화

- Airflow 사용하는 이유
    - 기존 방식의 한계(Cron Job, Bash Script)
        - 작업 간 의존성 관리 어려움
        - 장애 발생 시 원인 추적 및 복구 어려움
        - 로그 관리 및 모니터링 부족
    - Airflow 도입 시 장점
        - DAG 기반 의존성 관리 -> Task 실행 순서 설정 가능
        - WEB UI 제공 -> 직관적인 모니터링 가능
        - 재시도 및 알림 기능 -> 장애 발생 시 자동 대응
        - 확장성 및 유연성 -> 다양한 실행 환경 지원

## Airflow 개요 및 아키텍처
- Airflow의 장점
    - Python 기반 -> 개발자가 쉽게 접근 가능
    - 강력한 UI 제공 -> 직관적인 모니터링 가능
    - 태스크 간 의존성 관리 용이 -> DAG 구조 활용
    - 확장성 높음 -> 다양한 Executor 지원
    - 장애 복구 기능 제공 -> 재시도 및 알림 설정 가능

- Airflow의 단점
    - 초기 설정 및 학습 곡선이 가파름
        - 다양한 컴포넌트가 많이 있어서 설정 까다로울 수 있음
    - 실시간 데이터 처리에는 적합하지 않음
    - 복잡한 DAG의 경우 성능 튜닝 필요

- Airflow 설치
    - docker-compose.yaml 설치
        - $ curl-LfO 2.10.5
    - Airflow User 세팅
        - echo -e 'AIRFLOW_UID=$(id-u)' > .env
    - docker airflow 설치
        - $ docker compose up airflow-init
    - Airflow 실행
        - docker compose up
    
