from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render
from home.models import *
from product.models import *

# Create your views here.
def index(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    
    page = "home"
    
    context = {
        'category': category,
        'setting': setting,
        'page': page,
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
    # category = Category.objects.all()
    products = Product.objects.filter(category_id=id)

    context = {
        # 'category': category,
        'products': products,
    }
    return HttpResponse(products)