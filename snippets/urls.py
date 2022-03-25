from rest_framework.routers import DefaultRouter
from django.urls import path, include
from snippets import views
from rest_framework import renderers


# ViewSets を使っているので下記のように簡略化できる
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippets')
router.register(r'users', views.UserViewSet, basename='users')

# 例外のものは明示した
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])

urlpatterns = [
    # path('', api_root), <- 削除可能。DefaultRouter がやってくれる
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
]
