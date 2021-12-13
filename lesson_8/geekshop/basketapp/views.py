from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.db.models import F, Q

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket(request):
    title = 'корзина'
    links_page = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'товары'},
        {'href': 'contacts', 'name': 'контакты'},
    ]
    basket = request.user.basket.all()

    context = {
        'title': title,
        'links_page': links_page,
        'basket': basket,
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)

    basket[0].quantity = F('quantity') + 1
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, quantity):
    if request.is_ajax():
        quantity = int(quantity)
        new_basket = Basket.objects.get(pk=int(pk))
        if quantity > 0:
            new_basket.quantity = quantity
            new_basket.save()
        else:
            new_basket.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')
        title = 'корзина'
        links_page = [
            {'href': 'main', 'name': 'домой'},
            {'href': 'products:index', 'name': 'товары'},
            {'href': 'contacts', 'name': 'контакты'},
        ]
        context = {
            'title': title,
            'links_page': links_page,
            'basket': basket_items,
        }
        result = render_to_string('basketapp/includes/basket_row.html', context)
        return JsonResponse({'result': result})
