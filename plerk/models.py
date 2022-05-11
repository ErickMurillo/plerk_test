
import uuid
from django.db import models

# Create your models here.
STATUS_EMPRESA_CHOICE = ((1,'activa'),(0,'inactiva'))

class Empresa(models.Model):
	id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
	nombre = models.CharField(max_length=50)
	status = models.IntegerField(choices = STATUS_EMPRESA_CHOICE)

	def __str__(self):
		return self.nombre

STATUS_TRANSACTION = (('closed','closed'),('reversed','reversed'),('pending','pending'))
class Transaccion(models.Model):
	id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
	id_empresa = models.ForeignKey(Empresa, verbose_name="Empresa", on_delete=models.CASCADE)
	price = models.FloatField()
	date = models.DateTimeField(auto_now=False, auto_now_add=False)
	status_transaction = models.CharField(choices = STATUS_TRANSACTION, max_length=20)
	status_approved = models.BooleanField()

	def __str__(self):
		return self.id