from django.shortcuts import render, Http404, get_object_or_404, redirect
from .models import restaurantes, productos, pedido
from SessionApp.models import User
from CartApp.models import Cart
from django.views.generic.detail import DetailView
from .forms import AddForm
from django.contrib.auth.decorators import login_required


def home_page(request):
    if request.user.is_authenticated:
        queryset_0 = restaurantes.objects.all()[0:3]
        queryset_1 = restaurantes.objects.all()[3:7]

        context = {
            'prod_feat_0': queryset_0,
            'prod_feat_1': queryset_1,
        }
        return render(request, "main/home.html",context)
    else:
        return redirect('/')


def select_page(request, *args, **kwargs):
    if request.user.is_authenticated:
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
        res = restaurantes.objects.get(nombre_res__icontains=instance)
        prod = productos.objects.get_by_res(instance)
        context = {
            'queryset': prod,
            'res': res,
        }
        return render(request, "main/platillos.html", context)
    else:
        return redirect('/')

def select_page_prod(request, *args, **kwargs):
    if request.user.is_authenticated:
        userObj = User.objects.get(email=request.user)
        fdata = userObj.domicilio
        a = User.objects.filter(email=request.user).values()[0]
        correo = a['email']
        nombre = a['nombre']
        print(correo)
        print("aaaaaaaa   ",a)
        slug = kwargs.get("slug")
        form = AddForm(fdata, request.POST or None )
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

        if request.method == 'POST':  # If the form has been submitted...
            if form.is_valid():  # All validation rules pass
                print("-----____----",form.cleaned_data['cantidad'])
                cantidad = form.cleaned_data['cantidad']
                total = cantidad * prod.precio
                domicilio = form.cleaned_data['domicilio']
                observacion = form.cleaned_data['observacion']
                platillo = prod.platillo
                restaurant = prod.nombre_res
                usuario = request.user
                print("el usuario : {}, pidio: {} {} {} por un total de : {} del restaurante {} al domicilio {}".format(usuario,cantidad,platillo,observacion,total,restaurant, domicilio))
                new_pedido = pedido.objects.create(
                    usuario=correo,
                    nombre = nombre,
                    platillo=platillo,
                    cantidad=cantidad,
                    total=total,
                    domicilio=domicilio,
                    observacion=observacion,
                    nombre_res=restaurant,
                )
                return redirect('/carrito')
        else:
            pass
        context = {
            'item': prod,
            'cart': cart_obj,
            'form': form
        }
        return render(request, "main/cart.html", context)
    else:
        return redirect('/')

def product_detail_view(request, pk=None, *args, **kwargs):
    if request.user.is_authenticated:
        instance = productos.objects.get_by_id(pk)
        if instance is None:
            raise Http404("Product doesn't exist")
        context = {
            'item': instance
        }
        return render(request, "main/cart.html", context)
    else:
        return redirect('/')

