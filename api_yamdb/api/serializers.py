from django.db.models import Avg
from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField
from reviews.models import Review, Comment
from reviews.models import Category
from reviews.models import Genre
from reviews.models import Title
# from reviews.models import Genre_Title
from users.models import User


class UserEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class ConfirmationCodeSerializer(serializers.ModelSerializer):
    confirmation_code = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

    username = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',
                  'bio', 'role')
        read_only_fields = ('role', )


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


class CategorySerializer(serializers.ModelSerializer):
    '''
    Класс CategorySerializer для модели Category.
    '''
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    '''
    Класс GenreSerializer для модели Genre.
    '''
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    '''
    Класс TitleSerializer для модели Title.
    '''
    rating = serializers.SerializerMethodField()
    genre = GenreSerializer(many=True, required=True)
    category = CategorySerializer(many=False, required=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating',
            'description', 'genre', 'category'
        )

    def get_rating(self, title_obj):
        if title_obj.reviews.count() > 0:
            score = title_obj.reviews.aggregate(Avg('score'))
            return score.get('score__id')
        return None
