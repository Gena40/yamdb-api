# from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # , permissions
from rest_framework import mixins
from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Review, Comment
from reviews.models import Category, Genre
from api.serializers import ReviewSerializer, CommentSerializer
from api.serializers import CategorySerializer, GenreSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # pagination_class = LimitOffsetPagination
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsAuthorOrReadOnly)
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('group',)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsAuthorOrReadOnly)

    # def perform_create(self, serializer):
    #     post_id = self.kwargs.get('post_id')
    #     this_post = get_object_or_404(Post, id=post_id)
    #     serializer.save(
    #         author=self.request.user,
    #         post=this_post
    #     )

    # def get_queryset(self):
    #     post_id = self.kwargs.get('post_id')
    #     this_post = get_object_or_404(Post, id=post_id)
    #     return this_post.comments.all()


class CategoryViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
):
    '''
    Класс CategoryViewSet для модели Category.
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    pagination_class = LimitOffsetPagination


class GenreViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin
):
    '''
    Класс CategoryViewSet для модели Category.
    '''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    pagination_class = LimitOffsetPagination
