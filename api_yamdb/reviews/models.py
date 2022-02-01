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
