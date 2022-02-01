import os
from csv import DictReader
from django.core.management.base import BaseCommand
from reviews.models import Category, Genre, Title, Genre_Title
from api_yamdb.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Копирование данных из csv'
    shift_path = os.path.join(BASE_DIR, 'static')
    shift_path = os.path.join(shift_path, 'data')

    def handle(self, *args, **kwargs):
        print(self.shift_path)
        # Категории
        self.insert_categories()
        # Жанры
        self.insert_genres()
        # Произведения
        self.insert_titles()
        # Жанры-Произведения
        self.insert_genge_titles()

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
