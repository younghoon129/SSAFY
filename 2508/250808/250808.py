#필요한 모듈 임포트
import os
from dotenv import load_dotenv
import requests

import requests

# .env 파일 로드
load_dotenv()

#환경 변수 접근
TTBKEY = os.getenv('TTBKEY')
#알라딘 API 요청 예제
URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
# 필요한 파라미터 전달을 위한 Dictionary
params = {
    'ttbkey' : TTBKEY,
    'Querry' : '파울로 코엘료',
    'Query'
}