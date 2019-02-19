# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Cart
# Create your views here.

def cart_basic(request):
	cart_obj = Cart.objects.new_or_get(request)
	return render(request, "carts/home.html", {})