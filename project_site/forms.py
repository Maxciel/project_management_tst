from core.models import Project
from django import forms


# FORMULÁRIO DE INCLUSÃO DE FUNCIONÁRIOS
# -------------------------------------------

class IncludeProjectForm(forms.ModelForm):

    #chefe = forms.BooleanField(
    #    label='Chefe?',
    #    required=False,
    #)
    #project_name = forms.CharField(
    #    label='Nome do projeto xxx',
    #    required=False,
    #    widget=forms.Textarea
    #)

    start_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    finish_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )


    class Meta:
        model = Project
        # Campos que estarão no form
        fields = ['project_name', 'start_date', 'finish_date', 'proj_amount', 'proj_risk', 'proj_team']
