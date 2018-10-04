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


admin.site.register(productos)
admin.site.register(restaurantes)
admin.site.register(User,UserAdmin)
