from django.conf.urls import include, url

from rest_framework import routers

from account.api import UserViewSet
from tag.api import TagViewSet
from topic.api import TopicViewSet, ReplyViewSet
from notification.api import NotificationViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("tags", TagViewSet)
router.register("topics", TopicViewSet)
router.register("replies", ReplyViewSet)
router.register("notifications", NotificationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]
