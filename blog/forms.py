from django import forms
from .models import Comment


class CommentForm(forms.Form):
    author = forms.CharField(label="Author", max_length=128)
    body = forms.CharField(widget=forms.Textarea(attrs={"rows": "5"}))

    def save(self, post_obj):
        data = self.cleaned_data
        print(data)
        comment = Comment(author=data['author'], body=data['body'], post=post_obj)
        comment.save()
