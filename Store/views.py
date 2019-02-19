# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from carts.models import Cart


class ClothesListView(ListView):
	model = Product
	template_name = "main.html"

	def get_context_data(self, **kwargs):
		context = super(ClothesListView, self).get_context_data(**kwargs)
		dress = Product.objects.all().order_by("-date_add")
		context = {
			"dress": dress,
		}
		return context


class ClothesDetailView(DetailView):
	model = Product
	pk_url_kwarg = "dress_id"
	template_name = "detailView.html"

	def get_context_data(self, *args, **kwargs):
		obj = super(ClothesDetailView, self).get_context_data(*args, **kwargs)
		# print(self.kwargs['dress_id'])
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		items = GalleryDress.objects.filter(dress_id=self.kwargs['dress_id'])
		# print(context)
		context = {
			"items": items,
			"object": obj,
			"cart": cart_obj
		}
		# print(context)
		# print(context['items'])
		# for item in context['items']:
		# 	print(item)
		return context