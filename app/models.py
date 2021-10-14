from django.db import models


def upload_image_carros(instance, filename):
    return f"{instance.id_carros}-{filename}"

# Create your models here.

class Orcamentos(models.Model):
    quantidade      =   models.IntegerField()
    descricao       =   models.CharField(max_length=250)
    precoUnitario   =   models.IntegerField()
    subTotal        =   models.IntegerField()
    total           =   models.IntegerField()
    frete           =   models.IntegerField()
    taxas           =   models.IntegerField()

class Carros(models.Model):
    modelo          =   models.CharField(max_length=150)
    marca           =   models.CharField(max_length=100)
    ano             =   models.IntegerField()
    image           =   models.ImageField(upload_to='media/')
    class Meta:
        db_table = "app_carros"


class Vendedores(models.Model):
    nome            = models.CharField(max_length=150)
    telefone        = models.CharField(max_length=100)
    nascimento      = models.CharField(max_length=12)
    endereco        = models.CharField(max_length=250)
    funcao          = models.CharField(max_length=100)
    estado          = models.CharField(max_length=20)
    cidade          = models.CharField(max_length=100)
    cep             = models.CharField(max_length=25)
    rua             = models.CharField(max_length=25)
    foto            = models.ImageField(upload_to='media/')




    