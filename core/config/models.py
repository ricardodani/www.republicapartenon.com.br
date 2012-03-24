# -*- encoding: utf-8 -*-

'''Config Module'''

from django.db import models

from config.choices import *

class Configuracao(models.Model):
    '''Configurações que são adicionadas ao contexto das requisições.'''


    chave = models.CharField(max_length=255, choices=CONFIG_CHAVES, unique=True)

    valor = models.TextField()

    html = models.BooleanField(default=False)

    def __unicode__(self):
        return self.get_chave_display()

    class Meta:


        verbose_name = u'configuração'

        verbose_name_plural = u'configurações'
