from django.conf.urls import url
from django.views.generic import TemplateView

from .views import ClothesDetailView

urlpatterns = [

#ListView

	# url(r'^detail/$', TemplateView.as_view(template_name="detailView.html"), name='detail'),

	url(r'^detail/(?P<dress_id>\d+)/$', ClothesDetailView.as_view(), name='clothes_detail'),


#DetailView
	# url(r'^project-house/(?P<project_id>\d+)/$$', detail_gallery, name='detail_project_house'),
	# url(r'^design-room/(?P<design_room_id>\d+)/$$', DetailGalleryDesignRoom, name='detail_design_room'),
	# url(r'^project-cottage/(?P<project_cottage_id>\d+)/$$', DetailGalleryProjectCottage, name='detail_project_cottage'),
	# url(r'^reconstruction-object/(?P<reconst_obj_id>\d+)/$$', DetailGalleryReconstructionObject, name='detail_reconst_object'),
	# url(r'^landscape-design/(?P<landscape_design>\d+)/$$', DetailGalleryLandscapeDesign, name='detail_reconst_object'),
]