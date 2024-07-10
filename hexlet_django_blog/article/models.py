from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=15) # название статьи
    body = models.TextField() # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class ArticleComment(models.Model):
    content = models.CharField('content', max_length=100)
