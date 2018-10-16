from django.shortcuts import render, Http404, get_object_or_404
from .models import restaurantes, productos
from CartApp.models import Cart
from django.views.generic.detail import DetailView
from .forms import AddForm

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


def select_page_prod(request, *args, **kwargs):
    form = AddForm(request.POST or None)
    slug = kwargs.get("slug")
    try:
        instance = productos.objects.get(slug=slug)
        data = instance.platillo
    except productos.DoesNotExist:
        raise Http404()
    except productos.MultipleObjectsReturned:
        qs = productos.objects.filter(slug=slug)
        data = qs.first()
    except:
           raise  Http404()
    print(data)
    prod = productos.objects.get(platillo=data)
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    print(prod)
    print(cart_obj)
    context = {
        'item': prod,
        'cart': cart_obj,
        'form': form
    }
    return render(request, "main/cart.html", context)


def product_detail_view(request, pk=None, *args, **kwargs):
    instance = productos.objects.get_by_id(pk)
    if instance is None:
        raise Http404("Product doesn't exist")
    context = {
        'item': instance
    }
    return render(request, "main/cart.html", context)

