from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    
    def read_time(self):
        """Calculate estimated reading time in minutes"""
        word_count = len(self.content.split())
        return max(1, round(word_count / 200))  # 200 words per minute
    
    def __str__(self):
        return self.title