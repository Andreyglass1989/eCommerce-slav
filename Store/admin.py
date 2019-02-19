# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Store.models import Product, GalleryDress

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_img' ]
    list_editable = ("price",)
    list_filter = ("date_add",) #"name",
    search_fields = ("name",)

class GalleryAdmin(admin.ModelAdmin):
	list_display = ("dress", "image_img")


admin.site.register(Product, ProductAdmin)
admin.site.register(GalleryDress, GalleryAdmin)
admin.site.site_header = u"Славянская одежда"