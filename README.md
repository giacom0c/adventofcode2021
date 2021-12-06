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

Parte 2: Il task si risolve facilmente con una funzione ricorsiva. Considerando che non sono ancora molto capace col PowerShell in questi termini, l'ho implementata in Python. Magari prossimamente potrei fare una "traduzione" (oppure fatemi una merge request col vostro codice :grin:).
Tornando a noi: la logica "a eliminazione" ben si presta alla ricorsione. Ho strutturato la funzione nel seguente modo:
- La lista dei numeri binari ne contiene uno solo? Ok, allora ho trovato la risposta e la ritorno.
- Ce ne sono due o più? Controllo la *n-sima* cifra binaria (partendo da sinistra) e divido in due liste i numeri che hanno lo 0 o l'1.
    - A seconda del tipo di valore che sto cercando, richiamo la mia funzione passando la lista dei valori più (o meno) frequenti e *n+1*.
    - Ripetere i passi sopra.
---

## Giorno 4 Python
[Testo originale](https://adventofcode.com/2021/day/3)

La sfida di oggi richiede di gestire un bingo! Concettualmente molto semplice da capire, il problema sta nell'implementazione del tutto.

Come struttura dati per la gestione delle varie cartelle ho usato una lista di liste di liste:
- Lista "esterna": contenitore delle cartella. Il file di input contiene 1000 cartelle.
- Lista "cartella": rappresenta la singola cartella. Ognuna ha 5 righe all'interno
- Lista "riga": indica una singola riga di una cartella. Contiene 5 diversi numeri.

Per segnarmi i numeri estratti, ho utilizzato una funzione ricorsiva. [Fonte stackoverflow](https://stackoverflow.com/a/24516475/9851915)

Di per sé la funzione non ritorna nulla, ma applica una sostituzione *in place* del numero estratto con una *X*.

Il controllo della cartella vincente viene applicato semplicemente controllando le righe (se non ho trovato nulla anche le colonne) di tutte le cartelle. Trovata la vincente la ritorno e procedo a fare la somma dei numeri non estratti (in pratica i valori diversi da *X*), moltiplicando questo valore per l'ultimo numero estratto. Fun fact: questo è l'unico momento in cui converto i valori da stringa a numero intero.

La parte 2 della challenge ci chiede invece di trovare L'ULTIMA cartella vincente!

Quasi tutta la logica non cambia, l'unica cosa da tener conto è non ritornare subito la cartella vincente, bensì salvarsela (la rimuovo però dalla lista generale delle cartelle, ormai ha vinto e quindi non devo controllarla successivamente) e aggiornarla ogniqualvolta che esce un nuovo numero in caso di bingo. L'ultima rimasta sarà quella corretta.

---

## Giorno 5 WIP
[Testo originale](https://adventofcode.com/2021/day/5)

:construction_worker: :construction_worker: :construction_worker:

---

## Giorno 6 PowerShell
[Testo originale](https://adventofcode.com/2021/day/6)

Il task di oggi richiede di gestire la crescita di una popolazione di pesci su un certo periodo. Il testo è molto chiaro, ma facendo runnare lo script base (quello che ho chiamato `lento.ps1`) ci accorgiamo presto che non è così facile come sembrava.

I pesci infatti si riproducono piuttosto velocemente, andando a occupare molto spazio nell'array dedicato al loro tracciamento. Tutto ciò si traduce in una enorme lentezza, in quanto avviene una crescita di spazio a livello pseudo-esponenziale. Facendo un conto a spanne, **ogni 9 giorni la popolazione di pesci raddoppia**. Tenendo questo a mente, la prima implementazione *naive* impiega circa 2 ore per simulare 80 giorni! Per i 256 giorni richiesti dalla seconda parte credo che serva un tempo immane, per cui occorre affrontare il problema in modo diverso.

È davvero necessario tenere a mente lo stato di ogni singolo pesce, andando quindi ad allungare in modo indefinito il nostro array? In realtà, pensandoci bene, se nel giorno *X* ho 3 pesci con timer 4, al giorno *X+1*, avrò 3 pesci con timer 3, quindi possiamo usare come struttura dati di appoggio un semplice array con 9 slot, una per ogni possibile timer. Ogni giorno andiamo a contare i pesci attuali, e useremo quello come base per il giorno seguente. Per una corretta risoluzione, è importante aggiornare nel modo giusto le posizioni 6 e 8 del nostro array contatore, rispettivamente i pesci vecchi "rigenerati" e i pesci nuovi.

---

**TODO**: Indice