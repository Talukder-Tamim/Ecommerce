from django.shortcuts import render
from . models import Product, Category


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

