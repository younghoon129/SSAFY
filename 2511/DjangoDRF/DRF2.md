# DRF2
- raise_exception
    - is_valid 를 통과 못했을 때 리스폰 안해도 됨
- commit=False
    - .save() 할 때 모델폼에서는 commit False 이지만
    - 모델시리얼라이저를 통해 필드를 알고 있기 때문에 
    - serializer 에선 article(외래키 필드) = article 이렇게 작성해도 됨
    - 유효성 검사하고 외래키 확인 하기 때문에(순서가 잘못됨) 정상 작동 안함
        1. 외래키 데이터를 유효성 검사에서 제거
        2. 최종 제공 데이터에는 포함 시킴
        3. -> 읽기 전용 필드 필요 (read only)
        4. Serializer.py 에서 정의할때 read_only_fields = ('article',) 해야됨
- 댓글 출력할 때 게시글 번호(article) 이 아니라 제목(title)을 보여주고 싶음.
    - 재정의(덮어쓰기) 해야 되는데 재정의 할 경우 "read_only_fields = ('article',)" 적용 안됨
    - 제목(title)만 보여주는 시리얼라이저를 만듦(ArticleTitleSerializer, 필드에 title만 있음)
    - article = ArticleTitleSerializer(read_only=True)
    - 몇번 게시글인지도 보여주고 싶으면 필드에 id만 추가하면 됨
- 단일 게시글의 댓글 목록
    - comment_set = 시리얼라이저 하고 many=True, read_only=True 해야됨
- 단일 게시글의 댓글 갯수
    - from django.db.models import count
    - SerializerMethodField()
    - article = Article.objects.annotate(num_of_comments = Count('comment')).get(pk=article_pk)
- API(문서화) drf-spectacular
    - pip install drf-spectacular
    - 프로젝트에 앱 등록해야됨
- shortcuts
    - from django.shortcuts import get_object_or_404(get)
    - from django.shortcuts import get_list_or_404(filter)
    - 해당 객체 없을 때 500(에러) 이 아니라 404 출력
    - Article.objects.get(pk=article_pk) -> get_object_or_404(Article, pk=aritcle_pk)