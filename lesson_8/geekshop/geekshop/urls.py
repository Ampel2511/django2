"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the includes() function: from django.urls import includes, path
    2. Add a URL to urlpatterns:  path('blog/', includes('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import main, contacts
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cache_page(3600)(main), name='main'),
    path('', include('social_django.urls', namespace='social')),
    path('contacts/', cache_page(3600)(contacts), name='contacts'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('userapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('user_admin/', include('adminapp.urls', namespace='user_admin')),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
