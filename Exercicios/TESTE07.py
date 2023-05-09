"""
O grandioso rei da ilha Paradis é avisado que os titãs estão organizando um ataque!

Os titãs possuem 3 tamanhos, titãs pequenos de p metros, titãs médios de m metros e titãs grandes de g metros. Vários titãs de diferentes tamanhos estão se organizando para um ataque, e o rei precisa construir várias muralhas de x metros para pará-los.

Felizmente o rei conhece a estratégia dos titãs, eles atacarão em sequência, um após o outro. Quando um titã de tamanho k encontra uma muralha uma das duas situações acontecem:

Se a muralha for maior ou do mesmo tamanho que o titã, ele destrói k metros da muralha depois se cansa e morre, assim a muralha fica k metros mais baixa.
Se a muralha for menor que o titã, ele pula aquela muralha e segue para a próxima.
O rei pede a você, conselheiro do rei, qual o menor número de muralhas que precisam ser construídas antes do ataque para parar o ataque dos titãs.

Entrada
Na primeira linha seguirão 2 inteiros, n e x, separados por um espaço, que representam a quantidade de titãs que compõem o ataque e o tamanho das muralhas a serem construídas.

Na segunda linha segue uma string de tamanho n, composta pelos caracteres P, M e G, indicando o tamanho (pequeno, médio e grande respectivamente) do i-ésimo titã. O titã
T
i
+
1
 atacara depois do titã
T
i
.

Na terceira linha seguem 3 inteiros, p, m e g, que representam o tamanho de um titã pequeno, médio e grande respectivamente.

1
≤
n
≤
3
×
10
5
1
≤
x
≤
10
5
1
≤
p
≤
m
≤
g
≤
x
Saída
Baseado na descrição do problema, imprima a quantidade miníma de muralhas para parar o ataque dos titãs.

Exemplos de Entrada
3 20
MPG
3 8 10

	Exemplos de Saída
2

Exemplos de Entrada
8 20
MGGPGGGP
3 8 10

Exemplos de Saída
4

Exemplos de Entrada
4 6
GPMP
3 4 5

Exemplos de Saída
3
"""
n, x = map(int, input().split())
titans = input().strip()
p, m, g = map(int, input().split())

walls = [x] * 2  # inicia com duas muralhas de tamanho x
count = 0

for titan in titans:
    if titan == 'P':
        if walls[0] >= p:
            walls[0] -= p
        elif walls[1] >= p:
            walls[1] -= p
        else:
            walls.append(x - p)
            count += 1
    elif titan == 'M':
        if walls[0] >= m:
            walls[0] -= m
        elif walls[1] >= m:
            walls[1] -= m
        else:
            walls.append(x - m)
            count += 1
    else:  # titan == 'G'
        if walls[0] >= g:
            walls[0] -= g
        elif walls[1] >= g:
            walls[1] -= g
        else:
            walls.append(x - g)
            count += 1

print(count+2)  # adiciona 2 muralhas extras no final

