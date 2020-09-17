from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class SignUpForm(UserCreationForm, forms.ModelForm):
    email = forms.EmailField(
        label=False,
        widget=forms.EmailInput(attrs={'class': 'form-control',
                                       'placeholder': 'E-mail'})
    )
    first_name = forms.CharField(
        label=False,
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'First name'})
    )
    last_name = forms.CharField(
        label=False,
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Last name'})
    )
    username = forms.CharField(
        label=False,
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        label=False,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Repeat the password'})
    )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        try:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
        except KeyError:
            errors = {
                'password1': ValidationError('Короткий',
                                             code='password_mismatch')
            }
            raise ValidationError(errors)

        if password1 and password2 and password1 != password2:
            errors = {
                'password2': ValidationError('Введенные пароли не совпадают',
                                             code='password_mismatch')
            }
            raise ValidationError(errors)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=120,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )
    new_password1 = forms.CharField(
        max_length=120,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )
    new_password2 = forms.CharField(
        max_length=120,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'})
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
