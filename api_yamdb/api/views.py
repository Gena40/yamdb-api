# from django.shortcuts import get_object_or_404
from rest_framework import viewsets  # , permissions
# from rest_framework.pagination import LimitOffsetPagination
from reviews.models import Review, Comment
from api.serializers import ReviewSerializer, CommentSerializer


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
