# adventofcode2021
Le mie soluzioni alla challenge 2021 di adventofcode.com.

---

## Giorno 1 Bash
[Testo originale](https://adventofcode.com/2021/day/1)

Task molto base, per entrambe le parti è sufficiente ciclare la lista dei valori e confrontare il corrente (o una somma di essi) con il precedente. Prima di eseguire gli script, dare i permessi necessari con `chmod +x giorno1/parte*`.

**Nota**: ho aggiunto un "\n" (a capo) al file di input, altrimenti non viene letto il valore nell'ultima riga.

---

## Giorno 2 PowerShell
[Testo originale](https://adventofcode.com/2021/day/2)

Altro task piuttosto semplice, pure più di quello del primo giorno a mio parere. Anche qui è sufficiente leggere il file riga per riga e incrementare dei contatori in base ai valori letti, con un normale flusso `if .. elseif .. else`. I commenti di `parte2.ps1` non sono inclusi perché fondamentalmente identici a quelli di `parte1.ps1`.

---

## Giorno 3 PowerShell / Python
[Testo originale](https://adventofcode.com/2021/day/3)

Prima parte più facile, seconda un minimo complessa, tanto da dover sfoderare il Python :smirk:

Per la prima parte, è sufficiente sommare i vari numeri colonna per colonna. Alla fine, se il numero di ogni colonna è maggiore alla metà delle righe del file di input, quella colonna varra 1, altrimenti 0. A questo punto si convertono i binari ottenuti in questo modo in base 10 e si moltiplicano fra loro per il risultato finale.

Parte 2: Writeup in arrivo...

---