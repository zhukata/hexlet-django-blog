from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

def index(request, tags, article_id):
    return HttpResponse(f"Cтрока номер {article_id}. Тег {tags}")
