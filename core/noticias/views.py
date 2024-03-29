# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import Http404
from models import Noticia
from django.template import RequestContext

def noticia(request, link=None):
  
  if link:
    try:
      noticia = Noticia.objects.publicadas().get(cod=link)
    except:
      raise Http404
  else:
    raise Http404
  
  c = {"noticia":noticia}

  return render_to_response('conteudo/noticia.html', c, context_instance=RequestContext(request))