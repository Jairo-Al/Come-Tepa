from django.shortcuts import render, Http404
from .models import restaurantes, productos

def home_page(request):
    queryset_0 = restaurantes.objects.all()[0:3]
    queryset_1 = restaurantes.objects.all()[3:7]

    context = {
        'prod_feat_0': queryset_0,
        'prod_feat_1': queryset_1,
    }
    return render(request, "main/home.html",context)


def select_page(request, *args, **kwargs):
    slug = kwargs.get("slug")
    try:
        instance = restaurantes.objects.get(slug=slug)
    except restaurantes.DoesNotExist:
        raise Http404()
    except restaurantes.MultipleObjectsReturned:
        qs = restaurantes.objects.filter(slug=slug)
        instance = qs.first()
    except:
           raise  Http404()
    prod = productos.objects.get_by_res(instance)
    context = {
        'queryset': prod,
    }
    return render(request, "main/platillos.html", context)
