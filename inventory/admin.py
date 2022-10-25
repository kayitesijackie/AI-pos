from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


class ProductList(ImportExportModelAdmin):
    list_display = ('name', 'product_code', 'quantity')
    # exclude = ('amount',)


class OrderItemList(admin.ModelAdmin):
    list_display = ('product', 'order', 'quantity', 'amount')
    exclude = ('amount',)

class ProductCompanyList(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Product, ProductList)
admin.site.register(ProductCategories)
admin.site.register(ProductCompany, ProductCompanyList)
admin.site.register(Order)
admin.site.register(OrderItem, OrderItemList)
