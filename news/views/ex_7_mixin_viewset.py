from rest_framework import mixins, viewsets

from ..models import Article
from ..serializers import ArticleSerializer


class ArticleMixinViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
