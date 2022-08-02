from django import forms
from .models import cadastroatividade

class Formcadastroatividade(forms.ModelForm):
    class Meta:
        model= cadastroatividade
        fields= ["executor", "tipoequipamento", "origequipamento","destequipamento", "infoequipamento", "chamadootrs", "atividaderealizada"]
