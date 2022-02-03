from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


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
        verbose_name='Краткое описание произведения',
        help_text='Краткое описание произведения',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория',
        help_text='Категория'
    )
    genre = models.ManyToManyField(
        Genre,
        through='Genre_Title',
        verbose_name='Жанр',
        help_text='Жанр'
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


class Review(models.Model):
    """Модель отзыва на произведение."""
    SCORES = tuple([(i, i) for i in range(1, 11)])
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Произведение',
        verbose_name='Произведение'
    )
    text = models.TextField(
        'Текст отзыва',
        help_text='Текст отзыва'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        help_text='Автор отзыва',
        verbose_name='Автор отзыва'
    )
    score = models.IntegerField(
        'Оценка произведения',
        choices=SCORES,
        help_text='Оценка произведения'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        default=timezone.now,
        help_text='Дата публикации'
    )

    class Meta:
        verbose_name = 'Отзыв на произведение'
        verbose_name_plural = 'Отзывы на произведения'
        ordering = ('-pub_date',)
        constraints = (
            models.UniqueConstraint(
                fields=('author', 'title'),
                name='one_author-one_review'
            ),
        )

    def __str__(self) -> str:
        """Переопределяем метод для вывода информации об объекте."""
        return (
            f'Отзыв пользователя {self.author} '
            f'на произведение {self.title}, оценка {self.score}.'
        )


class Comment(models.Model):
    """Модель комментария к отзыву на произведение."""
    text = models.TextField(
        'Комментарий к отзыву',
        help_text='Комментарий к отзыву'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор комментария'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв на произведение',
        help_text='Отзыв на произведение'
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        default=timezone.now,
        help_text='Дата добавления'
    )

    class Meta:
        verbose_name = 'Комментарий к отзыву'
        verbose_name_plural = 'Комментарии к отзывам'
        ordering = ('-pub_date',)

    def __str__(self) -> str:
        """Переопределяем метод для вывода информации об объекте."""
        return (
            'Комментарий пользователя '
            f'{self.author} к отзыву с ID = {self.review.id}'
        )
