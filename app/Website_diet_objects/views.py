from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product, NutritionalInfo, ProductConsumption
from .forms import ProductForm, NutritionalInfoForm, ProductConsumptionForm

#Products
def return_all_products(request):
    products = Product.objects.all()
    return render(request, "products_info/product.html", {'products': products})

def return_product(request, id):
    products = Product.objects.filter(id=id)
    return render(request, "products_info/product.html", {'products': products})

def create_product(request):
    create_form = ProductForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "products_info/product_new.html", {'product_new': create_form})

def edit_product(request, id):
    instance_object = get_object_or_404(Product, pk=id)
    edit_form = ProductForm(request.POST or None, request.FILES or None, instance=instance_object)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "products_info/product_new.html", {'product_new': edit_form})

def delete_product(request, id):
    instance_object = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "products_info/product_delete.html", {'product_delete': instance_object})

#Nutritions
def return_all_nutritional_info(request):
    infos = NutritionalInfo.objects.all()
    return render(request, "products_info/nutritional_info.html", {'infos': infos})

def return_nutritional_info(request, id):
    nutritional_info = NutritionalInfo.objects.filter(id=id)
    return render(request, "products_info/nutritional_info.html", {'nutritional_info': nutritional_info})

def create_nutritional_info(request):
    create_form = NutritionalInfoForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "products_info/nutritional_info_new.html", {'nutritional_info_new': create_form})

def edit_nutritional_info(request, id):
    profile = get_object_or_404(NutritionalInfo, pk=id)
    edit_form = NutritionalInfoForm(request.POST or None, request.FILES or None, instance=profile)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "products_info/nutritional_info_new.html", {'nutritional_info_new': edit_form})

def delete_nutritional_info(request, id):
    instance_object = get_object_or_404(NutritionalInfo, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "products_info/nutritional_info_delete.html", {'nutritional_info_delete': instance_object})

#Consumptions
def return_all_product_consumptions(request):
    consumptions = ProductConsumption.objects.all()
    return render(request, "products_info/consumptions.html", {'consumptions': consumptions})


def return_product_consumptions(request, id):
    consumptions = ProductConsumption.objects.filter(id=id)
    return render(request, "products_info/consumptions.html", {'consumptions': consumptions})

def create_product_consumptions(request):
    create_form = ProductConsumptionForm(request.POST or None, request.FILES or None)

    if create_form.is_valid():
        create_form.save()

    return render(request, "products_info/consumptions_new.html", {'consumptions_new': create_form})

def edit_product_consumptions(request, id):
    profile = get_object_or_404(ProductConsumption, pk=id)
    edit_form = ProductConsumptionForm(request.POST or None, request.FILES or None, instance=profile)

    if edit_form.is_valid():
        edit_form.save()

    return render(request, "products_info/consumptions_new.html", {'consumptions_new': edit_form})

def delete_product_consumptions(request, id):
    instance_object = get_object_or_404(ProductConsumption, pk=id)

    if request.method == "POST":
        instance_object.delete()
        return redirect(new_profile)

    return render(request, "products_info/consumptions_delete.html", {'consumptions_delete': instance_object})