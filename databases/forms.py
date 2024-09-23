from django import forms

from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm

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
    birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}), label='Data de nascimento')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'sex', 'country', 'state', 'birth_date', 'email')

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
