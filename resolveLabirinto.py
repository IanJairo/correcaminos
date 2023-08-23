from geraLabirinto import *

class Node:
    def __init__(self, posicao, pai=None):
        self.posicao = posicao #Define a posição do nó.
        self.pai = pai #Define o nó pai na árvore de busca.
    
def movimento_valido(labirinto, linha, coluna):
    return 0 <= linha < len(labirinto) and 0 <= coluna < len(labirinto[0]) and labirinto[linha][coluna] == " " #Checa se o movimento realizado é válido ou não

def eh_fim(labirinto, linha, coluna):
    return len(labirinto[0]) - 1 == coluna and labirinto[linha][coluna] == "p" #Verifica se é o ponto de saída.

def eh_possivel_sair(labirinto):
    inicio = (1, 0) #Define a posição inicial.

    direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)] #Direções possíveis (direita, esquerda, baixo, cima).

    pilha = [Node(inicio)] #Inicializa a pilha com o nó inicial.
    visitados = set() #Conjunto para armazenar posições visitadas.

    while pilha:
        no_atual = pilha.pop() #Pega o último nó da pilha.

        if eh_fim(labirinto, no_atual.posicao[0], no_atual.posicao[1]): #Verifica se chegou ao ponto de saída do labirinto.
            
            print(" ")
            print("Labirinto Completo ")
            
            print_lab(labirinto)
            
            print(" ")  
            print(" ")
                        
            return True

        if no_atual.posicao in visitados: #Ignora nós já visitados.
            continue

        visitados.add(no_atual.posicao) #Marca o nó como visitado.

        for direcao_linha, direcao_coluna in direcoes: #Se estiver na última coluna, não verifica outras direções.
            if (no_atual.posicao[1] == len(labirinto[0]) - 1):
                break
            
            nova_linha = no_atual.posicao[0] + direcao_linha
            nova_coluna = no_atual.posicao[1] + direcao_coluna

            if movimento_valido(labirinto, nova_linha, nova_coluna):
                nova_posicao = (nova_linha, nova_coluna)
                pilha.append(Node(nova_posicao, no_atual)) #Adiciona novo nó à pilha.
                labirinto[nova_linha][nova_coluna] = 'p' #Marca o caminho percorrido.

    return False

if __name__ == "__main__":
    lab = gera_lab(6,9) #Gera um labirinto 
    lab [1][0] = "p" #Define o ponto de partida.

    print_lab(lab) #Imprime o labirinto.

    resultado_esperado = True
    resultado = eh_possivel_sair(lab) #Verifica se é possível sair.

    print(resultado_esperado == resultado)