"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python

import this

A ideia de PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;
[2] - Utilize nomes em minúsculo, separados por underline para funções ou
variáveis;
[3] - Utilize 4 espaços para indentação!
[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos  dentro de uma classe devem ser separados com uma única linha
em branco;
[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;
import sys
import os

*Não há problemas em utilizar:
from types import StringType.ListType

*Caso tenha muitos imports de um mesmo pacote, recomenda-se:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType)

* Imports devem ser colocados no topo do arquivo, logo depois de qualquer
comentário ou docstrings e antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções
*Não faça:
funcao( algo[ 1 ], { outro: 2 } )
algo (1)
dict ['chave'] = lista[indice]
x              = 1
y              = 3
variave_longa  = 5

*Faça
funcao(algo[1],{outro:2})
algo(1)
dict['chave'] = lista[indice]
x = 1
y = 3
variave_longa = 5

[7] - Termina sempre uma instrução com uma nova linha

import this

"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 3

if 'a' in 'banana':
    print('tem')