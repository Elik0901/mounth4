from django.shortcuts import render
from product.models import Product


# Create your views here.
def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def products_view(request):
    if request.method == 'GET':

        product =Product.objects.all()

        # context = {
        #     'product':product
        # }
        return render(request, 'product/product.html', {'product':product})
