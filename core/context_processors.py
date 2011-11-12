# -*- encoding: utf-8 -*-

from django.conf import settings
from paginas.models import Banner

def portal(request):
  banners = Banner.objects.filter(publicado=True)
  c = {'ABSOLUTE_URL_PREFIX': settings.ABSOLUTE_URL_PREFIX,'banners':banners}
  return c