from django.contrib import admin
from blogs import models
# Register your models here.


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = 'id', 'title', 'author', 'updated_at'


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = 'id', 'title',

class CommentInline(admin.TabularInline):

    model = models.Comment


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    list_display = 'id', 'title', 'blog', 'created_at'
    inlines = CommentInline,


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = 'id', 'post', 'author', 'created_at'

