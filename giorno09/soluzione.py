from math import prod
# product ci permette di "appiattire" i doppi cicli for
from itertools import product

# Costruisco la mappa leggendo il file di input
def get_mappa(filename):
    mappa = []
    with open(filename, 'r') as file:
        for line in file:
            riga = []
            line = line.strip()
            for i in range(len(line)):
                riga.append(int(line[i]))
            mappa.append(riga)
    return mappa

# Fonte: https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
def flood_fill(mappa, x ,y):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(mappa) or y < 0 or y >= len(mappa[0]):
        return
    # secondly, check if the current position equals the old value
    if mappa[x][y] == 9 or mappa[x][y] == -1:
        return    
    # thirdly, set the current position to the new value
    mappa[x][y] = -1    
    # fourthly, attempt to fill the neighboring positions
    flood_fill(mappa, x + 1, y)
    flood_fill(mappa, x - 1, y)
    flood_fill(mappa, x, y + 1)
    flood_fill(mappa, x, y - 1)


def parte1(mappa):    
    low_points = []
    for i, j in product(range(len(mappa)), range(len(mappa[0]))):
        temp = []
        try:
            temp.append(mappa[i - 1][j])
        except:
            pass
        try:
            temp.append(mappa[i][j - 1])
        except:
            pass
        try:
            temp.append(mappa[i][j + 1])
        except:
            pass
        try:
            temp.append(mappa[i + 1][j])
        except:
            pass
        if mappa[i][j] < min(temp):
            low_points.append(mappa[i][j])
    print(sum(low_points) + len(low_points))


def parte2(mappa):
    bacini = []
    # Applico la funzione ricorsiva a ogni elemento della mappa
    for i, j in product(range(len(mappa)), range(len(mappa[0]))):
        flood_fill(mappa, i, j)
        totale = 0
        # Dopo ogni "passata", scorro la mappa per vedere la grandezza del bacino creato
        for x, y in product(range(len(mappa)), range(len(mappa[0]))):
            if mappa[x][y] == -1:
                totale += 1
                # Reinizializzo il valore dell'elemento a 9:
                # Ogni elemento si trova in un solo e unico bacino, in questo modo non viene considerato per le iterazioni successive
                mappa[x][y] = 9
        if totale > 0:
            bacini.append(totale)
    # Do in output il prodotto dei 3 bacini pi?? grandi
    bacini.sort()
    print(prod(bacini[-3:]))


filename = 'input.txt'
mappa = get_mappa(filename)
parte1(mappa)
parte2(mappa)
