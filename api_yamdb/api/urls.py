from rest_framework.routers import SimpleRouter
from django.urls import path, include
from api.views import ReviewViewSet, CommentViewSet
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet


app_name = 'api'

router = SimpleRouter()
router.register('v1/categories', CategoryViewSet)
router.register('v1/genres', GenreViewSet)
router.register('v1/titles', TitleViewSet)
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
