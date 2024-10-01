from django.contrib import admin
from .models import Product, Payment

# Register the Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # Display these fields in the product list
    search_fields = ('name',)  # Allow search by product name
    list_filter = ('price',)  # Add filter by price in the admin panel

# Register the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'transaction_id', 'timestamp')  # Display key fields
    search_fields = ('transaction_id', 'user__username')  # Allow search by transaction ID and username
    list_filter = ('timestamp', 'amount')  # Add filter by date and amount
