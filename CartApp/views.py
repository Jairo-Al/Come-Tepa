from django.shortcuts import render, redirect,get_object_or_404
from .models import Cart
from SalesApp.models import productos, pedido, restaurantes
from django.db.models import Q
from django.core.mail import send_mail
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from SessionApp.models import User


def cart_create(request, user=None):
    if request.user.is_authenticated:
        cart_obj = Cart.objects.create(user=None)
        print("New cart created")
        return cart_obj
    else:
        return redirect('/')


def cart_home(request):
    if request.user.is_authenticated:
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        print(cart_obj)
        return render(request, "main/cart.html", {})
    else:
        return redirect('/')


def cart_update(request):
    if request.user.is_authenticated:
        product_id = 1
        product_obj = productos.objects.get(id = product_id)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in Cart.objects.all():
             #cart_obj.products.remove(product_obj)
            print("its in")
        else:
            print("its not in")
            #cart_obj.product.add(product_obj)
        return redirect(product_obj.get_url_prod())
    else:
        return redirect('/')

def carrito(request):
    if request.user.is_authenticated:
        pedidos_usuario = pedido.objects.filter(usuario=request.user)
        print(pedidos_usuario)
        total_ped = 0
        for i in pedidos_usuario:
            total_ped += i.total
        context = {
            'pedidos': pedidos_usuario,
            'total_ped': total_ped
        }
        request.session['cantidad'] = pedidos_usuario.count()
        return render(request, "main/final_cart.html", context)
    else:
        return redirect('/')

def delete_func(request, id):
    if request.user.is_authenticated:
        pedido.objects.filter(id=id).delete()
        return redirect('/carrito')
    else:
        return redirect('/')

def clear_func(request):
    if request.user.is_authenticated:
        a = User.objects.filter(email=request.user).values()[0]
        domicilio = a['domicilio']
        nombre = a['nombre']
        telefono = a['telefono']
        pedidos_usuario = pedido.objects.filter(usuario=request.user)
        res_dist = pedidos_usuario.order_by().values('nombre_res').distinct()
        for res in res_dist:
            emailRes = res['nombre_res']
            res = restaurantes.objects.filter(nombre_res__icontains=emailRes)
            for r in res:
                Res_email = r.correo
                pedidos_res = pedidos_usuario.filter(nombre_res__icontains=emailRes)
                total_ped = 0
                for i in pedidos_res:
                    total_ped += i.total
                html_message = loader.render_to_string('components/table.html',{
                        'pedidos': pedidos_res,
                        'total_ped': total_ped,
                        'nombre': nombre,
                        'domicilio': domicilio,
                        'telefono': telefono,
                        })
                send_mail('Nuevo pedido',
                         'Te llego un pedido de :',
                         'cometepa@gmail.com',
                         [Res_email],
                         fail_silently=True,
                         html_message=html_message
                        )
        pedido.objects.filter(usuario=request.user).delete()
        return redirect('/carrito')
    else:
        return redirect('/')