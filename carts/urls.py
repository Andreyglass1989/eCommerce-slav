from django.conf.urls import url
from django.views.generic import TemplateView

from .views import cart_basic, cart_update

urlpatterns = [

	url(r'^$', cart_basic, name='home'),
	url(r'^update/$', cart_update, name='update'),
]