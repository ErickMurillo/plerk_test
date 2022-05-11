from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
# Register your models here.

class EmpresaResource(resources.ModelResource):
	class Meta:
		model = Empresa
		fields = ('id', 'nombre', 'status')

class EmpresaAdmin(ImportExportModelAdmin):
	 resource_class = EmpresaResource

class TransaccionResource(resources.ModelResource):
	class Meta:
		model = Transaccion
		fields = ('id', 'id_empresa', 'price', 'date', 'status_transaction', 'status_approved')

class TransaccionAdmin(ImportExportModelAdmin):
	resource_class = TransaccionResource
	list_display = ('id', 'id_empresa', 'price', 'date', 'status_transaction', 'status_approved')


admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Transaccion,TransaccionAdmin)
