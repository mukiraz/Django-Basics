from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect, reverse

# Create your views here.

data = {
    "telefon": "telefon kategorisindeki ürünler",
    "bilgisayar": "bilgisayar kategorisindeki ürünler",
    "elektronik": "elektronik kategorisindeki ürünler",
}

def index(request):
    return HttpResponse("index")

def details(request):
    return HttpResponse("details")

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
        category_text = data[category]    
        return HttpResponse(category_text)
    except KeyError:
        return HttpResponseNotFound("kategori bulunamadı")
