from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_technician:
                login(request, user)
                return redirect('technician')
            else:
                msg = 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


from django.contrib.auth.decorators import login_required
from .forms import TechnicianProfileForm
from .models import TechnicianProfile, utechnicianProfile
from products.models import Product

@login_required
def update_profile(request):
    try:
        technician_profile = request.user.technicianprofile
    except TechnicianProfile.DoesNotExist:
        technician_profile = TechnicianProfile(user=request.user)
        technician_profile.save()

    if request.method == 'POST':
        form = TechnicianProfileForm(request.POST, instance=technician_profile)
        if form.is_valid():
            form.save()
            return redirect('technician')  # Redirect to the technician's profile page
    else:
        form = TechnicianProfileForm(instance=technician_profile)
    return render(request, 'update_profile.html', {'form': form})


@login_required  # শুধুমাত্র লগইন ইউজারই অ্যাক্সেস পাবে
def admin(request):
    product_count = Product.objects.count()
    technician_count = TechnicianProfile.objects.count()
    context = {
        'product_count': product_count,
        'technician_count': technician_count,
    }
    return render(request, 'admin.html', context)


def customer(request):
    return render(request, 'customer.html')


def technician(request):
    return render(request, 'technician.html')


def technician_list(request):
    technicians = TechnicianProfile.objects.all()
    context = {'technicians': technicians}
    return render(request, 'technician_list.html', context=context)


# views.py

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponse


def logout_view(request):
    logout(request)
    return redirect('login_view')  # Redirect to the login page after logging out


from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_technician_profile(sender, instance, created, **kwargs):
    if created and instance.is_technician:
        TechnicianProfile.objects.create(user=instance)


from django.shortcuts import render
from .models import TechnicianProfile
from django.contrib.auth.decorators import login_required


@login_required
def view_utechnician_profile(request, id):
    technicians = TechnicianProfile.objects.get(id=id)
    context = {'technicians': technicians}
    return render(request, 'utechnician_profile.html', context=context)




from django.shortcuts import render
from .models import TechnicianProfile
from django.contrib.auth.decorators import login_required


@login_required
def view_technician_profile(request):
    try:
        technician_profile = request.user.technicianprofile
    except TechnicianProfile.DoesNotExist:
        technician_profile = None

    return render(request, 'technician_profile.html', {'technician_profile': technician_profile})

# from django.shortcuts import render, get_object_or_404
# from .models import utechnicianProfile

# def view_utechnician_profile(request, technician_id):
#     # Retrieve the technician object from the database, or return a 404 error if not found
#     technician = get_object_or_404(utechnicianProfile, id=technician_id)
#     context = {
#         'technician': technician,
#         'technician_id': technician_id,
#     }
#     return render(request, 'view_utechnician_profile.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from products.forms import ProductForm
from products.models import Product

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('adminpanel:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('adminpanel:product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

