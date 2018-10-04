from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import restaurantes, productos


def home_page(request):
    user = request.user
    if request.user.is_authenticated:
        context = {"correo": user}
    return render(request, "main/home.html",context)



def res_list_view(request):
    queryset = restaurantes.objects.all()
    queryset2 = productos.objects.all()
    context = {
        'res_list': queryset,
        'feat_prod': queryset2
    }
    return render(request, "main/home2.html",context)
