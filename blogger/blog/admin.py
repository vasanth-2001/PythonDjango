from django.contrib import admin
from .models import Blogger, Post

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'contact')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('email',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'blogger', 'slug')
    list_filter = ('date', 'blogger')
    search_fields = ('title', 'content', 'description')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'date'
    ordering = ('-date',)