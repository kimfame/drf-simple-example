from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views import (
    ex_1_regular_view,
    ex_2_decorator_api_view,
    ex_3_class_api_view,
    ex_4_mixin_api_view,
    ex_5_generic_api_view,
    ex_6_viewset,
    ex_7_mixin_viewset,
    ex_8_model_viewset,
)

router = DefaultRouter()

# ViewSet
router.register("viewset", ex_6_viewset.ArticleViewSet, basename="viewset")

# Mixin ViewSet
router.register(
    "mixin_viewset", ex_7_mixin_viewset.ArticleMixinViewSet, basename="mixin_viewset"
)

# Model ViewSet
router.register(
    "model_viewset", ex_8_model_viewset.ArticleModelViewSet, basename="model_viewset"
)


urlpatterns = [
    # Regular Method
    path("regular-method/", ex_1_regular_view.article_list),
    path("regular-method/<int:pk>/", ex_1_regular_view.article_detail),
    # Decorator APIView
    path("decorator_api_view/", ex_2_decorator_api_view.article_list),
    path("decorator_api_view/<int:pk>/", ex_2_decorator_api_view.article_detail),
    # Class APIView
    path("class_api_view/", ex_3_class_api_view.ArticleList.as_view()),
    path("class_api_view/<int:pk>/", ex_3_class_api_view.ArticleDetail.as_view()),
    # Mixin APIView
    path("mixin_api_view/", ex_4_mixin_api_view.ArticleList.as_view()),
    path("mixin_api_view/<int:pk>/", ex_4_mixin_api_view.ArticleDetail.as_view()),
    # Generic APIView
    path("generic_api_view/", ex_5_generic_api_view.ArticleList.as_view()),
    path("generic_api_view/<int:pk>/", ex_5_generic_api_view.ArticleDetail.as_view()),
    # Router
    path("", include(router.urls)),
]

urlpatterns.append(path("admin/", admin.site.urls))
