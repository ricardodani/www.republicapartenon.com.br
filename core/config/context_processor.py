# -*- encoding: utf-8 -*-

'''
Context Processor da app de Configurações.
'''

from config.models import Configuracao

def configuracoes(request):
    '''
    Atualiza o request context com variávies definidas
    no model config.Configuracao.
    '''

    configs = {}

    for c in Configuracao.objects.all():
        configs.update({
            c.chave: (c.valor, c.html)
        })

    return {'configs': configs}

