from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: #메타 클래스
        model=Post
        fields=['title','photo','body'] #항목지정가능
        # fields='__all__'   #모든 항목 입력 가능