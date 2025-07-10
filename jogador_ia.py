# -*- coding: utf-8 -*-
# jogador_ia.py

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self):
        simbolo_ia = self.getSimbolo()
        simbolo_oponente = Tabuleiro.JOGADOR_X if simbolo_ia == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0
        m = self.tabuleiro.matriz
        casas = self.tabuleiro.get_casas_vazias()

        # R1 – Vitória ou bloqueio
        for l, c in casas:
            if self.tabuleiro.simula_jogada(l, c, simbolo_ia):
                return (l, c)
            if self.tabuleiro.simula_jogada(l, c, simbolo_oponente):
                return (l, c)

        # R2 – Criar duas ameaças (garfo)
        for l, c in casas:
            m[l][c] = simbolo_ia
            ameacas = 0
            for l2, c2 in self.tabuleiro.get_casas_vazias():
                if self.tabuleiro.simula_jogada(l2, c2, simbolo_ia):
                    ameacas += 1
            m[l][c] = Tabuleiro.DESCONHECIDO
            if ameacas >= 2:
                return (l, c)

        # R3 – Centro
        if m[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4 – Canto oposto
        cantos_opostos = [((0, 0), (2, 2)), ((0, 2), (2, 0)), ((2, 0), (0, 2)), ((2, 2), (0, 0))]
        for (a, b), (x, y) in cantos_opostos:
            if m[a][b] == simbolo_oponente and m[x][y] == Tabuleiro.DESCONHECIDO:
                return (x, y)

        # R5 – Qualquer canto
        for l, c in [(0, 0), (0, 2), (2, 0), (2, 2)]:
            if m[l][c] == Tabuleiro.DESCONHECIDO:
                return (l, c)

        # R6 – Casa livre arbitrária
        if casas:
            return casas[0]

        # Fallback absoluto – nunca retorna None
        print("[IA DEBUG] Nenhuma jogada válida. Retornando (0, 0)")
        return (0, 0)
