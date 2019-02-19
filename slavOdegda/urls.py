"""slavOdegda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static
from Store.views import ClothesListView
from carts.views import cart_basic

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name="main.html"), name='home'),
    url(r'^$', ClothesListView.as_view(), name='home'),
    url(r'^blog/$', TemplateView.as_view(template_name="blog.html"), name='blog'),
    url(r'^contact/$', TemplateView.as_view(template_name="contact.html"), name='contact'),
    url(r'^store/', include('Store.urls', namespace='Store')),
    url(r'^cart/', cart_basic, name='cart'),

    url(r'^admin/', admin.site.urls),

]

urlpatterns +=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)