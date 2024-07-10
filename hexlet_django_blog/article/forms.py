from django import forms
from hexlet_django_blog.article.models import Article, ArticleComment


class ArticleForm(forms.ModelForm):
    name = forms.CharField(max_length=15, required=True)
    body = forms.CharField(max_length=100, required=True, widget=forms.Textarea)

    class Meta:
        model = Article
        fields = ['name', 'body']


class ArticleCommentForm(forms.ModelForm):

    class Meta:
        model = ArticleComment
        fields = ['content']
