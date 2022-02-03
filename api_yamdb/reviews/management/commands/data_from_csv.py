import os
import datetime
from csv import DictReader
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, Genre_Title
from reviews.models import User
from reviews.models import Review, Comment
from api_yamdb.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Копирование данных из csv'
    shift_path = os.path.join(BASE_DIR, 'static')
    shift_path = os.path.join(shift_path, 'data')

    def handle(self, *args, **kwargs):
        self.insert_categories()
        self.insert_genres()
        self.insert_titles()
        self.insert_genge_titles()
        self.insert_users()
        self.insert_reviews()
        self.insert_comments()

    def insert_categories(self):
        filename = self.shift_path + '\\category.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    Category.objects.create(**row)
                    print(row, 'добавлен')
                except Exception as err:
                    print(err)

    def insert_genres(self):
        filename = self.shift_path + '\\genre.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    Genre.objects.create(**row)
                    print(row, 'добавлен')
                except Exception as err:
                    print(err)

    def insert_titles(self):
        filename = self.shift_path + '\\titles.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    num_category = int(row.pop('category'))
                    category = Category.objects.get(pk=num_category)
                    if category:
                        Title.objects.create(category=category, **row)
                        print(category, row, 'добавлен')
                    else:
                        print(num_category, 'не было')
                except Exception as err:
                    print(err)

    def insert_genge_titles(self):
        filename = self.shift_path + '\\genre_title.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    genre_id = int(row.pop('genre_id'))
                    genre = Genre.objects.get(pk=genre_id)
                    title_id = int(row.pop('title_id'))
                    title = Title.objects.get(pk=title_id)
                    if all((genre, title)):
                        Genre_Title.objects.create(
                            genre=genre, title=title, **row)
                        print(genre, title, row, 'добавлен')
                    else:
                        print(row, 'нельзя создать')
                except Exception as err:
                    print(err)

    def insert_users(self):
        filename = self.shift_path + '\\users.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    User.objects.create(**row)
                    print(row, 'добавлен')
                except Exception as err:
                    print(err)

    def insert_reviews(self):
        filename = self.shift_path + '\\review.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    format_dt = '%Y-%m-%dT%H:%M:%S.%fZ'
                    dt = datetime.datetime.strptime(
                        row.pop('pub_date'), format_dt)
                    title_id = int(row.pop('title_id'))
                    title = Title.objects.get(pk=title_id)
                    author_id = int(row.pop('author'))
                    author = User.objects.get(pk=author_id)
                    id = row.pop('id')
                    text = row.pop('text')
                    score = row.pop('score')
                    if all((title, author, dt)):
                        Review.objects.create(
                            title=title, author=author, id=id,
                            text=text, score=score, pub_date=dt)
                    else:
                        print(row, 'нельзя создать')
                except Exception as err:
                    print(err)

    def insert_comments(self):
        filename = self.shift_path + '\\comments.csv'
        print(filename)
        with open(filename, 'r', encoding='utf-8') as f:
            csvdict = DictReader(f)
            for row in csvdict:
                try:
                    format_dt = '%Y-%m-%dT%H:%M:%S.%fZ'
                    dt = datetime.datetime.strptime(
                        row.pop('pub_date'), format_dt)
                    review_id = int(row.pop('review_id'))
                    review = Review.objects.get(pk=review_id)
                    author_id = int(row.pop('author'))
                    author = User.objects.get(pk=author_id)
                    if all((review, author, dt)):
                        Comment.objects.create(
                            review=review, author=author, pub_date=dt, **row)
                        print(review, author, row, dt, 'добавлен')
                    else:
                        print(row, 'нельзя создать')
                except Exception as err:
                    print(err)
