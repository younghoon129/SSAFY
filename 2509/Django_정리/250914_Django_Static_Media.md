# Static files
- 서버측에서 변경되지 않고 고정적으로 제공되는 파일
- 자원에 접근 가능한 주소가 있고 제공하기 위해 경로 있어야됨
- {% load static%}
- STATIC_URL = 'static/' -> 보여주기용 경로
- STATICFILES_DIRS = [
    BASE_DIR = 'static'
    ]
- BASE_DIR = 최상위


## MEDIA
- pip install pillow
- MEDIA_URL = 'media/'
- MEDIA_ROOT = BASE_DIR / 'media'
- + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
- enctype = 'multipart/form-data'
    * 데이터 전송방식 결정