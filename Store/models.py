# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.Simple




class Product(models.Model):
	class Meta:
		verbose_name = "СЛАВЯНСКИЕ ПЛАТЬЯ"
		verbose_name_plural = "Платья в славянском стиле"

	name = models.CharField(verbose_name="Название", max_length=255)
	material = models.CharField(verbose_name="Материал", max_length=255)
	color = models.CharField(verbose_name="Цвет", max_length=255)
	availability = models.BooleanField(verbose_name="в наличие", default=True)
	price = models.FloatField(verbose_name="Цена, грн.")
	description = models.TextField(verbose_name="Описание")
	image = models.ImageField(upload_to = 'img/odegda')
	date_add = models.DateTimeField(verbose_name="Дата добавления", auto_now=True)

	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("Store:clothes_detail", kwargs={"dress_id": self.id })


	def image_img(self):
		if self.image:
		    return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
		else:
		    return '(Нет изображения)'

	image_img.short_description = 'Картинка'
	image_img.allow_tags = True




class GalleryDress(models.Model):
    class Meta:
        verbose_name = "ГАЛЕРЕЯ ДЛЯ ПЛАТЬЕВ"
        verbose_name_plural = "Изображения для славянских платьев"

    dress = models.ForeignKey(Product)
    img = models.ImageField(upload_to = 'img/odegda/detail')


    # def __unicode__(self):
    #     return self.dress

    def image_img(self):
        if self.img:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
