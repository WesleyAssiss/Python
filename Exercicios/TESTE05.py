"""
Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

Exemplo de Entrada
7 8 9 10
Exemplo de Saída
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
"""

# hi -> horário inicial
# mi -> minuto inicial
# hf -> horário final
# mf -> minuto final

hi, mi, hf, mf = map(int, input().split())

# transforma as horas em minutos
ini_min = hi * 60 + mi
fim_min = hf * 60 + mf

# se o horário final é menor que o inicial, acrescenta 24h ao horário final
if ini_min >= fim_min:
    fim_min += 24 * 60

duracao_min = fim_min - ini_min
duracao_h = duracao_min // 60
duracao_min -= duracao_h * 60

print(f"O JOGO DUROU {duracao_h} HORA(S) E {duracao_min} MINUTO(S)")
