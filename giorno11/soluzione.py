from math import prod
from itertools import product

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

# Fonte: https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569
def flood_flash(octos, x ,y):
    # we need the x and y of the start position, the old value,
    # and the new value
    # the flood fill has 4 parts
    # firstly, make sure the x and y are inbounds
    if x < 0 or x >= len(octos) or y < 0 or y >= len(octos[0]) or octos[x][y] == -1:
        return
    # secondly, check if the current position equals the old value
    if octos[x][y] < 9:
        octos[x][y] += 1
        return
    
    # thirdly, set the current position to the new value
    octos[x][y] = -1
    
    # fourthly, attempt to fill the neighboring positions
    flood_flash(octos, x+1, y)
    flood_flash(octos, x-1, y)
    flood_flash(octos, x, y+1)
    flood_flash(octos, x, y-1)


def parte1(octos):    
    low_points = []
    for i, j in product(range(len(octos)), range(len(octos[0]))):
        temp = []
        try:
            temp.append(octos[i - 1][j])
        except:
            pass
        try:
            temp.append(octos[i][j - 1])
        except:
            pass
        try:
            temp.append(octos[i][j + 1])
        except:
            pass
        try:
            temp.append(octos[i + 1][j])
        except:
            pass
        if octos[i][j] < min(temp):
            low_points.append(octos[i][j])
    print(sum(low_points) + len(low_points))


def parte2(octos):
    bacini = []
    for i, j in product(range(len(octos)), range(len(octos[0]))):
        flood_flash(octos, i, j)
        #print(octos)
        totale = 0
        for x, y in product(range(len(octos)), range(len(octos[0]))):
            if octos[x][y] == -1:
                totale += 1
                octos[x][y] = 9
        if totale > 0:
            bacini.append(totale)
    bacini.sort()
    #print(bacini)
    print(prod(bacini[-3:]))


filename = 'input.txt'
octos = get_octos(filename)
parte1(octos)
#parte2(octos)
