from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField()
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return f'Отзыв пользователя {self.author}, оценка {self.score}.'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    def __str__(self) -> str:
        return (
            'Коментарий пользователя '
            f'{self.author} к отзыву с ID = {self.review.id}'
        )


class Category(models.Model):
    '''
    Класс Category.
    '''
    name = models.CharField(
        max_length=256,
        verbose_name='Категория',
        help_text='Категория',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug категории',
        help_text='Slug категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        '''
        При обращении к экземпляру возвращаем slug для ссылки на категорию.
        '''
        return f'Категория: {self.slug}'


class Genre(models.Model):
    '''
    Класс Genre.
    '''
    name = models.CharField(
        max_length=256,
        verbose_name='Жанр',
        help_text='Жанр',
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='Slug жанра',
        help_text='Slug жанра'
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        '''
        При обращении к экземпляру возвращаем slug для ссылки на жанр.
        '''
        return f'Жанр: {self.slug}'


class Title(models.Model):
    '''
    Класс Title.
    '''
    name = models.CharField(
        max_length=200,
        verbose_name='Произведение',
        help_text='Произведение',
    )
    year = models.IntegerField(
        verbose_name='Год выпуска',
        help_text='Год выпуска'
    )
    description = models.TextField(
        verbose_name='Кратное описание произведения',
        help_text='Кратное описание произведения',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='Категория',
        help_text='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        through='Genre_Title',
        verbose_name='Жанр',
        help_text='Жанр',
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        '''
        При обращении к экземпляру возвращаем name.
        '''
        return self.name


class Genre_Title(models.Model):
    '''
    Класс Genre_Title.
    '''
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
        help_text='Жанр',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Произведение',
        help_text='Произведение',
    )

    def __str__(self):
        return f'Жанр {self.genre} для произведения {self.title}'
