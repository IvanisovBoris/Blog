from django import forms


class ReviewForm(forms.Form):
    text = forms.CharField(label="text", max_length=255)


class LoginForm(forms.Form):
    username = forms.CharField(label="login", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
