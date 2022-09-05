from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
import datetime
from .models import Product

# Create your views here.

# we assumed that the data dictionary is from a database
data = {
    "telefon": ["telefon 1", "telefon 2", "telefon 3"],
    "bilgisayar": ["bilgisayar 1", "bilgisayar 2"],
    "elektronik": [],
}

# the index page
def index(request):
    products = Product.objects.all()
    
    return render(request, 'index.html', {
        "products":products
    })

def details(request, id):
    product = Product.objects.get(pk = id)
    context = {
        "product": product
    }

    return render(request, "details.html", context)



def getProductsByCategoryID(request, category_id):
    try:
        ids = list(data.keys())
        category_name = ids[category_id-1]
        # we send the category_name as parameter to the products_by_category named url path!!!!
        # here if the id is 1, category_name is "telephone"
        # with rewerse function, indeed we call the getProductsByCategory function.
        redirect_path = reverse('products_by_category', args =[category_name])
        return redirect(redirect_path)
        # this exception is used for exceeding the number of products
    except IndexError:
        return HttpResponseNotFound("kategori bulunamadı")

def getProductsByCategory(request, category):
    try:
        # we used now variable to see the filter in html page
        now = datetime.datetime.now()
        # products variable is a list, it holds products- list
        products = data[category]    
        return render(request, 'products.html', {
            "category":category,
            "products":products,
            "now":now
        })
    except KeyError:
        return HttpResponseNotFound("kategori bulunamadı")
