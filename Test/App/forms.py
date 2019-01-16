from django import forms
from App.models import StudentModel



class StudentForm(forms.Form):
    name = forms.CharField(
        label = "User Name",
        widget = forms.TextInput(
            attrs=({'placeholder':'Enter user name', 'id':'name'})
        ),
        required = False,
    )

    email = forms.EmailField(
        label="Enter email address",
        widget= forms.TextInput(
            attrs=({'placeholder':'Enter email address','id':'email'})
        ),
        required=False,
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "":
            raise forms.ValidationError("Name shouldn't be empty!")
        elif len(name)<=3:
            raise forms.ValidationError("Name length should not be less than 3")
        else:
            return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != "":
            return email
        else:
            raise forms.ValidationError("Email shouldn't be empty!")