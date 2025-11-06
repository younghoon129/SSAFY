# Many to one relationships

- Many to one relationships
    - N:1 or 1:N
    - 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계

- on_delete 속성 종류
    - CASCADE
        게시글이 삭제되면 해당 게시글 모든 댓글 삭제
    - PROTECT
        - 댓글 존재하면 게시글 삭제 불가
    - SET_NULL
        - 부모 객체 삭제되면, 해당 필드 값이 NULL로 저장

- comment.article_id = book.pk -> 잘못된 정보지만 에러 발생 안함
    - comment.article_id = article.pk -> 이게 맞는 거
    - comment.article = article 이렇게 하는 게 나음

- 역참조
    - article.comment_set.all()
        - 모델 인스턴스.역참조 이름+_set(related manager).QuerySet API
    - 참조하는 것을 거꾸로 찾는 것
    - related manager (역참조 이름)
        - 역참조 시에 사용하는 매니저
        - 모델 클래스명 + _set이 기본
        - 특정 댓글의 게시글 참조 (Comment -> Article)
            - comment.article
        - 특정 게시글의 댓글 목록 역참조(Article -> Comment)
            - article.comment_set.all()

- def comments_create(request, pk):
    article = Article.objects.get(pk=pk)

    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        # commit=False 는 DB에 저장 요청을 잠시 보류하고,
        # 대신 comment 인스턴스는 반환 해줌
        comment = comment_form.save(commit=False)
        # 외래 키 데이터를 할당
        comment.article = article
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)