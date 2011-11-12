# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.localflavor.br.br_states import STATE_CHOICES as UFS
from django.conf import settings
import Image

CATEGORIAS = (
  ('EA', "Ex-Alunos"),
  ('HO', "Homenageados"),
  ('EM', "Ex-Moradores"),
  ('MO', "Moradores"),
)

def caminho_foto(instance, filename):
  return "%s/moradores/%s" % (settings.UPLOAD_PATH, filename)
  
class Morador(models.Model):
    """Perfil do morador com seus dados."""
    
    foto = models.ImageField(upload_to=caminho_foto)

    nome = models.CharField(max_length=100)
    email = models.EmailField(verbose_name=u"E-mail de contato")
    
    categoria = models.CharField(max_length=2, choices = CATEGORIAS)
    
    sobre = models.CharField(max_length=100)

    cidade = models.CharField(null=True, blank=True, max_length=100)
    uf = models.CharField(null=True, blank=True, max_length=2, choices=UFS)
    
    def save(self, *args, **kwargs):
        
        tar_width = 117
        tar_height = 300
        jpeg_quality = 90
        
        super(Morador, self).save(*args, **kwargs)
    
        #redimensionando a imagem    
        src_path = settings.RAIZ + self.foto.url
        image = Image.open(src_path)
        src_width, src_height = image.size
        resize_ratio = min(1, min(float(tar_width) / float(src_width), float(tar_height) / float(src_height)))
        image = image.resize((int(resize_ratio * src_width), int(resize_ratio * src_height)), Image.ANTIALIAS)
    
        try:
            image.save(src_path, image.format, quality = jpeg_quality, optimize = 1)
        except:
            image.save(src_path, image.format, quality = jpeg_quality)
    
    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = u"Partênope"