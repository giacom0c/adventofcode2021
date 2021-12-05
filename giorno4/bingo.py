import re

#Check orizzontale del bingo
bingo = ['X', 'X', 'X', 'X', 'X']

# Funzione per parsare il file di input: 
# restituisce la lista di numeri estratti dal tabellone del bingo e la lista delle cartelle
def getCartelle(filename):
    tabellone = ''
    cartelle = []
    cartella = []
    with open(filename, 'r') as file:
        for line in file:
            # Se la riga letta del file contiene una virgola, allora è quella dei numeri del tabellone
            if ',' in line:
                tabellone = line.strip('\n').split(',')
            else:
                # Controllo se la riga non è vuota: 
                # in questo caso significa che sto costruendo una cartella riga per riga
                if re.search("\d ", line) is not None:
                    cartella.append(line.strip('\n').split())
                else:
                    # Ultimo caso: la riga è vuota
                    # se non ho una cartella vuota (unico caso, la seconda riga del file), la aggiungo alla lista delle cartelle
                    if len(cartella):
                        cartelle.append(cartella)
                        # Svuoto la cartella "temporanea"
                        cartella = []
    # Inserisco l'ultima cartella, visto che il file non termina con riga vuota
    cartelle.append(cartella)
    return tabellone, cartelle


# Questa funzione ricorsiva prende in input la lista delle cartelle, il numero estratto, e un valore per segnare il numero uscito
# Non resituisce output, modifica però ogni occorrenza del numero estratto con il valore per segnare
def segnoNum(cartelle, num, segno):
    for index, item in enumerate(cartelle):
        if type(item) == list:
            segnoNum(item, num, segno)
        else:
            if item == num:
                cartelle[index] = segno


# Soluzione alla parte1 del giorno3
# Ritorno la cartella vincente e l'ultimo numero estratto
def parte1(tabellone, cartelle):
    for num in tabellone:
        segnoNum(cartelle, num, 'X')
        for c in cartelle:
            # Scorro le righe per controllare bingo in orizzontale
            for l in c:
                if l == bingo:
                    return(c, num)
            # Scorro le colonne per controllare bingo in verticale
            for i in range(len(c)):
                if c[0][i] == c[1][i] == c[2][i] == c[3][i] == c[4][i]:
                    return(c, num)
    # Gestione possibile assenza di vincitori
    return None, 'Nessun vincitore'

# Soluzione alla parte1 del giorno3
# Ritorno l'ULTIMA cartella vincente e l'ultimo numero estratto
def parte2(tabellone, cartelle):
    ultimo_vincitore = []
    ultimo_num = ''
    for num in tabellone:
        segnoNum(cartelle, num, 'X')        
        for c in cartelle:
            bingo_orizzontale = False
            print('sono in cart')
            for l in c:
                if l == bingo:
                    # Mi segno l'attuale cartella vincente e il relativo numero
                    # Poi rimuovo la cartella dalla lista, ha già vinto non mi interessa controllarla successivamente
                    # Breako il ciclo perché non mi interessa controllare le righe seguenti
                    ultimo_vincitore = c
                    ultimo_num = num
                    cartelle.remove(c)
                    bingo_orizzontale = True
                    break
            # Se non ho trovato un bingo in orizzontale devo controllare anche le colonne
            if not bingo_orizzontale:
                for i in range(len(c)):
                    if c[0][i] == c[1][i] == c[2][i] == c[3][i] == c[4][i]:
                        # Anche qui mi segno l'attuale vincente, numero. Poi breako
                        ultimo_vincitore = c
                        ultimo_num = num
                        cartelle.remove(c)
                        break
    # Gestione possibile assenza di vincitori
    if len(ultimo_vincitore):
        return ultimo_vincitore, ultimo_num
    return None, 'Nessun vincitore'
    

tabellone, cartelle = getCartelle('input.txt')
#vincitore, num = parte1(tabellone, cartelle)
vincitore, num = parte2(tabellone, cartelle)
# Se ho trovato un vincente (primo o ultimo che sia), calcolo il prodotto richiesto
if type(vincitore) == list:
    somma_non_segnati = 0
    for l in vincitore:
        for n in l:
            if n != 'X':
                somma_non_segnati += int(n)
    print(somma_non_segnati * int(num))
