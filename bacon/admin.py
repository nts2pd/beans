from django.contrib import admin

from .models import Customer, Order

class OrderInline(admin.TabularInline):
    model = Order
    extra = 3

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,      {'fields': ['first_name']}),
        (None,      {'fields': ['last_name']}),
        ('Favorite Food', {'fields': ['favorite_food'], 'classes': ['collapse']}),
    ]
    inlines = [OrderInline]
    list_display = ('first_name', 'last_name', 'favorite_food', 'order_time')
    search_fields = ['first_name']

admin.site.register(Customer, CustomerAdmin)
