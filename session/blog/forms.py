from django import forms
from .models import Blog
from blog.models import Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

class BlogSearchForm(forms.Form):
    query = forms.CharField()

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': '댓글을 입력하세요...', 'rows': 4, 'cols': 50}))
    blog_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ['content', 'blog_id']