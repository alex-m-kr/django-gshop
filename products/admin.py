from django.contrib import admin

from products.models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = (
    'name', 'category', 'image', 'description', ('price', 'quantity'))
    readonly_fields = ('price',)
    ordering = ('-quantity',)
    search_fields = ('name',)
