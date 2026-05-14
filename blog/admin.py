from django.contrib import admin
from .models import Post, Comment

# This shows comments inside the post admin page
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

# Register Post model with inline comments
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')  # Only use fields that exist
    inlines = [CommentInline]

# Register Comment model
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_date')  # Only fields that exist
    list_filter = ('created_date',)
    search_fields = ('name', 'body')