""" Constantes do jogo Numberlink """

""" TIPOS DE CANOS 
Pontas
* n: virado para cima, norte.
* w: virado para a esquerda, oeste.
* e: virado para a direita, este.
* s: virado para baixo, sul.
* ns: cano vertical
* we: cano horizontal
Cotovelos
* ne: cotovelo para cima e para a direita
* nw: cotovelo para cima e para a esquerda
* se: cotovelo para baixo e para a direita
* sw: cotovelo para baixo e para a esqueda
"""
COTOVELOS_NORTE = ['ne', 'nw']
COTOVELOS_SUL = ['se', 'sw']
COTOVELOS = COTOVELOS_NORTE + COTOVELOS_SUL
VERTICAIS = ['ns']
HORIZONTAIS = ['we']
ORTOGONAIS = VERTICAIS + HORIZONTAIS
PONTAS_NORTE = ['n']
PONTAS_SUL = ['s']
PONTAS_ESTE = ['e']
PONTAS_OESTE = ['w']
PONTAS = PONTAS_NORTE + PONTAS_SUL + PONTAS_ESTE + PONTAS_OESTE
CANOS = COTOVELOS + ORTOGONAIS + PONTAS