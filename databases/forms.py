from django import forms

from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone

from django.utils.translation import gettext_lazy as _

from databases.models import *


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, label='País')
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, label='Estado')
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label='Data de nascimento')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'sex', 'country', 'state', 'birth_date', 'email') + UserCreationForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop('autofocus', None)
        self.fields['password1'].widget.attrs.pop('autofocus', None)
        self.fields['password2'].widget.attrs.pop('autofocus', None)

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if birth_date > timezone.now().date():
            self.add_error('birth_date', forms.ValidationError('Data de nascimento não pode ser posterior ao dia atual.', code='Claudenir'))
        return birth_date

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            self.add_error(
                'email',
                forms.ValidationError('Email já cadastrado.', code='invalid')
            )
        return email


class ModifyUserForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    country = forms.ModelChoiceField(queryset=Country.objects.all(), required=False, label='País')
    state = forms.ModelChoiceField(queryset=State.objects.all(), required=False, label='Estado')
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'format': '%Y-%m-%d'}), input_formats=['%Y-%m-%d'], label='Data de nascimento')

    password1 = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'sex', 'country', 'state', 'birth_date', 'email', 'password1', 'password2')

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()
        
        return user
        

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', forms.ValidationError('Senhas não coincidem'))
        
        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if email != current_email:
            if CustomUser.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    forms.ValidationError('Email já cadastrado.', code='invalid')
                )
        
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except Exception as errors:
                self.add_error('password1', forms.ValidationError(errors))
        
        return password1


class ThemeChoiceForm(forms.Form):
    theme = forms.ModelMultipleChoiceField(queryset=Theme.objects.all(), label='Temas')