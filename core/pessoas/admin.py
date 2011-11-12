#!/usr/bin/python
# -*- coding: utf-8 -*

from models import Morador
from django.contrib import admin


class MoradorAdmin(admin.ModelAdmin):
  pass

admin.site.register(Morador, MoradorAdmin)