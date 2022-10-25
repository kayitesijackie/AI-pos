from import_export import resources
from .models import  Product

class  ProductResource(resources.ModelResource):
    class Meta:
        model =  Product
        fields = ['product_code','name','cost', 'mrp', 'discount_price','discount_percentage','quantity_unit', 'quantity','weight', 'weight_unit','expiry_date','company','brand', 'tax_type','tax_rate', 'description', 'category','rack_number','modified_time' ]