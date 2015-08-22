from django.conf.urls import include, url

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from account.api import UserViewSet
from tag.api import TagViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("tags", TagViewSet)

urlpatterns = [
    url(r'^token/$', obtain_auth_token),
    url(r'^', include(router.urls)),
]