"""
Módulo das escalas musicais.

Attributes:
   ESCALAS: Escalas implementadas usando a notação de inteiros
   NOTAS: Notas musicais

# ESCALAS

As escalas estão implementadas em uma constante chamada `ESCALAS`. Que é um dicionário onde as chaves são os nomes das escalas. Se quiser ver todas as escalas implementadas pode usar:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import ESCALAS
>>> ESCALAS
{'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)...}

```

A notação inteira para as escalas foi retirada da página [List of musical scales and modes](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes) na wikipedia.

tip: Dica!
    Você pode contribuir com novas escalas usando a notação inteira:
    [Escalas wikipedia](https://en.wikipedia.org/wiki/List_of_musical_scales_and_modes).
    Todos os Pull Requests serão bem vindos! :heart:

# NOTAS

As notas estão sendo definidas em uma constante `NOTAS`. Foi optado por menter somente as notas no formato Natural e o Sustenido (#) para a simplificação do fluxo de trabalho. Embora não esteja totalmente correto. Para ver as 12 notas você pode:

```py title="No seu shell interativo"
>>> from notas_musicais.escalas import NOTAS
>>> NOTAS
['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

```
"""


NOTAS = 'C C# D D# E F F# G G# A A# B'.split()
ESCALAS = {'maior': (0, 2, 4, 5, 7, 9, 11), 'menor': (0, 2, 3, 5, 7, 8, 10)}
