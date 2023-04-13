from django import forms
from .models import Post, Category

class PostCreate(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'title',
            'text'
        ]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     request = self.request
    #     if request.path.startswith('/news/'):
    #         cleaned_data['type'] = 'news'
    #     elif request.path.startswith('/articles/'):
    #         cleaned_data['type'] = 'article'
    #     return cleaned_data
