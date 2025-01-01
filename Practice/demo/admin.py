from django.contrib import admin
from .models import Chef,Dish

# Register your models here.
# class ChefAdmin(admin.ModelAdmin):
#     list_display=('fullname','age','address')
class DishAdmin(admin.ModelAdmin):
    list_display=('name','rating','is_billing','price','chef')
    list_filter=['rating']
admin.site.register(Dish,DishAdmin)
admin.site.register(Chef)