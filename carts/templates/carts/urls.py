from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ClothesDetailView

urlpatterns = [
	url(r'^detail/(?P<dress_id>\d+)/$', ClothesDetailView.as_view(), name='clothes_detail'),
]