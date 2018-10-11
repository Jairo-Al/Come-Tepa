from django.shortcuts import render
from django.shortcuts import render, Http404
from SalesApp.models import restaurantes, productos
from django.db.models import Q

# Create your views here.
def search_page(request):

    context = dict()
    method_dict = request.GET
    query = method_dict.get('q',None)
    if query is not None:
        busquedas = Q(platillo__icontains=query) | Q(descripcion__icontains=query)
        query_search_p = productos.objects.filter(busquedas).distinct()

    if query is not None:
        busquedas = Q(nombre_res__icontains=query) | Q(descripcion__icontains=query)
        query_search_r = restaurantes.objects.filter(busquedas).distinct()

    query_search_f = restaurantes.objects.all()

    print("------",query_search_p.count())
    print("------", query_search_r.count())
    if query_search_p.count() > 0:
        context['queryset_p'] = query_search_p
    if query_search_r.count() > 0:
        context['queryset_r'] = query_search_r
    if query_search_p.count() == 0 and query_search_r.count() == 0:
        context['queryset_f'] = query_search_f
    return render(request, "main/search.html",context)