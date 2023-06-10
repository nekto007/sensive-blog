from django.contrib import admin
from blog.models import Post, Tag, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ['post', 'author', ]
    search_fields = ('post', 'author', 'published_at',)
    list_display = ['post', 'author', 'text', 'published_at', ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'likes', 'tags']
    list_display = ['title', 'slug', 'published_at', 'author']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']
