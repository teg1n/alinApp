from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from .models import Share

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={'placeholder': 'E-posta adresinizi girin', 'class':'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;'})
    )

    username= forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder':'Kullanıcı adınızı girin', 'class':'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;' })
    )

    password1=forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder':'Şifrenizi Giriniz', 'class':'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;' })
    )

    password2 = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi tekrar girin', 'class': 'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;'}),
        help_text="Şifreniz en az 8 karakter olmalı, harf ve rakam içermelidir."
    )

    usable_password= None
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Girdiğiniz şifreler eşleşmiyor!")

        return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Kullanıcı Adı",
        widget=forms.TextInput(attrs={'placeholder': 'Kullanıcı adınızı girin', 'class':'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;'})
    )

    password = forms.CharField(
        label="Şifre",
        widget=forms.PasswordInput(attrs={'placeholder': 'Şifrenizi girin', 'class':'form-control', 'style': 'width: 300px; height: 40px;margin: auto; display: block; text-align: center;'})
    )

class ShareForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'maxlength': '150'}),  
        validators=[MaxLengthValidator(150, message="Maksimum 150 karakter girebilirsiniz!")]
    )
    class Meta:
        model = Share
        fields = ['content']
        