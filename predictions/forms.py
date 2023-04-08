from django import forms
from .symptoms import SYMPTOMS

class SymptomsForm(forms.Form):

    symptom1 = forms.ChoiceField(choices=SYMPTOMS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    symptom2 = forms.ChoiceField(choices=SYMPTOMS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    symptom3 = forms.ChoiceField(choices=SYMPTOMS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    symptom4 = forms.ChoiceField(choices=SYMPTOMS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    symptom5 = forms.ChoiceField(choices=SYMPTOMS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        form_data = super().clean()

        symptom1 = form_data.get('symptom1')
        symptom2 = form_data.get('symptom2')
        symptom3 = form_data.get('symptom3')
        symptom4 = form_data.get('symptom4')
        symptom5 = form_data.get('symptom5')

        return symptom1, symptom2, symptom3, symptom4, symptom5
