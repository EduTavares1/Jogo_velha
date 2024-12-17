# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
        self.tipo_d_oponente = Tabuleiro.JOGADOR_X if tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0
        

    
    
               
                      
               
            

    def getJogada(self) -> tuple[int, int] | None:
        #Regra 1
        jogada = self.Regra_1(self.tipo) or self.Regra_1(self.tipo_d_oponente)
        if jogada:
            return jogada
        

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

    def Regra_1(self, tipo:int) -> tuple[int, int] | None:
        for i in range(0,3):
            #checando as linhas
            if self.matriz[i].count(tipo) == 2 and Tabuleiro.DESCONHECIDO in self.matriz[i]:
                return(i, self.matriz[i].index(Tabuleiro.DESCONHECIDO))
        
        #checando colunas
        coluna = [self.matriz[c][i] for c in range(0,3)]
        if coluna.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in coluna:
            return(coluna.index(Tabuleiro.DESCONHECIDO), i)
        
        #checando as diagonais
        diagonal_p = [self.matriz[i][i] for i in range(0,3)]
        diagonal_s = [self.matriz[i][2- i] for i in range(0,3)]

        if diagonal_p.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal_p:
            return (diagonal_p.index(Tabuleiro.DESCONHECIDO), diagonal_p.index(Tabuleiro.DESCONHECIDO))
        if diagonal_s.count(tipo) == 2 and Tabuleiro.DESCONHECIDO in diagonal_s:
            return (diagonal_s.index(Tabuleiro.DESCONHECIDO), 2-diagonal_s.index(Tabuleiro.DESCONHECIDO))
        return None
        
        
    
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