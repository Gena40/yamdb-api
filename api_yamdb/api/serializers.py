from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField
from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    # author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(
    #     read_only=True, slug_field='username'
    # )

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')
        # read_only_fields = ('post', 'created')
