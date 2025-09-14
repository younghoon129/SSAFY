# 생성하기
def create(request):
    article = ArticleForm(request.POST)
    if article.is_valid():
        article.save()
        return redirect('articles:detail', article.pk)
    context= {
        'article':article
    }
    return render(request, 'articles/new.html', context)



def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance = article)
    context = {
        'form':form,
        'article':article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article':article,
        'form':form,
    }
    return render(request, 'articles ')



def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form,
        'article':article
    }    
    return render(context, 'articles/update.html', context)