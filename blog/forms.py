from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='称呼')
    email = forms.EmailField(label='邮箱')
    content = forms.CharField(label='内容')
