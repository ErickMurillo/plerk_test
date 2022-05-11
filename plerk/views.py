from django.shortcuts import render
from .serializers import *
from .models import *
from django.db.models import Avg, Max, Min, Sum, Count
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.contrib.auth.models import User

# Create your views here.
@api_view()
def servicio_resumen(request):
	dict = {}
	dict_cobros = {}
	for x in Transaccion.objects.distinct('id_empresa'):
		ventas = Transaccion.objects.filter(id_empresa = x.id_empresa).aggregate(total = Sum('price'))['total']
		empresa_no_cobros = Transaccion.objects.filter(id_empresa = x.id_empresa, status_approved = False).count()

		dict[x.id_empresa.nombre] = ventas

		dict_cobros[x.id_empresa.nombre] = empresa_no_cobros

	#empresa con mas ventas
	max_ventas = max(dict, key=dict.get)
	#empresa con menos ventas
	min_ventas = min(dict, key=dict.get)
	#empresa con mas rechazos de ventas
	rechazos = max(dict_cobros, key=dict_cobros.get)

	cobros = Transaccion.objects.filter(status_transaction = 'closed', status_approved = True).aggregate(total = Sum('price'))['total']
	no_cobros = Transaccion.objects.filter(status_approved = False).aggregate(total = Sum('price'))['total']

	return Response({"La empresa con más ventas": max_ventas,
					"La empresa con menos ventas": min_ventas,
					"El precio total de las transacciones que SÍ se cobraron": cobros,
					"El precio total de las transacciones que NO se cobraron": no_cobros,
					"La empresa con más rechazos de ventas": rechazos })

@api_view()
def servicio_empresa(request, id=None):
	empresa = Empresa.objects.get(id = id)
	si_cobraron = Transaccion.objects.filter(id_empresa = id,status_transaction = 'closed', status_approved = True).count()
	no_cobraron = Transaccion.objects.filter(id_empresa = id, status_approved = False).count()

	dict = {}
	for x in Transaccion.objects.filter(id_empresa = id).distinct('date__year','date__month', 'date__day'):
		count = Transaccion.objects.filter(date__year = x.date.year, date__month = x.date.month, date__day = x.date.day, id_empresa = id).count()
		dict[x.date.strftime('%Y-%m-%d')] = count
		
	max_transacciones = max(dict, key=dict.get)

	return Response({"Nombre de la empresa": empresa.nombre,
					"Total de transacciones que SÍ se cobraron": si_cobraron,
					"Total de transacciones que NO se cobraron": no_cobraron,
					"El día que se registraron más transacciones": max_transacciones})


