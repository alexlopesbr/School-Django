from django import forms

from core.models import CustomUser


class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        is_editing = kwargs.pop('is_editing', False)
        super(UserForm, self).__init__(*args, **kwargs)
        if is_editing:
            self.fields['first_name'].required = False
            self.fields['role'].required = False

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
