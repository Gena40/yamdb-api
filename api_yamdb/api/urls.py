from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views import ReviewViewSet, CommentViewSet


app_name = 'api'

router = SimpleRouter()
router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet
)
router.register(
    r'v1/titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comment',
    CommentViewSet,
    # basename='comment'
)

urlpatterns = [
    path('', include(router.urls)),
]
