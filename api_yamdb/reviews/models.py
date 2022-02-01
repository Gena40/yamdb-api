from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Review(models.Model):
    """Модель отзыва на произведение."""
    SCORES = tuple(range(1, 11))
    # title = models.ForeignKey(
    #     Title,
    #     on_delete=models.CASCADE,
    #     related_name='titles'
    # )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(choices=SCORES)
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )

    def __str__(self) -> str:
        """Переопределяем метод для вывода информации об объекте."""
        return f'Отзыв пользователя {self.author}, оценка {self.score}.'


class Comment(models.Model):
    """Модель комментария к отзыву на произведение."""
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
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True
    )

    def __str__(self) -> str:
        """Переопределяем метод для вывода информации об объекте."""
        return (
            'Комментарий пользователя '
            f'{self.author} к отзыву с ID = {self.review.id}'
        )
