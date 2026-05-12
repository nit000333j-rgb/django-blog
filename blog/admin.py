from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'published')
    list_editable = ('published',)
    list_filter = ('published',)
    ordering = ('created_at',)  # ← Add this line (note: tuple with comma)
    actions = ['make_published', 'make_unpublished']

def make_published(self, request, queryset):
    count = queryset.update(published=True)
    self.message_user(request, f"{count} posts were published.")
    make_published.short_description = "Publish selected posts"

def make_unpublished(self, request, queryset):
    count = queryset.update(published=False)
    self.message_user(request, f"{count} posts were unpublished.")
    make_unpublished.short_description = "Unpublish selected posts"

admin.site.register(Post, PostAdmin)