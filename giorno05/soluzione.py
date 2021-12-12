from collections import defaultdict

# Funzione generatrice https://wiki.python.org/moin/Generators
# Ritorna un iterable, nel nostro caso la lista dei punti da segnare.
# Unendo i punti troviamo il segmento tracciato.
def disegno_segmento(ax, ay, bx, by):
    if ax == bx:
        for y in range(min(ay, by), max(ay, by) + 1):
            yield ax, y
    elif ay == by:
        for x in range(min(ax, bx), max(ax, bx) + 1):
            yield x, ay


def parte1(filename):
    coordinate = []
    # Struttura dati che funge da matrice sparsa
    # Se una chiave del dizionario non ha valore, gli viene automaticamente assegnato 0
    mappa = defaultdict(int)
    with open(filename, 'r') as file:
        # Parsing dell'input: va diviso in 4 coordinate
        for line in file:
            a, b = line.split('->')
            ax, ay = map(int, a.split(','))
            bx, by = map(int, b.split(','))
            coordinate.append((ax, ay, bx, by))
    # Disegno ogni segmento ricavato dalle 4-uple di coordinate prese sopra
    for c in coordinate:
        # L'asterisco indica argument unpacking, passa quindi le 4 coordinate come parametri distinti
        for x, y in disegno_segmento(*c):
            mappa[x, y] += 1
    # Conto i punti di intersezioni di 2 o più segmenti
    da_evitare = sum(x > 1 for x in mappa.values())
    print(da_evitare)


def parte2(filename):
    print('TODO')


filename = 'input.txt'
parte1(filename)
parte2(filename)
