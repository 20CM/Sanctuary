from django.conf.urls import include, url

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from account.api import UserViewSet
from tag.api import TagViewSet
from topic.api import TopicViewSet, ReplyViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("tag", TagViewSet)
router.register("topic", TopicViewSet)
router.register("reply", ReplyViewSet)

urlpatterns = [
    url(r'^token/$', obtain_auth_token),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
