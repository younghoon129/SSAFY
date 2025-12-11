# MCP
- 어플리케이션이 LLM(Model)에게 문맥(Context)를 제공하는 방법을 표준화한 프로토콜(Protocol)


- MCP Server
  - 사용자의 입력을 분석해서, 필요한 서비스(MCP Server)에 연결
    - MCP 라는 표준 규격으로 만들어서 제공
    - Open API를 만드는 느낌

- MCP hosts
  - 사용자의 의도를 파악하고, 어떤 App의 Mcp Server를 호출

- MCP Client
  - MCP hosts 한 후 JSON 형태(MCP)로 바꿈

- uv
  - 엄청나게 빠름
  - 프로젝트 생성, 라이브러리 설치, 가상환경 관리 엄청 빠름

## AI Agent
- 지금까지 만든 Tool만 있는 MCP Serever는 팔다리만 있는 기계와 같음
- 내부에 저장한 데이터와 프롬프트가 결합되면서 스스로 생각하고 행동하게 됨
- AI Agent는 아래의 사이클을 갖춤 (ReAct 패턴, Reasoning + Acting)
  - 계획 -> 행동 -> 관찰
- 데이터 저장소 생성
  - AI 가 가져온 정보를 잠시 보관할 저장소 생성
  - 저장소 필요한 이유
    - AI 가 긁어온 뉴스를 채팅창에 건네주면(컨텍스트 주입), 토큰이 낭비됨
    - 내부 저장소를 활용하면 컨텍스트 주입을 할 필요 없이, 내부 데이터를 활용하여 이전 맥락을 이해할 수 있음
- 나만의 LLM을 기반으로 돌아가는 AI Agent를 만들기
  - LLM을 다루는 프레임워크인 LangChain 1.0
  - 