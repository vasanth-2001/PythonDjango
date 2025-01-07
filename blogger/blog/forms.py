from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_name', 'content', 'description', 'image', 'blogger']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }