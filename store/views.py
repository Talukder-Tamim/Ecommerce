from django.shortcuts import render, redirect
from . models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages


def index(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {'products': products, 'categories': categories}
	return render(request, 'index.html', context)


def category_post(request, ctg_name):
    category_obj = Category.objects.get(name=ctg_name)
    category_post = Product.objects.filter(category=category_obj)
    context = {'categories': category_post}
    return render(request, 'category_post.html', context)


def add_cart(request):
    if request.method == "POST":
        product = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print(request.session['cart'])

        return redirect('index')
    else:
        return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        values = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone': phone
        }

        if password1 == password2:
            if Customer.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists...')
                data = {'values': values}
                return render(request, 'signup.html', data)
            else:
                customer = Customer.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    email = email,
                    phone = phone,
                    password = password1
                )
                customer.password = make_password(customer.password)
                customer.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password not matched..')
            data = {
                'values': values
            }
            return render(request, 'signup.html', data)
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password1']
        
        customer = Customer.objects.get(email=email)
        
        if customer:
            customer_obj = check_password(password, customer.password)
            if customer_obj:
                request.session['customer_id'] = customer.id 
                request.session['email'] = customer.email

                return redirect('index')
            else:
                messages.info(request, 'Email or password doesnt exist!')
                return redirect('login')
        else:
            messages.info(request, 'Email or password doesnt exist!')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logout(request):
    request.session.clear()
    return redirect('login')

