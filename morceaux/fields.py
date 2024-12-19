from django import forms

class CustomModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def clean(self, value):
        if value and '' in value:
            value.remove('')
        return super().clean(value)