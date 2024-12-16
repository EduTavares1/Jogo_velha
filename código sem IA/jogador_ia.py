# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)

    
               
                      
               
            

    def getJogada(self) -> (int, int):

        #Regra 4
        
        
        #Regra 5
        jogada = self.Regra_5()
        if jogada:
            return jogada

        #Regra 6
        return self.Regra_6()
    
    def Regra_5(self) -> (int, int):
        
        extremidades =[(0,0),(0,2),(2,0),(2,2)]

        for extremo in extremidades:
            l,c = extremo
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return(l,c)
        return None    

    def Regra_6(self) -> (int,int):
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)
        return None            