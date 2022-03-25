from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from django.urls import path, include

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # https://github.com/encode/django-rest-framework/blob/master/rest_framework/urls.py
    # API で追加するだけならこの URL を使う必要もなさそう
    # NOTE: admin/fukuoka123
]

urlpatterns = format_suffix_patterns(urlpatterns)