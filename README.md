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

## Giorno 5 Python
[Testo originale](https://adventofcode.com/2021/day/5)

Per il momento questo è stato il problema che ho trovato più complesso, tant'è che l'ho risolto solo al giorno 8 (e solo nella prima parte, per ora :confused:). La consegna di chiede di lavorare con una sorta di piano cartesiano e di tracciarvi vari segmenti: lo scopo di tutto ciò è scoprire i punti di intersezione di 2 o più segmenti e contarli andandoli a sommare tutti.

Concettualmente è piuttosto chiaro, ciò che mi sfuggiva era come rappresentare questa mappa. Ho pensato a matrici, strutture con *numpy*, ecc. Dopo qualche ricerca, ho scoperto il *defaultdict*, che ci permette di avere una struttura nativamente inizializzata con degli 0 e soprattutto flessibile, in modo da non doverci andare a cercare il numero *M* (max) per costruire staticamente una griglia *M\*M*.

Parsiamo ogni riga del file di input in modo da avere 4 coordinate per ogni riga: 2 per l'ascissa e 2 per l'ordinata, in pratica abbiamo così ottenuto due punti: inizio e fine del segmento da tracciare. La parte 1 dell'esercizio prevede **solo segmenti vertiicali od orizzontali** (quindi con stessi *x* o *y*).

Parte 2 :construction_worker: :construction_worker: :construction_worker:

---

## Giorno 6 PowerShell
[Testo originale](https://adventofcode.com/2021/day/6)

Il task di oggi richiede di gestire la crescita di una popolazione di pesci su un certo periodo. Il testo è molto chiaro, ma facendo runnare lo script base (quello che ho chiamato `lento.ps1`) ci accorgiamo presto che non è così facile come sembrava.

I pesci infatti si riproducono piuttosto velocemente, andando a occupare molto spazio nell'array dedicato al loro tracciamento. Tutto ciò si traduce in una enorme lentezza, in quanto avviene una crescita di spazio a livello pseudo-esponenziale. Facendo un conto a spanne, **ogni 9 giorni la popolazione di pesci raddoppia**. Tenendo questo a mente, la prima implementazione *naive* impiega circa 2 ore per simulare 80 giorni! Per i 256 giorni richiesti dalla seconda parte credo che serva un tempo immane, per cui occorre affrontare il problema in modo diverso.

È davvero necessario tenere a mente lo stato di ogni singolo pesce, andando quindi ad allungare in modo indefinito il nostro array? In realtà, pensandoci bene, se nel giorno *X* ho 3 pesci con timer 4, al giorno *X+1*, avrò 3 pesci con timer 3, quindi possiamo usare come struttura dati di appoggio un semplice array con 9 slot, una per ogni possibile timer. Ogni giorno andiamo a contare i pesci attuali, e useremo quello come base per il giorno seguente. Per una corretta risoluzione, è importante aggiornare nel modo giusto le posizioni 6 e 8 del nostro array contatore, rispettivamente i pesci vecchi "rigenerati" e i pesci nuovi.

---

## Giorno 7 PowerShell
[Testo originale](https://adventofcode.com/2021/day/7)

L'enigma di oggi è abbastanza particolare, ma in soldoni si tratta di un **problema di ottimizzazione**: data una serie di numeri in input, bisogna manipolarli affiché si ottenga una somma più bassa possibile. Precisamente l'esercizio ci richiede di renderli tutti uguali fra loro, quindi vanno incrementati o decrementati, a seconda che siano rispettivamente minori o maggiori del numero target da raggiungere.

La mia soluzione utilizza un approccio *bruteforce*, probabilmente non la soluzione più elegante o rapida, ma è la prima che mi è venuta in mente e, provandola, ho visto che ha funzionato. :grin:

La complessità in tempo dell'algoritmo usato = *O(M\*N) + N*, dove *M* è uguale al numero più grande fra quelli nella lista in input e *N* è la lunghezza della lista in input.

Per quanto riguarda la parte 2, il procedimento è fondamentalmente identico, cambia solo come viene contato il raggiungimento del numero target, che diventa una somma (o differenza) incrementale. Per calcolare il nuovo valore, si può usare la [famosa formula di Gauss.](https://it.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%C2%B7_%C2%B7_%C2%B7)

---

## Giorno 8 Python
[Testo originale](https://adventofcode.com/2021/day/8)

La challenge di oggi sembra quasi uscita dalla settimana enigmistica! Lo scopo è quello di decifrare dei pattern per ricostruire dei numeri nel formato degli [orologi digitali](https://it.wikipedia.org/wiki/Display_a_sette_segmenti).

La prima parte è molto facile: si focalizza sulle cifre 1, 4, 7 e 8, che si differenziano rispetto alle altre perché rappresentabili con un numero univoco di segmenti digitali, rispettivamente 2, 4, 3, 7. Gli altri sei numeri usano 5 o 6 segmenti. Per trovare la soluzione è sufficiente quindi contare la lunghezza dei codici nella parte destra dell'input e contare le occorrenze di questi quattro numeri.

La seconda parte è decisamente più complessa, perché ci richiede di decodificare completamente ogni riga del file di input: la parte sinistra conterrà le 10 cifre in formato digitale, mentre la parte destra ne contiene quattro e bisogna decifrare di quale numero si tratta, una volta trovato il primo, ripetere il procedimento per ogni riga dele file di input e sommare fra loro tutti i valori ottenuti.

Abbiamo detto che le cifre 1, 4, 7 e 8 ci vengono date "gratis", basta contare la lunghezza del pattern. Come fare per gli altri 6 numeri?
- Se è lungo 6 caratteri e il pattern di 1 *non* è incluso, allora corrisponde sicuramente alla cifra 6.
- Se è lungo 6 caratteri (e non è 6) e il pattern di 4 *non* è incluso, allora corrisponde sicuramente alla cifra 0.
- Se è lungo 6 caratteri ma non è né 0 né 6, allora è la cifra 9.
- Se è lungo 5 caratteri e il pattern di 7 è incluso, allora è sicuramente la cifra 3.
- Se è lungo 5 caratteri (e non è 3) e differisce di un unico carattere rispetto al pattern di 6, allora è la cifra 2
- Se è lungo 5 caratteri ma non è né 2 né 3, allora è la cifra 5.

Una volta stabiliti questi vincoli il gioco è fatto! :wink:

---

## Giorno 9 Python
[Testo originale](https://adventofcode.com/2021/day/9)

L'esericizio di oggi prevede di **individuare dei minimi locali in una mappa 2D**. In pratica bisogna confrontare il valore di ogni "cella" con quello dei suoi 4 adiacenti. L'unica complicazione sta nel fatto che le celle agli angoli e sui bordi hanno rispettivamente 2 e 3 vicini.

La soluzione da me applicata è abbastanza brutale: per modellare la mappa 2D ho usato una lista di liste, dove la lista interna corrisponde a una riga del file di input. Per **ogni** valore controllo i suoi 4 vicini, se sono uscito dai limiti di una delle liste (quindi fuori dal perimetro della mappa), sollevo un'eccezione e semplicemente non faccio nulla, altrimenti mi segno il valore della cella adiacente presa in esame. Una volta trovati tutti i vicini, confronto il minore di essi con il valore corrente, se quest'ultimo è minore allora me lo segno. Il valore da ritornare come soluzione corrisponde alla somma di questi minimi più 1.

La seconda parte ci richiede di individuare delle aree contenenti numeri minori di 9. L'idea quindi è quella di trovare tutti i valori adiacenti validi dei vari numeri, e costruire quindi dei bacini. C'è un algoritmo che fa proprio al caso nostro, [si chiama flood fill](https://python.plainenglish.io/a-python-example-of-the-flood-fill-algorithm-bced7f96f569), ed è quello usato dal tool di paint che riempie un area con lo stesso colore (icona del secchiello). Tramite la ricorsione esploro la mappa e mi segno la dimensione dei vari bacini trovati. A questo punto per la soluzione ci richiedono di restituire il prodotto dei 3 bacini con dimensione maggiore.

---

## Giorno 10 Python
[Testo originale](https://adventofcode.com/2021/day/10)

Oggi bisogna parsare una **serie di parentesi**! Nel file di input ci vengono date delle sequenze di tutti i tipi di parentesi `<>()[]{}` e dobbiamo stabilirne due tipologie differenti:

- Quelle *corrotte*, ovvero sequenze dove c'è una mancata corrispondenza fra una parentesi aperta e una chiusa, per esempio apro la tonda ma la chiudo con la quadra.
- Quelle *incomplete*, qui non ci sono mismatch fra parentesi, bensì la sequenza termina senza che una o più parentesi venga chiusa correttamente.
Nel testo troviamo vari esempi di questi scenari possibili.

La soluzione sia per la parte 1 che 2 prevede l'uso di una pila (`deque` in python), dove vi andiamo a inserire tutte le parentesi aperte, poi quando incontriamo una chiusa la confrontiamo con il primo elemento della pila (che ha natura LIFO, *last in, first out*): se è la parentesi corrispondente le togliamo dalla pila, altrimenti abbiamo già trovato la corruzione della riga. Se arrivo fino in fondo senza trovare mismatch, allora è una sequenza incompleta (nel testo è specificato che sono incomplete o corrotte).

La parte 2 ci chiede di completare appunto queste sequenze. Anche qui è semplice, invertiamo la nostra pila e fondamentalmente abbiamo ottenuto il risultato richiesto.

---

## Giorno 11 Python
[Testo originale](https://adventofcode.com/2021/day/11)

Questo esercizio è concettualmente **molto simile a quello affrontato nel giorno 9**. Anche qui abbiamo una mappa 2D che ci richiede di interagire con le sue "celle" e relativi vicini. In questo caso però nei vicini si includono anche quelli in diagonale. Per la risoluzione viene usato un algoritmo praticamente uguale al flood fill.

Per la parte 2 è sufficiente ripetere il ciclo fino a quando tutti gli elementi della mappa vengono attivati con il "flash". Attenzione a non usare la stessa mappa della parte 2, perché si trova in uno stato avanzato, va rigenerato.

---

**TODO**: Indice