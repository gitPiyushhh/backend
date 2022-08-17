from django.shortcuts import render

from .models import Article


########################################
#### Custom views

# Create your views here.
def article_detail_view(request, id = None):
    art_obj = None

    if id is not None: art_obj = Article.objects.get(id=id)

    context = {
        'object': art_obj,
    }

    return render(request, 'articles/detail.html', context=context)