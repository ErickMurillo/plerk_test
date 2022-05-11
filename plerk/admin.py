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

# from django import forms
# class ProductAdminForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ProductAdminForm, self).__init__(*args, **kwargs)
#         self.fields['date'].widget = admin.widgets.AdminSplitDateTime()

class TransaccionAdmin(ImportExportModelAdmin):
	resource_class = TransaccionResource
	# form = ProductAdminForm

admin.site.register(Empresa,EmpresaAdmin)
admin.site.register(Transaccion,TransaccionAdmin)
