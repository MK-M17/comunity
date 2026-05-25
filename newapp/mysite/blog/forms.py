from django import forms
from django.contrib.auth.models import User

from .models import Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'id': 'nameInput',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'id': 'exampleInputEmail1',
                                                          'aria-describedby': 'emailHelp',}))
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                       'id': 'comments',
                                                       'rows': '3'}))

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())



from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','short_description','image','tags')

from .models import PostPoint

class PostPointForm(forms.ModelForm):
    class Meta:
        model = PostPoint
        fields = ('post_header', 'post_point_text', 'post_images')

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name',
                'username','email')

class SearchForm(forms.Form):
    query=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control mr-sm-2',
        'type':'search',
        'placeholder':'Search',
        'aria-label':'Search'
    }))