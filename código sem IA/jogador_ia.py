# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)

    def R_3(self) -> (int,int):
        lista = []
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            self.matriz[1][1] == Tabuleiro.JOGADOR_0
            return 1,1
        return None
            

    def getJogada(self) -> (int, int):
        lista = []

        meio = self.R_3()
        if meio:
            return meio
        
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))
                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None