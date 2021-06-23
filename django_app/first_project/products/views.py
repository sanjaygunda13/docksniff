from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
from products.forms import NewUserForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm 
from products.models import products
from django.contrib.auth.models import User

from django.contrib import messages #import messages

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return render(request,"home.html", context={'data':["no value"]})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                product = list_products(user)
                return render(request,"home.html",context={'data':product})
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def new_product(request):
    if request.method == 'POST':
        print(request.user)
        print(request.POST['product'])
        abc=""
        if len(request.POST['product'])>0:
            try:
                prod =products()
                prod.products_name = request.POST['product']
                prod.user = User.objects.get(username=request.user)
                prod.save()
            except Exception as error:
                print (error)
        
            ### will list product
        product=list_products(request.user)


                
        return render(request,"home.html",context={'data':product})


def list_products(user):
    abc= list(products.objects.filter(user=user).values('products_name'))
    product=[]
    if len(abc) < 1:
        product.append("no value")
    else:
        for i in abc:
            product.append(i['products_name'])
    return product
