from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('tests/', views.tests, name='tests'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('policy/', views.policy, name='policy'),
    path('send_email/', views.send_email, name='sendEmail')
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
