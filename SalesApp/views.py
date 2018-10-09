from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import DetailView, ListView
from .models import restaurantes, productos
import logging

def home_page(request):
    user = request.user
    if request.user.is_authenticated:
        context = {"correo": user}
    return render(request, "main/home.html",context)



def res_list_view(request):

    queryset = restaurantes.objects.all()
    queryset2 = productos.objects.all()
    queryset3 = productos.objects.featured()[0:3]
    queryset4 = productos.objects.featured()[3:7]
    queryset5 = restaurantes.objects.all()[0:3]
    queryset6 = restaurantes.objects.all()[3:7]

    context = {
        'res_list': queryset,
        'prod': queryset2,
        'prod_feat': queryset3,
        'prod_feat2': queryset4,
        'prod_feat3': queryset5,
        'prod_feat4': queryset6,
    }
    return render(request, "main/home2.html",context)

def res_detail_view(request,pk = None, *args, **kwargs):
    #instance = productos.objects.get(pk=pk)
    #instance = get_object_or_404(productos, pk=pk)
    #qs = productos.objects.filter(pk=pk)
    #if qs.exists() and qs.count() ==1:
    #    instance = qs.first()
    #else:
    #    raise Http404("Producto no existe")
    instance = productos.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Producto no existe")
    context = {
        'object':instance,
    }
    return render(request, "main/productos.html", context)

def res_slug_view(request, *args, **kwargs):
    slug = kwargs.get("slug")
    try:
        instance = restaurantes.objects.get(slug=slug)
    except restaurantes.DoesNotExist:
        raise Http404("Not Found")
    except restaurantes.MultipleObjectsReturned:
        qs = restaurantes.objects.filter(slug=slug)
        instance = qs.first()
    except:
           raise  Http404("Error")
    context = {
        'object':instance,
    }
    return render(request, "main/slug.html", context)


#class res_slug_view(DetailView):
    #    queryset = restaurantes.objects.all()
    #template_name = "main/slug.html"
    #
    #def get_object(self, *args, **kwargs):
    #   request = self.request
    #   slug = self.kwargs.get("slug")
    #   try:
    #       instance = restaurantes.objects.get(slug= slug)
    #   except restaurantes.DoesNotExist:
    #       raise Http404("Not Found")
    #   except restaurantes.MultipleObjectsReturned:
    ##       qs = restaurantes.objects.filter(slug=slug)
    #      instance = qs.first()
    #   except:
    #       raise  Http404("Error")
#   return instance
