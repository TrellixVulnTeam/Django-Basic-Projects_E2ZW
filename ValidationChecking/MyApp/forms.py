from django import forms
from MyApp.models import PasswordModel




class PasswordForm(forms.ModelForm):

    password = forms.CharField(
        label='Enter a password',
        widget=forms.PasswordInput(
            attrs=({'placeholder':'Enter a password', 'id':'password'})),
        required=True,
        max_length=20,
    )

    confirm_password = forms.CharField(
        label="Confirm your password",
        widget=forms.PasswordInput(
            attrs=({'placeholder':'Confirm password', 'id':'confirm_password'})
        ),
        required=True,
        max_length=20,
    )

    class Meta:
        model = PasswordModel
        fields = [
            'password',
            'confirm_password'
        ]

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Password didn't match")
        return confirm_password
