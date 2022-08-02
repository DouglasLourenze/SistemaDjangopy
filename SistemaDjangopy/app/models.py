from django.db import models

# Create your models here.

class cadastroatividade(models.Model):
    executor= models.CharField(max_length=50)
    tipoequipamento= models.CharField(max_length=100)
    origequipamento= models.CharField(max_length=100)
    destequipamento= models.CharField(max_length=100)
    infoequipamento= models.CharField(max_length=100)
    chamadootrs= models.CharField(max_length=50)
    atividaderealizada= models.CharField(max_length=3000)

    class Meta:
        db_table = "cadastroatividade"