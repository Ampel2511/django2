from django.urls import path
from .views import products, product
from django.views.decorators.cache import cache_page

app_name = 'mainapp'
urlpatterns = [
   path('', cache_page(3600)(products), name='main'),
   path('<int:pk>/', cache_page(3600)(products), name='category'),
   path('product/<int:pk>/', cache_page(3600)(products), name='product'),
   path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
