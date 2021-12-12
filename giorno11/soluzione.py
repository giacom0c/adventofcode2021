from itertools import product

# Costruisco la mappa dei polpi luminosi leggendo il file di input
def get_octos(filename):
    octos = []
    with open(filename, 'r') as file:
        for line in file:
            riga = []
            line = line.strip()
            for i in range(len(line)):
                riga.append(int(line[i]))
            octos.append(riga)
    return octos


# Funzione generatrice dei (fino a) 8 vicini
# Credits to u/mebeim
def neighbors8(r, c, h, w):
    deltas = (
        (1, 0), (-1,  0), ( 0, 1), ( 0, -1),
        (1, 1), ( 1, -1), (-1, 1), (-1, -1)
    )
    for dr, dc in deltas:
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < h and 0 <= cc < w:
            yield rr, cc


def flood_flash(octos, x ,y):
    # Caso in cui NON c'è il flash, non faccio nulla
    if octos[x][y] <= 9:
        return    
    # Se c'è il flash, marco la cella con un -1 e propago ai vicini con la ricorsione
    octos[x][y] = -1    
    for nx, ny in neighbors8(x, y, len(octos), len(octos[0])):
        if octos[nx][ny] != -1:
            octos[nx][ny] += 1
            flood_flash(octos, nx, ny)


def step(octos):
    flash = 0
    # Passo 1: incremento tutti i valori di 1
    for i, j in product(range(len(octos)), range(len(octos[0]))):
        octos[i][j] += 1
    # Passo 2: applico la funzione ricorsiva di flash
    for i, j in product(range(len(octos)), range(len(octos[0]))):
        flood_flash(octos, i, j)
    # Infine conto tutti i valori uguali a -1: sono quelli che hanno flashato
    for i, j in product(range(len(octos)), range(len(octos[0]))):
        if octos[i][j] == -1:
            flash += 1
            octos[i][j] = 0
    return flash


def parte1(octos):
    flash = 0
    for _ in range(100):
        flash += step(octos)
    print(flash)


def parte2(filename):
    # Rigenero la mappa dal file di input
    octos = get_octos(filename)
    flash = 0
    steps = 0
    while flash != (len(octos) * len(octos[0])):
        flash = step(octos)
        steps += 1
    print(steps)


filename = 'input.txt'
octos = get_octos(filename)
parte1(octos)
parte2(filename)
