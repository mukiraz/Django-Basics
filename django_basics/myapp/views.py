from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse
import datetime

# Create your views here.

data = {
    "telefon": ["telefon 1", "telefon 2", "telefon 3"],
    "bilgisayar": ["bilgisayar 1", "bilgisayar 2"],
    "elektronik": [],
}

def index(request):
    list_items = ""
    categories = list(data.keys())
    for category in categories:
        redirect_path = reverse('products_by_category', args =[category])
        list_items += f'<li><a href ="{redirect_path}">{category}</a></li>'

    html = f'<ul>{list_items}</ul>'
    
    return render(request, 'index.html', {
        "categories":categories
    })


def getProductsByCategoryID(request, category_id):
    try:
        ids = list(data.keys())
        category_name = ids[category_id-1]
        redirect_path = reverse('products_by_category', args =[category_name])
        return redirect(redirect_path)
    except IndexError:
        return HttpResponseNotFound("kategori bulunamadı")

def getProductsByCategory(request, category):
    try:
        now = datetime.datetime.now()
        products = data[category]    
        return render(request, 'products.html', {
            "category":category,
            "products":products,
            "now":now
        })
    except KeyError:
        return HttpResponseNotFound("kategori bulunamadı")
