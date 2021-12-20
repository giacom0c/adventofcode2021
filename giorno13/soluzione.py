def get_data(filename):
    coordinate = []
    mosse = []
    x_max = y_max = 0
    with open(filename, 'r') as file:
        for line in file:
            if ',' in line:
                x, y = map(int, line.strip().split(','))
                coordinate.append((x, y))
                if x > x_max:
                    x_max = x
                if y > y_max:
                    y_max = y
            elif 'x=' in line:
                temp = line.strip().split('=')
                mosse.append(('x', int(temp[1])))
            elif 'y=' in line:
                temp = line.strip().split('=')
                mosse.append(('y', int(temp[1])))
            else:
                continue
    return coordinate, x_max, y_max, mosse


def parte1(coordinate, x_max, y_max, mosse):
    foglio = []
    for j in range(y_max + 1):
        temp = []
        for i in range(x_max + 1):
            if (i, j) in coordinate:
                temp.append('#')
            else:
                temp.append('.')
        foglio.append(temp)
    for idx, m in enumerate(mosse):
        print('Piega numero: ' + str(idx))
        if m[0] == 'y':
            y_max = m[1]
            for j in range(1, y_max + 1):
                for i in range(x_max + 1):
                    if foglio[-j][i] == '#':
                        foglio[j - 1][i] = '#'
                print(foglio[j - 1])
        else:
            x_max = m[1]
            for j in range(y_max + 1):
                for i in range(1, x_max + 1):
                    if foglio[j][-i] == '#':
                        foglio[j][i - 1] = '#'
                print(foglio[j][:x_max])
    conta = 0
    for j in range(fold + 1):
        for i in range(x_max + 1):
            if foglio[j][i] == '#':
                conta += 1
    return conta


def parte2(filename):
    print('TODO')


filename = 'input.txt'
coordinate, x_max, y_max, mosse = get_data(filename)
print(parte1(coordinate, x_max, y_max, mosse))
parte2(filename)
