from django.shortcuts import render

# adminpanel/views.py

from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from products.forms import ProductForm  # তুমি যদি ফর্ম ব্যবহার করো

def admin_dashboard(request):
    products = Product.objects.all()
    return render(request, 'admin.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('adminpanel:product_list')
    return render(request, 'product_form.html', {'form': form})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('adminpanel:product_list')
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('adminpanel:product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})
