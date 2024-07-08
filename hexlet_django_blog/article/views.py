from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.views import View

class IndexView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))

def index(request, tags, article_id):
    return HttpResponse(f"Cтрока номер {article_id}. Тег {tags}")
