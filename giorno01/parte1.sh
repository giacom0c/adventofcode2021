#!/bin/bash

# Prendere l'input da -> https://adventofcode.com/2021/day/1/input (necessario login utente adventofcode.com)
input="input.txt"
risposta=0
# Inizializzo con il primo valore del file
prev=$(head -n 1 $input)
# Leggo il file scorrendo riga per riga
while IFS= read -r line
do
    # Se il valore della riga attuale è maggiore del precedente, incremento di 1 la risposta
    if [[ $line -gt $prev ]]
    then
        risposta=$(($risposta+1))
    fi
    # Aggiorno il valore precedente per il confronto successivo
    prev=$line
done < "$input"
echo $risposta