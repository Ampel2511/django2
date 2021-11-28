import random

from django.shortcuts import render, get_object_or_404

from mainapp.models import ProductCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def get_hot_product():
    product = Product.objects.all()
    return random.sample(list(product), 1)[0]


def get_same_product(hot_product):
    same_product = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_product


def products(request, pk=None, page=1):
    title = 'каталог'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    links_menu = ProductCategory.objects.all()
    products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')
    hot_product = get_hot_product()
    same_product = get_same_product(hot_product)

    if pk is not None:
        if pk == 0:
            category = {'name': 'Все'}
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        context = {
            'title': title,
            'links_menu': links_menu,
            'links_page': links_page,
            'products': products_paginator,
            'category': category,
            'hot_product': hot_product,
            'same_product': same_product,
        }
        return render(request, 'mainapp/category_products.html', context=context)
    context = {
        'title': title,
        'links_menu': links_menu,
        'links_page': links_page,
        'products': products,
        'hot_product': hot_product,
        'same_product': same_product,
    }
    return render(request, 'mainapp/products.html', context=context)


def product(request, pk):
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    product = get_object_or_404(Product, pk=pk)
    title = f'{product.name}'
    context = {
        'title': title,
        'links_page': links_page,
        'product': product,
    }

    return render(request, 'mainapp/product.html', context=context)
