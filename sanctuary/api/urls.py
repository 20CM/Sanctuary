from django.conf.urls import include, url

from rest_framework import routers

from account.api import UserViewSet
from tag.api import TagViewSet
from topic.api import TopicViewSet, ReplyViewSet
from notification.api import NotificationViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)
router.register("tag", TagViewSet)
router.register("topic", TopicViewSet)
router.register("reply", ReplyViewSet)
router.register("notification", NotificationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
