from django import forms
from survey.models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['gender', 'age', 'region_1', 'area_1']
        fields = ['gender', 'age', 'region_1', 'area_1','region_2', 'area_2','region_3', 'area_3']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['region_1'].widget.attrs['class'] = 'form-select'
        self.fields['area_1'].widget.attrs['class'] = 'form-select'
        # self.fields['region_2'].widget.attrs['class'] = 'form-select'
        # self.fields['area_2'].widget.attrs['class'] = 'form-select'
        # self.fields['region_3'].widget.attrs['class'] = 'form-select'
        # self.fields['area_3'].widget.attrs['class'] = 'form-select'