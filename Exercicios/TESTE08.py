"""
No tower defense Magic and Sword, o jogador pode lançar magias de área para derrotar as unidades inimigas. As magias são elementais: fogo, água, ar e terra, e a região afetada é determinada por um círculo cujo raio depende do nível da magia.

A tabela abaixo lista cada magia, o dano e o respectivo raio por nível:



As unidades inimigas são delimitadas por um retângulo de largura w e altura h, com canto inferior esquerdo posicionado no ponto (x0, y0). O inimigo sofrerá dano caso seu retângulo delimitador tenha qualquer intercessão com a área deﬁnida pelo círculo da magia.

Dada a posição e o retângulo delimitador da unidade inimiga, o centro da explosão e o identiﬁcador e o nível da magia, determine o dano sofrido pela unidade. Caso a unidade esteja fora do alcance da magia, o dano sofrido é igual a zero.

Entrada
A entrada consiste em T (1 ≤ T ≤ 1000) casos de teste, onde o valor de T é informado na primeira linha da entrada. Cada caso de teste é composto por duas linhas. A primeira contém quatro número inteiros que repre-sentam as dimensões w e h (1 ≤ w, h ≤ 1000) do retângulo e as coordenadas x0 e y0 (0 ≤ x0, y0 ≤ 1000) do canto inferior esquerdo. A segunda linha do caso de teste contém uma string com o identiﬁcador da magia (ﬁre para fogo, water para água, earth para terra e air para ar), o nível N desta magia (1 ≤ N ≤ 3) e as coordenadas cx e cy (0 ≤ cx, cy ≤ 1000) do centro da área da explosão.

Saída
Para cada caso de teste, a saída deve ser o valor do dano recebido pela unidade, seguido de uma quebra de linha.

Exemplo de Entrada
4
10 10 50 50
fire 1 85 55
10 10 50 50
fire 2 85 55
10 10 50 100
water 3 100 100
10 10 50 100
air 3 100 100


Exemplo de Saída
0
200
300
100
"""
import math

# Função para calcular a distância entre dois pontos
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Função para verificar se um ponto está dentro do retângulo
def dentro_do_retangulo(x, y, x0, y0, w, h):
    return x >= x0 and x <= x0 + w and y >= y0 and y <= y0 + h

# Dicionário com as informações sobre as magias
magias = {
    "fire": [(2, 20), (3, 30), (4, 40)],
    "water": [(3, 10), (5, 20), (7, 30)],
    "earth": [(1, 30), (2, 50), (3, 80)],
    "air": [(4, 15), (6, 25), (8, 35)]
}

# Lê o número de casos de teste
t = int(input())

# Loop pelos casos de teste
for _ in range(t):
    # Lê as informações do retângulo
    w, h, x0, y0 = map(int, input().split())

    # Lê as informações da magia
    magia, nivel, cx, cy = input().split()
    nivel = int(nivel)
    cx, cy = int(cx), int(cy)

    # Calcula o raio da magia
    raio = magias[magia][nivel - 1][1]

    # Inicializa o dano como zero
    dano = 0

    # Loop pelos pontos dentro do retângulo
    for x in range(x0, x0 + w + 1):
        for y in range(y0, y0 + h + 1):
            # Se o ponto está dentro do raio da magia, adiciona o dano
            if distancia(x, y, cx, cy) <= raio and dentro_do_retangulo(x, y, x0, y0, w, h):
                dano += magias[magia][nivel - 1][0]

    # Imprime o dano
    print(dano)
