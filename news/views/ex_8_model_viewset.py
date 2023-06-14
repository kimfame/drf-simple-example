from rest_framework import viewsets

from ..models import Article
from ..serializers import ArticleSerializer


class ArticleModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    http_method_names = ["get", "post", "put", "delete"]
