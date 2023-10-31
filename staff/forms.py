from django import forms

from core.models import CustomUser


class UserForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='first_name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES
    )

class UserList(forms.Form):
    ROLE_CHOICES = [
        ('all', 'All'),
        *CustomUser.ROLE_CHOICES
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(attrs={'id': 'roleSelect'})
    )
