from django import forms
from .models import Choice



class questForm(forms.ModelForm):
   

    class Meta:
        model = Choice
        fields = ('question_text','Choice1', 'Choice2', 'Choice3')