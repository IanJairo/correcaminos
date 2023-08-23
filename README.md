# Correcaminos

## Objetivo
Colocar em prática os conceitos aprendidos sobre listas encadeadas numa aplicação em Python. Um miniprojeto da matéria Estrutura de Dados.
## Problema
Considere um labirinto representado por uma matriz m × n. O caminho livre é marcado na matriz com " " (sem aspas),
enquanto os caminhos ocupados são marcados com "#" (sem aspas).
O ratinho está na posição (livre) (1, 0) e quer chegar à posição (livre) (m − 2, n − 1) passando pelo labirinto.

## Integrantes
* [Ian Jairo T. Gonzales](github.com/IanJairo)
* [João Gabriel S. Dantas](github.com/gabrielDantas10)
* [Haul Muller](https://github.com/HaulMuller)

## Comentários sobre a solução
1. Sofremos um pouco para entender a lógica de como ratinho iria percorrer cada espaço.
2. No entanto, encontramos a maneira de fazer acontecer. O ratinho percorre cada passo, e, se encontrar um beco sem saída, ele volta casa por casa até a última que ele conseguir avançar.
3. Foi meio frustrante em um dos testes perceber que o gerador sempre vinha com um laberinto sem saída. Deve ter sido um erro da máquina ou azar da vida.
4. Sem mais, **foi legal de resolver**.