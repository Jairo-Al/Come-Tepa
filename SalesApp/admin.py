from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import productos,restaurantes


User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display = ('email','nombre','telefono')
    list_filter = ('superuser','active')
    class Meta:
        model = User

class SalesAdmin(admin.ModelAdmin):
    list_display =('__str__','slug')
    class Meta:
        model = restaurantes

class productsAdmin(admin.ModelAdmin):
    list_display =('platillo','nombre_res','featured')
    class Meta:
        model = productos


admin.site.register(productos, productsAdmin)
admin.site.register(restaurantes, SalesAdmin)
admin.site.register(User,UserAdmin)
