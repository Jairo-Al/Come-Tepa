from django.db import models
from django.conf import settings
from SalesApp.models import productos
from django.db.models.signals import m2m_changed, pre_save

User = settings.AUTH_USER_MODEL
# Create your models here.

class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            print('Cart ID exists')
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            cart_obj = Cart.objects.new_cart(user=request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new_cart(self, user=None):
        print("------",user)
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    product     = models.ManyToManyField(productos, blank=True)
    subtotal = models.DecimalField(default=0.00, max_digits=50, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=50,decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.product.all()
        total = 0
        for x in products:
            total += x.precio
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.product.through)

def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = instance.subtotal + 10
    else:
        instance.total = 0

pre_save.connect(pre_save_cart_receiver,sender = Cart)


