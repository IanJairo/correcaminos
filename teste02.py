from resolveLabirinto import *

labirinto2 = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
['#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],
['#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

resultado_esperado = False
resultado = eh_possivel_sair(labirinto2)

print(resultado == resultado_esperado) #deve ser True

