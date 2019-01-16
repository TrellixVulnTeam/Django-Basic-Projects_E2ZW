from django import forms
from App.models import StudentModel



class ValidationForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        required=False,
        widget=(forms.TextInput(attrs=({'placeholder':'Enter valid title'})))
    )

    class Meta:
        model = StudentModel
        fields=['title']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data['title']
        if title != "":
            return title
        else:
            raise forms.ValidationError("Form shouldn't be Empty!")