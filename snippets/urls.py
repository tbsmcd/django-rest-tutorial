from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets.views import SnippetViewSet, UserViewSet


# ViewSets を使っているので下記のように簡略化できる
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippets')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    # path('', api_root), <- 削除可能。DefaultRouter がやってくれる
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
