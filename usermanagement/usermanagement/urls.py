
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    # Product routes
    path('products/', views.product_list, name='product_list'),  # List all products
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # Product detail page

    # Payment routes
    path('products/<int:pk>/pay/', views.process_payment, name='process_payment'),  # Payment processing
    path('payment/success/', views.payment_success, name='payment_success'),  # Payment success page
    path('payment/history/', views.payment_history, name='payment_history'),  # Payment history page

    # Authentication routes
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', views.logout, name='logout'),  # Custom logout view

    # Admin routes
    path('admin/', admin.site.urls),  # Django admin interface
]
