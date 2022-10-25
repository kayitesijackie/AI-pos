from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from inventory.models import *

from django.http import HttpResponseRedirect, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string

from weasyprint import HTML

# Create your views here.

@login_required
def pos_homeView(request):
    all_products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cart_items = order.orderitem_set.all()
        context = {
            'all_products': all_products,
            'order': order,
            'cart_items': cart_items,
            'payment_mode': Payment_mode
        }
    else:
        context = {
            'all_products': all_products,
            'order': [],
            'cart_items': []
        }
    return render(request, 'pos/pos.html', context)


def receiptView(request, pk):
    try:
        order = Order.objects.get(pk=pk)
        cart_items = order.orderitem_set.all()
        context = {
            'order': order,
            'cart_items': cart_items,
            'cart_items_quantity': order.get_cart_items_quantity,
            'cart_total': order.get_cart_revenue,
            'cart_tax_total': order.get_cart_tax,
            'cart_mrp_total': order.get_cart_mrp,
            'savings': order.get_cart_mrp - order.get_cart_revenue,
        }
        html_string = render_to_string( 'pos/receipt.html', context)
    except ObjectDoesNotExist:
        html_string = render_to_string( 'pos/receipt.html', {'error': "ERROR REASON: "
                                                             "Maybe order doesn't exist,"
                                                             " Check if you have completed the order on POS page,"
                                                             " Check orders page to print the receipt"})

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/invoice.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('invoice.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="invoice.pdf"'
        return response

    return response

def productLabelView(request, pk):
    try:
        product = Product.objects.get(product_code=pk)
        context = {
            'product': product,
        }
        return render(request, 'pos/product-label.html', context)
    except ObjectDoesNotExist:
        return render(request, 'pos/product-label.html', {'error': "ERROR REASON: "
                                                                   "Product not found with that product id"})
