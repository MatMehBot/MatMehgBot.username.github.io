from django import forms
from .models import *
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not User.objects.filter(username=username).exists():
            raise ValidationError('User is not register')
        user = User.objects.get(username=username)

        if not user.check_password(password):
            raise ValidationError('Password is wrong')


class RegistrationForm(forms.ModelForm):
    password_check = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password_check',
            'first_name',
            'last_name',
            'email'
        ]

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        password_check = self.cleaned_data['password_check']

        if User.objects.filter(username=username).exists():
            raise ValidationError('User is allready register')
        if password != password_check:
            raise ValidationError('Password not exists')


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = [
            'food_list',
        ]


class CookerForm(forms.ModelForm):

    class Meta:
        model = CookRequest
        fields = [
            'food',
        ]


class SupportForm(forms.ModelForm):

    class Meta:
        model = SupportRequest
        fields = [
                'email',
                'title',
                'message'
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
        ]
