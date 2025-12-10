# DRF with Vue


## CORS Policy
- 웹 서버가 리소스에 대한 서로 다른 출처 간 접근을 허용하도록 선택할 수 있는 기능 제공
- 웹 브라우저의 동일 출처 정책과 보안
  - 기본적으로 웹 브라우저는 같은 출처에서만 요청하는 것을 허용
  - 다른 출처로의 요청은 보안상의 이유로 차단
  - 이는 SOP(동일 출처 정책)에 의해 다른 출처의 리소스와 상호작용 하는 것이 기본적으로 제한 됨
  - 서버에서 설정, 브라우저가 해당 정책을 확인하여 요청 허용되는지 여부 결정

- SOP(Same-origin policy)
  - 동일 출처 정책(브라우저 정책)

  - 같은 출처에서만 리소스를 자유롭게 공유할 수 있다
    - 어떤 출처(Origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호 작용하는 것을 제한하는 보안 방식
  - 웹 도메인이 다른 도메인의 리소스에 접근하는 것을 제어하여 사용자의 개인 정보 및 데이터의 보안을 보호, 잠재적인 보안 위협 방지
  - 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임

- Origin
  - URL의 Protocol, Host, Port를 모두 포함하여 '출처'라고 함
  - Same Origin 예시
    - http(Protocol)://localhost(Host):3000(Port)/posts(Path)/3(Path)

- CORS(Cross-Origin Resource Sharing)
  - 교차 출처 리소스 공유
  - 서버가 발급하는 '허가증' 
  
- 다른 출처의 리소스를 불러오려면 올바른 **CORS header를 포함한 응답을 반환**해야 됨

- 적용방법
  - 서버에서 CORS Header를 만들어야 됨
  - settings.py에서 MIDDLEWARE 설정
    - comon 미들웨어보다 위에 있어야됨
    - Whitenoise's 미들웨어보다 위에 있어야됨 (배포 단계)
  - Configuration
    - CORS_ALLOWED
      - ORIGINS(리스트로 관리)
      - REGEXES(정규표현식)
      - ALL_ORIGINS(모두 허용 - T, F)
      - CORS_ALLOWED_ORIGINS = [
            'http://127.0.0.1:5173',
            'http://localhost:5173',
        ]
  - 서버(도메인 B)
    - HTTP Header에 도메인A 가 포함되면 접근 가능
  - 브라우저(도메인 A)
    - 서버에 등록됐기 때문에 안전하게 데이터 사용 가능