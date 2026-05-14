from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:  # You forgot 'class Meta:'
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment...', 'rows': 4}),
        }