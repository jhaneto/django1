from django.db import models

# Create your models here.ass 
class Contato(models.Model):
    nome = models.CharField('Nome',max_length=150)
    endereco = models.CharField('Endereço', max_length=100)
    numero = models.DecimalField('Numero',max_digits = 4, decimal_places=2)
    telefone = models.CharField('Telefone', max_length=9)
    email = models.EmailField('E-mail', max_length=100, null=True)
     
    def __str__(self):
        return self.nome
         
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    descriacao = models.CharField('Descrição', max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    quantidade = models.IntegerField()
    
    def __str__(self):
        return self.nome