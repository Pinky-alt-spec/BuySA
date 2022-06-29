import json

from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from home.forms import SearchForm
from home.models import *
from product.models import *


def index(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product_featured = Product.objects.all().order_by('?')[:16]
    product_best_seller = Product.objects.all().order_by('id')[:6]
    product_popular = Product.objects.all().order_by('id')[:6]
    product_new_arrival = Product.objects.all().order_by('-id')[:16]
    product_top_related = Product.objects.all().order_by('?')[:9]
    bottom_product_top_related = Product.objects.all().order_by('?')[:3]
    product_featured_item = Product.objects.all().order_by('-id')[:1]
    special_offer = Product.objects.all().order_by('id')[:3]
    best_bottom = Product.objects.all().order_by('?')[:3]

    page = "home"

    context = {
        'page': page,
        'setting': setting,
        'category': category,
        'product_featured': product_featured,
        'product_best_seller': product_best_seller,
        'product_popular': product_popular,
        'product_new_arrival': product_new_arrival,
        'product_top_related': product_top_related,
        'bottom_product_top_related': bottom_product_top_related,
        'product_featured_item': product_featured_item,
        'special_offer': special_offer,
        'best_bottom': best_bottom,
    }
    return render(request, 'index.html', context)


def about(request):
    setting = Setting.objects.get(pk=1)

    context = {
        'setting': setting
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.subject = form.cleaned_data['subject']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent, we will be in touch with you shortly")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get(pk=1)
    form = ContactForm

    context = {
        'setting': setting,
        'form': form,
    }
    return render(request, 'contact.html', context)


def category_products(request, id, slug):
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_products.html', context)


def search(request):
    query = request.GET.get('query')
    product = Product.objects.filter(title__icontains=query)

    context = {
        'product': product,
    }
    return render(request, 'search_products.html', context)


def product_detail(request, id, slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    comments = Comment.objects.filter(product_id=id, status="True")

    context = {
        'category': category,
        'product': product,
        'images': images,
        'comments': comments,
    }
    return render(request, 'product_detail.html', context)


