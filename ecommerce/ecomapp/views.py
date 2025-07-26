from django.shortcuts import render


#def home(request):
    #return render(request, 'index.html')


from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product, Category
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'products': products
})