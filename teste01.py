from resolveLabirinto import *
#Teste 1
labirinto1 = [

['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
[' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'],
['#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#'],
['#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


resultado_esperado = True
resultado = eh_possivel_sair(labirinto1)

print(resultado == resultado_esperado) #deve ser True

