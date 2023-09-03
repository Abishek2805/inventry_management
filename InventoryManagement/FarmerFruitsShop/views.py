from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from FarmerFruitsShop.models import Product, Location, Product_Movement


# Create your views here.
def home(request):
    return render(request,'home.html')


def signin_fun(request):
    if request.method == "POST":
        name = request.POST['txtname']
        email = request.POST['txtemail']
        password = request.POST['txtpassword']
        if User.objects.filter(Q(username=name) | Q(email=email)).exists():
            data = {"msg": True}
            return render(request, 'signin.html', data)
        else:
            u1 = User.objects.create_superuser(username=name, password=password, email=email)
            u1.save()
            # return render(request,'login.html')
            return redirect('login')
    return render(request, 'signin.html', {'msg': False})


def login_fun(request):
    if request.method == "POST":
        name = request.POST['txtname']
        password = request.POST['txtpassword']
        user = authenticate(username=name, password=password)

        if user is not None:
            if user.is_superuser:
                return render(request,'home1.html')
            else:
                data = {"msg": True}
                return render(request, 'login.html', data)
        else:
            data = {"msg": True}
            return render(request, 'login.html', data)
    else:
        return render(request, 'login.html', {'msg': False})


def product_fun(request):
    s=Product.objects.all()
    return render(request, 'product.html', {'fruit': s})



def location_fun(request):
    l=Location.objects.all()
    return render(request,'location.html',{'location':l})


def movement_fun(request):
    m = Product_Movement.objects.all()
    return render(request,'movement.html',{'data':m})



def logout_fun(request):
    return render(request,'home.html')


def add_fruit(request):

    if request.method == 'POST':
        fruit_name = request.POST.get('txtfruit')
        s1 = Product(name=fruit_name)
        s1.save()
        return redirect('product')
    return render(request,'add_fruit.html')


def edit_fruit(request, id):
    s1 = Product.objects.get(id=id)
    if request.method == 'POST':
        name1 = request.POST.get('txtfruit')
        s1.name=name1
        s1.save()
        return redirect('product')
    return render(request, 'edit_fruit.html', {'name': s1})


def add_location(request):
    if request.method == 'POST':
        location_name = request.POST.get('txtlocation')
        s1 = Location(l_name=location_name)
        s1.save()
        return redirect('location')
    return render(request, 'add_location.html')


def edit_location(request,id):
    s1 = Location.objects.get(id=id)
    if request.method == 'POST':
        name1 = request.POST.get('txtlocation')
        s1.l_name = name1
        s1.save()
        return redirect('location')
    return render(request, 'edit_location.html', {'name': s1})


def edit_movement(request,id):
    m = Location.objects.all()
    n = Product.objects.all()
    s1 = Product_Movement.objects.get(id=id)
    if request.method == 'POST':
        product = request.POST.get('ddllocation1')
        from_loc = request.POST.get('ddllocation2')
        to_loc = request.POST.get('ddllocation3')
        quantity = request.POST.get('txtnum1')
        assign = request.POST.get('txtaname')
        print(product,from_loc,to_loc)
        product_name = Product.objects.get(name=product)
        from_location = Location.objects.get(l_name=from_loc)
        to_location = Location.objects.get(l_name=to_loc)
        data=Product_Movement()
        s1.f_name = product_name
        s1.from_location = from_location
        s1.to_location = to_location
        s1.p_name = assign
        s1.quantity = int(quantity)
        s1.save()
        return redirect('movement')
    return render(request, 'edit_movement.html', {'place': m,'data':n})


def add_movement(request):
    m = Location.objects.all()
    n = Product.objects.all()
    s1 = Product_Movement.objects.all()
    if request.method == 'POST':
        product = request.POST.get('ddllocation1')
        from_loc = request.POST.get('ddllocation2')
        to_loc = request.POST.get('ddllocation3')
        quantity = request.POST.get('txtnum1')
        assign = request.POST.get('txtaname')
        print(product,from_loc,to_loc)
        product_name = Product.objects.get(name=product)
        from_location = Location.objects.get(l_name=from_loc)
        to_location = Location.objects.get(l_name=to_loc)
        data=Product_Movement()
        data.f_name = product_name
        data.from_location = from_location
        data.to_location = to_location
        data.p_name = assign
        data.quantity = int(quantity)
        data.save()
        return redirect('movement')
    return render(request, 'add_movement.html', {'place': m,'data':n})


def delete_movement(request,id):
    s1 = Product_Movement.objects.get(id=id)
    s1.delete()
    return render(request, 'movement.html')