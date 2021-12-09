# Funzione che restituisce il file di input parsato
def get_signals(filename):
    signal_patterns = []
    with open(filename, 'r') as file:
        for line in file:
            signals = []
            sx, dx = line.strip().split('|')
            signals.append(sx.split())
            signals.append(dx.split())
            signal_patterns.append(signals)
    return signal_patterns


def parte1(signal_patterns):
    conta = 0
    # I numeri da cercare in questo caso sono decifrabili guardando la lunghezza
    for signal in signal_patterns:
        for s in signal[1]:
            if len(s) <= 4 or len(s) == 7:
                conta += 1
    print(conta)


def parte2(signal_patterns):
    totale = 0
    for signal in signal_patterns:
        # Ordino per lunghezza i pattern da decifrare
        temp = sorted(signal[0], key=len)
        # Lista "posizionale" dove vado a inserire nello slot giusto il numero decodificato
        decoded = ['', '', '', '', '', '', '', '', '', '']
        # I primi 3 pattern (i più corti) corrispondono alle cifre 1, 7, 4. L'ultimo (più lungo) è la cifra 8
        # Una volta individuati, li elimino dalla lista. Restano quindi 0, 2, 3, 5, 6, 9
        decoded[1] = sorted(temp.pop(0))
        decoded[7] = sorted(temp.pop(0))
        decoded[4] = sorted(temp.pop(0))            
        decoded[8] = sorted(temp.pop())
        # 0, 6, 9 occupano gli ultimi 3 posti della lista temp
        for t in temp[-3:]:
            # Se il pattern di 1 è incluso, allora è 0 o 9, altrimenti è 6
            if decoded[1][0] in t and decoded[1][1] in t:
                conta = 0
                # Se il pattern di 4 è incluso, allora è 9, altrimenti è 0
                for n in decoded[4]:                    
                    if n in t:
                        conta += 1
                if conta == 4:
                    decoded[9] = sorted(t)
                else:
                    decoded[0] = sorted(t)
            else:
                decoded[6] = sorted(t)
        # Restano 2, 3, 5: occupano i primi 3 posti della lista temp
        for t in temp[:3]:
            conta = 0
            #Se il pattern di 7 è incluso, allora è 3, altrimenti è 2 o 5
            for n in decoded[7]:                
                if n in t:
                    conta += 1
            if conta == 3:
                decoded[3] = sorted(t)
            else:
                # Se il pattern differisce di un solo valore rispetto a quello di 6, è 2, altrimenti è 5
                if len(set(sorted(t)) - set(decoded[6])) == 1:
                    decoded[2] = sorted(t)
                else:
                    decoded[5] = sorted(t)
        codice = ''
        for s in signal[1]:
            # Scorro la lista dei pattern decodificati e li confronto con la parte dx dell'input
            # Itero e calcolo il totale
            for i in range(len(decoded)):
                if decoded[i] == sorted(s):
                    codice += str(i)
        totale += int(codice)
    print(totale)                    


filename = 'input.txt'
signals = get_signals(filename)
parte1(signals)
parte2(signals)
