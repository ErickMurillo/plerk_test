from .models import *
from rest_framework import serializers

class TransaccionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaccion
		fields = ('id','id_empresa','price','date','status_transaction','status_approved')