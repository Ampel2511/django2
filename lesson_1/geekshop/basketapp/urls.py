from django.urls import path
from .views import basket, add, remove, basket_edit

app_name = 'basketapp'
urlpatterns = [
    path('', basket, name='view'),
    path('add/<int:pk>/', add, name='add'),
    path('remove/<int:pk>/', remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basket_edit, name='edit'),
]
