from rest_framework import generics, mixins

from ..models import Article
from ..serializers import ArticleSerializer


class ArticleList(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request, pk=None):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ArticleDetail(
    generics.GenericAPIView,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    def get(self, request, pk=None):
        return self.retrieve(request, pk)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)
