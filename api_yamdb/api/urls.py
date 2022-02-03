# from rest_framework.routers import SimpleRouter
from rest_framework import routers
from django.urls import path, include
from api.views import ReviewViewSet, CommentViewSet
from api.views import CategoryViewSet, GenreViewSet, TitleViewSet
from api.views import send_confirmation_code, get_token, UsersViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register('users', UsersViewSet, basename='user')

# router = SimpleRouter()
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
    path('v1/auth/signup/', send_confirmation_code,
         name='SendConfirmationCode'),
    path('v1/auth/token/', get_token, name='GetToken'),
    path('', include(router.urls)),
]
