from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from engine.models import *


def index(request):
    products = Product.objects.all()
    return render(request, "engine/index.html", context={"products": products})


def create(request):
    create_companies()

    if request.method == "POST":
        product = Product()
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.company_id = request.POST.get('company')
        product.save()
        return redirect('home')

    companies = Company.objects.all()
    return render(request, "engine/create.html", context={'companies': companies})


def edit(request, id):
    try:
        product = Product.objects.get(id=id)
        if request.method == "POST":
            product.name = request.POST.get('name')
            product.price = request.POST.get('price')
            product.company_id = request.POST.get('company')
            product.save()
            return redirect('home')
        else:
            companies = Company.objects.all()
            return render(request, 'engine/edit.html', context={'product': product, "companies": companies})
    except:
        return HttpResponseNotFound('<h2>Product not found</h2>')


def delete(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('home')
    except:
        return HttpResponseNotFound('<h2>Product not found</h2>')


def create_companies():
    if Company.objects.all().count() == 0:
        Company.objects.create(name='Apple')
        Company.objects.create(name='Asus')
        Company.objects.create(name='MSI')

