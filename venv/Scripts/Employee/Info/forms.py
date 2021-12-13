from django import forms
from .models import Empdet
class EmpdetForms(forms.ModelForm):
    class Meta:
        model = Empdet
        fields = '__all__'
