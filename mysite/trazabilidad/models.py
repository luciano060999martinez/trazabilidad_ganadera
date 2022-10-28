from unittest.util import _MAX_LENGTH
from django.db import models
from .choices import sexos, estados

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Propietario(models.Model):
    #por defecto crea el ID Propietario
    propietario_nombre = models.CharField(max_length=50)
    propietario_apellido = models.CharField(max_length=50)
    propietario_ci = models.PositiveIntegerField(null=False, unique = True)
    propietario_ruc = models.CharField(max_length = 50)
    propietario_direccion = models.CharField(max_length = 100)
    propietario_telefono = models.CharField(max_length = 50)
    sexo = models.CharField(max_length = 1, choices = sexos, default = 'M')

class Estado(models.Model):
    #por defecto crea estado_id
    estado_animal = models.CharField(max_length = 1, choices = estados)


class Animal(models.Model):
    #por defecto crea el ID ANIMAL
    codigo_animal = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    peso = models.FloatField()
    propietario = models.ForeignKey(Propietario, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, default = 'V') #recien agregado

class Vacuna(models.Model): #recien agregado
    vacuna_nombre = models.CharField(max_length = 50)
    vacuna_origen = models.CharField(max_length = 50)
    vacuna_dosis = models.PositiveBigIntegerField(default = 0)

class Vacuna_X_Animal(models.Model): #recien agregado
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vacuna = models.ForeignKey(Vacuna, on_delete = models.CASCADE)



