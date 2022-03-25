# MVC ではなく MTV (Model Template View)モデルなので、 Views は他の Controller に近い（も含む）
# https://docs.djangoproject.com/ja/3.2/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User


@api_view(['GET'])
def api_root(request, format=None):
    # https://www.django-rest-framework.org/api-guide/reverse/#reverse
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


class SnippetViewSet(viewsets.ModelViewSet):
    """
    このクラスは list, create, retrieve, update, destroy アクションを自動で提供する
    highlight と create は明示的に設定
    create は perform_create でオーバーライドしている
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     snippet = self.get_object()
    #     return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    この ViewSet は自動的に list と retrieve アクションを提供する
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
