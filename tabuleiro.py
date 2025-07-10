# -*- coding: utf-8 -*-
# tabuleiro.py

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO] * 3,
            [Tabuleiro.DESCONHECIDO] * 3,
            [Tabuleiro.DESCONHECIDO] * 3
        ]

    def verifica_vitoria(self, simbolo):
        m = self.matriz
        for i in range(3):
            # Linhas e colunas
            if all(m[i][j] == simbolo for j in range(3)) or all(m[j][i] == simbolo for j in range(3)):
                return True
        # Diagonais
        if m[0][0] == simbolo and m[1][1] == simbolo and m[2][2] == simbolo:
            return True
        if m[0][2] == simbolo and m[1][1] == simbolo and m[2][0] == simbolo:
            return True
        return False

    def get_casas_vazias(self):
        return [(l, c) for l in range(3) for c in range(3) if self.matriz[l][c] == Tabuleiro.DESCONHECIDO]

    def simula_jogada(self, l, c, simbolo):
        if self.matriz[l][c] != Tabuleiro.DESCONHECIDO:
            return False
        self.matriz[l][c] = simbolo
        venceu = self.verifica_vitoria(simbolo)
        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
        return venceu

    def tem_campeao(self):
        if self.verifica_vitoria(Tabuleiro.JOGADOR_X):
            return Tabuleiro.JOGADOR_X
        if self.verifica_vitoria(Tabuleiro.JOGADOR_0):
            return Tabuleiro.JOGADOR_0
        return None
