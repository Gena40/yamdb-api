from django.contrib import admin
from reviews.models import Review, Comment


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'author',
        'score',
        'pub_date'
    )
    list_editable = ('text', 'score')
    search_fields = ('text',)
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'review',
        'text',
        'author',
        'pub_date'
    )
    list_editable = ('text',)
    search_fields = ('text', 'author')
    list_filter = ('pub_date', 'author')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
