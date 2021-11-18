from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, CategoryEditForm, ProductEditForm
from userapp.forms import ShopUserRegisterForm
from userapp.models import ShopUser
from django.contrib.auth.decorators import user_passes_test

from mainapp.models import ProductCategory, Product
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


class UsersListView(LoginRequiredMixin, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'
    context_object_name = 'objects'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UsersListView, self).get_context_data()
        context['title'] = 'админка/пользователи'

        return context

    def get_queryset(self):
        return ShopUser.objects.all()


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка/пользователи'
#
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#
#     return render(request, 'adminapp/users.html', context)


class UserCreateView(CreateView):
    model = ShopUser
    form_class = ShopUserRegisterForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('user_admin:users')


# def user_create(request):
#     title = 'пользователи/создание'
#
#     if request.method == 'POST':
#         user_form = ShopUserRegisterForm(request.POST, request.FILES)
#         if user_form.is_valid():
#             user_form.save()
#             return HttpResponseRedirect(reverse('user_admin:users'))
#     else:
#         user_form = ShopUserRegisterForm()
#
#     context = {
#         'title': title,
#         'user_form': user_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class UserUpdateView(UpdateView):
    model = ShopUser
    form_class = ShopUserAdminEditForm
    template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('user_admin:users')


# def user_update(request, pk):
#     title = 'пользователи/редактирование'
#
#     edit_user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('user_admin:user_update', args=[edit_user.pk]))
#     else:
#         edit_form = ShopUserAdminEditForm(instance=edit_user)
#
#     context = {
#         'title': title,
#         'user_form': edit_form
#     }
#
#     return render(request, 'adminapp/user_update.html', context)


class UserDeleteView(DeleteView):
    model = ShopUser
    context_object_name = 'user_to_delete'
    template_name = 'adminapp/user_delete.html'
    success_url = reverse_lazy('user_admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()

        return HttpResponseRedirect(self.get_success_url())


# def user_delete(request, pk):
#     title = 'пользователи/удаление'
#
#     user = get_object_or_404(ShopUser, pk=pk)
#
#     if request.method == 'POST':
#         user.delete()
#         return HttpResponseRedirect(reverse('user_admin:users'))
#
#     context = {
#         'title': title,
#         'user_to_delete': user
#     }
#
#     return render(request, 'adminapp/user_delete.html', context)


class CategoryListView(ListView):
    model = ProductCategory
    context_object_name = 'objects'
    template_name = 'adminapp/categories.html'


# def categories(request):
#     title = 'админка/категории'
#
#     categories_list = ProductCategory.objects.all()
#
#     content = {
#         'title': title,
#         'objects': categories_list
#     }
#
#     return render(request, 'adminapp/categories.html', content)


class CategoryCreateView(CreateView):
    model = ProductCategory
    form_class = CategoryEditForm
    context_object_name = 'category_form'
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('user_admin:categories')


# def category_create(request):
#     title = 'категория/создание'
#
#     if request.method == 'POST':
#         category_form = CategoryEditForm(request.POST, request.FILES)
#         if category_form.is_valid():
#             category_form.save()
#             return HttpResponseRedirect(reverse('user_admin:categories'))
#     else:
#         category_form = CategoryEditForm()
#
#     context = {
#         'title': title,
#         'category_form': category_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class CategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = CategoryEditForm
    context_object_name = 'category_form'
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('user_admin:categories')


# def category_update(request, pk):
#     title = 'категория/редактирование'
#
#     edit_category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         edit_form = CategoryEditForm(request.POST, request.FILES, instance=edit_category)
#
#         if edit_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse('user_admin:category_update', args=[edit_category.pk]))
#     else:
#         edit_form = CategoryEditForm(instance=edit_category)
#
#     context = {
#         'title': title,
#         'category_form': edit_form
#     }
#
#     return render(request, 'adminapp/category_update.html', context)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    context_object_name = 'category_to_delete'
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('user_admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())


# def category_delete(request, pk):
#     title = 'категория/удаление'
#
#     category = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         category.delete()
#         return HttpResponseRedirect(reverse('user_admin:categories'))
#
#     context = {
#         'title': title,
#         'category_to_delete': category
#     }
#
#     return render(request, 'adminapp/category_delete.html', context)


# class ProductListView(DetailView):
#     model = Product
#     context_object_name = 'objects'
#     template_name = 'adminapp/products.html'
#
#     def get_queryset(self):
#           как здесь достать pk?
#         return Product.objects.filter(category__pk=pk).order_by('name')


def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


# class ProductDetailView(DetailView):
#     model = Product
#     context_object_name = 'objects'
#     template_name = 'adminapp/product_read.html'


def product_read(request, pk):
    title = 'продукт/подробнее'
    product = get_object_or_404(Product, pk=pk)
    context = {'title': title, 'object': product, }

    return render(request, 'adminapp/product_read.html', context)


# class ProductCreateView(UpdateView):
#     model = Product
#     form_class = ProductEditForm
#     context_object_name = 'product_form'
#     template_name = 'adminapp/product_update.html'
#     success_url = reverse_lazy('user_admin:products')


def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('user_admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    context = {'title': title,
               'form': product_form,
               'category': category
               }

    return render(request, 'adminapp/product_update.html', context)


# class ProductUpdateView(UpdateView):
#     model = Product
#     form_class = ProductEditForm
#     context_object_name = 'product_form'
#     template_name = 'adminapp/product_update.html'
#     success_url = reverse_lazy('user_admin:products')


def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('user_admin:products', args=[edit_product.category.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    context = {'title': title,
               'product_form': edit_form,
               'category': edit_product.category
               }

    return render(request, 'adminapp/product_update.html', context)


# class ProductDeleteView(DeleteView):
#     model = Product
#     context_object_name = 'product_to_delete'
#     template_name = 'adminapp/product_delete.html'
#     success_url = reverse_lazy('user_admin:products')
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         self.object.delete()
#         return HttpResponseRedirect(self.get_success_url())
def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()
        return HttpResponseRedirect(reverse('user_admin:products', args=[product.category.pk]))

    context = {'title': title, 'product_to_delete': product}

    return render(request, 'adminapp/product_delete.html', context)
