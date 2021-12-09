def parte1(filename):
    mappa = []
    with open(filename, 'r') as file:
        for line in file:
            riga = []
            line = line.strip()
            for i in range(len(line)):
                riga.append(int(line[i]))
            mappa.append(riga)
    low_points = []
    for i in range(len(mappa)):
        for j in range(len(mappa[0])):
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


filename = 'input.txt'
parte1(filename)
