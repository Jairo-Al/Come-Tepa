"""Come_Tepa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from SalesApp.views import home_page, select_page, select_page_prod, product_detail_view
from SessionApp.views import login_page, register_page,logout_page
from SearchApp.views import search_page
from django.conf import settings
from django.conf.urls.static import static
from CartApp.views import cart_home, cart_update


urlpatterns = [
    path('', login_page),
    url(r'^registrate/$', register_page, name='registrate'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^productos-detail/(?P<pk>\d+)/$', product_detail_view),
    url(r'^productos/(?P<slug>[\w-]+)/$', select_page, name='select'),
    url(r'^detail/(?P<slug>[\w-]+)/$', select_page_prod, name='select_prod'),
    url(r'^search/$', search_page, name="search"),
    url(r'^cart/$', cart_home, name='cart'),
    url(r'^cart/update$', cart_update, name='cart_update'),
    path('home/', home_page),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
