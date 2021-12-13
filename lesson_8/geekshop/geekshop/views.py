from django.shortcuts import render

from mainapp.models import Product


def main(request):
    title = 'главная'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    products = Product.objects.filter(is_active=True).select_related('category')[:4]
    context = {
        'title': title,
        'links_page': links_page,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context=context)


def contacts(request):
    title = 'контакты'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    context = {
        'title': title,
        'links_page': links_page,
    }
    return render(request, 'geekshop/contact.html', context=context)

