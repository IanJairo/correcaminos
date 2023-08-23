from geraLabirinto import *

class Node:
    def __init__(self, posicao, pai=None):
        self.posicao = posicao
        self.pai = pai
    
def movimento_valido(labirinto, linha, coluna):
    return 0 <= linha < len(labirinto) and 0 <= coluna < len(labirinto[0]) and labirinto[linha][coluna] == " "

def eh_fim(labirinto, linha, coluna):
    return len(labirinto[0]) - 1 == coluna and labirinto[linha][coluna] == "p"

def eh_possivel_sair(labirinto):
    inicio = (1, 0)

    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    pilha = [Node(inicio)]
    visitados = set()

    while pilha:
        no_atual = pilha.pop()

        if eh_fim(labirinto, no_atual.posicao[0], no_atual.posicao[1]):
            
            print(" ")
            print("Labirinto Completo ")
            
            print_lab(labirinto)
            
            print(" ")  
            print(" ")
                        
            return True

        if no_atual.posicao in visitados:
            continue

        visitados.add(no_atual.posicao)

        for direcao_linha, direcao_coluna in direcoes:
            if (no_atual.posicao[1] == len(labirinto[0]) - 1):
                break
            
            nova_linha = no_atual.posicao[0] + direcao_linha
            nova_coluna = no_atual.posicao[1] + direcao_coluna

            if movimento_valido(labirinto, nova_linha, nova_coluna):
                nova_posicao = (nova_linha, nova_coluna)
                pilha.append(Node(nova_posicao, no_atual))
                labirinto[nova_linha][nova_coluna] = 'p'

    return False


lab = gera_lab(6,9) #gera um labirinto 
lab [1][0] = "p"

print_lab(lab)

resultado_esperado = True
resultado = eh_possivel_sair(lab)

print(resultado_esperado == resultado)