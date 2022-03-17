from django.contrib import admin
from django.urls import path
from account.views import AccountListCreateApi, AccountRetrieveUpdateDestroyAPIView
from feed.views import PostListCreateApi, PostRetrieveUpdateDestroyAPIView, CommentListCreateApi, CommentRetrieveUpdateDestroyAPIView, MediaListCreateApi, MediaRetrieveUpdateDestroyAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Instagram API",
      default_version='v1',
      description="This Api was created using Django, Django Rest Framework",
      contact=openapi.Contact("Abduvaxobov Abdunabi <email:AbdunabiAbduvahobov86@gmail.com>"),
   ),
   public=True,

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account', AccountListCreateApi.as_view(), name='account'),
    path('accountrud/<int:pk>', AccountRetrieveUpdateDestroyAPIView.as_view(), name='accountrud'),
    path('post', PostListCreateApi.as_view(), name='post'),
    path('postrud/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view(), name='postrud'),
    path('comment', CommentListCreateApi.as_view(), name='comment'),
    path('commentrud/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='commentrud'),
    path('media', MediaListCreateApi.as_view(), name='media'),
    path('mediarud/<int:pk>', MediaRetrieveUpdateDestroyAPIView.as_view(), name='mediarud'),
    path('docs/', schema_view.with_ui("swagger", cache_timeout=0), name="docs")
]
