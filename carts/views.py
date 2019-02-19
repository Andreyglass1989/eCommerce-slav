# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def cart_basic(request):
	cart_id = request.session.get("cart_id", None)
	if cart_id is None: #and isinstance(cart_id, int):
		print("create new cart id")
		request.session["cart_id"] = 12

	else:
		print("Cart ID exists")
	return render(request, "carts/home.html", {})