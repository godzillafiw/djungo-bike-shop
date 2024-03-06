from django.contrib.auth import password_validation
from store.models import Address
from django import forms
import django
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _



class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='รหัสผ่าน', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'รหัสผ่าน'}))
    password2 = forms.CharField(label="ยืนยันรหัสผ่าน", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'ยืนยันรหัสผ่าน'}))
    email = forms.CharField(required=True, label='อีเมล', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'ที่อยู่อีเมล'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'username':'บัญชีผู้ใช้งาน','email': 'อีเมล'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'บัญชีผู้ใช้งาน'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_("บัญชีผู้ใช้งาน"),widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(label=_("รหัสผ่าน"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['locality', 'city', 'state']
        widgets = {'locality':forms.TextInput(attrs={'class':'form-control', 'placeholder':'สถานที่ยอดนิยม เช่น ร้านอาหาร สถานที่ทางศาสนา ฯลฯ'}), 'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'เมือง'}), 'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'รัฐหรือจังหวัด'})}


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("รหัสผ่านเก่า"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'auto-focus':True, 'class':'form-control', 'placeholder':'รหัสผ่านปัจจุบัน'}))
    new_password1 = forms.CharField(label=_("รหัสผ่านใหม่"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'รหัสผ่านใหม่'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("ยืนยันรหัสผ่าน"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control', 'placeholder':'ยืนยันรหัสผ่าน'}))


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("รหัสผ่านใหม่"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("ยืนยันรหัสผ่าน"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))

