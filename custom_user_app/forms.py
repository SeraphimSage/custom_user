from django import forms
from custom_user_app.models import MyUser


class MyUserForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ["username", "display_name", "age"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
