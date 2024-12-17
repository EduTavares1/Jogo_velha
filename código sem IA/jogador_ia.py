# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
        self.tipo_d_oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0
        

    
    
               
                      
               
            

    def getJogada(self) -> tuple[int, int] | None:

        #Regra 3
        jogada = self.Regra_3()
        if jogada:
            return jogada

        #Regra 4
        jogada = self.Regra_4()
        if jogada:
            return jogada
        
        
        #Regra 5
        jogada = self.Regra_5()
        if jogada:
            return jogada

        #Regra 6
        return self.Regra_6()
    
    def Regra_3(self) -> tuple[int, int] | None:
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1,1)

    def Regra_4(self) -> tuple[int, int] |  None:
        extremidades = [(0,0), (0,2),(2,0),(2,2)]

        for extremo in extremidades:
            l,c = extremo
            canto_oposto = (2-l, 2-c)
            if self.matriz[l][c] == self.tipo_d_oponente and self.matriz[canto_oposto[0]][canto_oposto[1]] == Tabuleiro.DESCONHECIDO:
                return canto_oposto
        return None

    
    
    
    def Regra_5(self) -> tuple[int, int] |  None:
        
        extremidades =[(0,0),(0,2),(2,0),(2,2)]

        for extremo in extremidades:
            l,c = extremo
            if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                return(l,c)
        return None    

    def Regra_6(self) -> tuple[int, int] | None:
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    return (l, c)
        return None            