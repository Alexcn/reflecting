from django import forms


class CommentForm(forms.Form):
    url = forms.CharField(required=True)
    body = forms.CharField(required=True)


class ReplyForm(forms.Form):
    commentid = forms.CharField(required=True)
    body = forms.CharField(required=True)