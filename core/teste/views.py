# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from noticias.models import Noticia
from photologue.models import Gallery
from videos.models import Video

def default(request):
  try:
      destaque = Noticia.objects.publicadas()[0]
  except:
      destaque = None
  noticias = Noticia.objects.publicadas()[1:][:3]
  
  try:
    g = Gallery.objects.filter(is_public=True)[0].photos.all()[:12]
  except:
    g = None
  
  try:
    v = Video.objects.order_by('-id')[0]
  except:
    v = None
  
  c = {"noticias":noticias, "destaque":destaque, "galeria":g, "video":v}

  return render_to_response('conteudo/index.html', c, context_instance=RequestContext(request))
