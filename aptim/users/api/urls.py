#end Points 

from django.urls import path
from django.conf.urls import url , include
# from users.api.views import CurrentUserAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token
from .views import UserProfileListCreateView, userProfileDetailView

schema_view = get_schema_view(
   openapi.Info(
      title="APTIM API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns=[
#   path("user/", CurrentUserAPIView.as_view(), name="current-user"),
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
   # paths for existing profiles
   path("all-profiles",UserProfileListCreateView.as_view(),name="all-profiles"),
   path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile") 
    # The rest of the endpoints
]