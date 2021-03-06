# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from Store.models import Product
from .models import Cart
# Create your views here.

def cart_basic(request):
	cart_obj, new_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {"cart": cart_obj})


def cart_update(request):
	print(request.POST)
	product_id = request.POST.get("product")
	if product_id is not None:
		try:
			product_obj =Product.objects.get(id=product_id)
		except Product.DoesNotExist:
			print("Show message to user product is gone?")
			return redirect("cart:home")
		cart_obj, new_obj = Cart.objects.new_or_get(request)
		if product_obj in cart_obj.products.all():
			cart_obj.products.remove(product_obj)
		else:
			cart_obj.products.add(product_obj) #cart_obj.products.add(1)
		# return redirect("Store:clothes_detail")
		# return redirect(product_obj.get_absolute_url())
	request.session["cart_items"] = cart_obj.products.count()
	return redirect("cart:home")