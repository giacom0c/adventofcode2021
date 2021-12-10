from collections import deque

aperte = ['(', '[', '{', '<']

def parte1(filename):
    totale = 0
    incomplete = []
    punti = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            incompleto = True
            pila = deque()
            for parentesi in line:
                # Se trovo un "aperta parentesi", inserisco nella pila
                if parentesi in aperte:
                    pila.append(parentesi)
                # Altrimenti se è una chiusa, controllo che sia l'opposto dell'ultima parentesi aperta
                # La confronto quindi con l'elemento in cima alla pila, se non corrisponde ho trovato un chunck corrotto
                else:
                    if not len(pila) or not (abs(ord(parentesi) - ord(pila.pop())) <= 2):
                        totale += punti[parentesi]
                        incompleto = False
                        break
            # Se il chunck non è corrotto, allora è incompleto. Li raccolgo perché serviranno per la parte 2
            if incompleto:
                incomplete.append(pila)
    return totale, incomplete


def parte2(incomplete):
    totali = []
    for chunk in incomplete:
        totale = 0
        # Inverto le posizioni degli elementi nella pila, altrimenti li avrei dovuti scorrere al contrario
        chunk.reverse()
        for parentesi in chunk:
            if parentesi == '(':
                totale = totale * 5 + 1
            elif parentesi == '[':
                totale = totale * 5 + 2
            elif parentesi == '{':
                totale = totale * 5 + 3
            else:
                totale = totale * 5 + 4
        totali.append(totale)
    # Ordino i vari totali e stampo quello in posizione centrale
    totaltemp = sorted(totali)
    print(totaltemp[len(totaltemp) // 2])


filename = 'input.txt'
totparte1, incomplete = parte1(filename)
parte2(incomplete)
