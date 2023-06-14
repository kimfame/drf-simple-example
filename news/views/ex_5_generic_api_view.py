from rest_framework import generics

from ..models import Article
from ..serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
