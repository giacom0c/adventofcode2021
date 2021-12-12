#!/bin/bash

# L'input è lo stesso della parte 1 -> https://adventofcode.com/2021/day/1/input
input="input.txt"
risposta=0
# Preparo un array per contenere i valori del file
lista=()
# Scorro il file e inserisco ogni valore nell'array
while IFS= read -r line
do
    lista+=($line)
done < "$input"
# Inizializzo con la somma dei primi 3 valori
prev=$((${lista[0]} + ${lista[1]} + ${lista[2]}))
# Nota: fermo il ciclo 3 numeri prima (e parto da 1 anziché da 0)
for ((i=1; i<=${#lista[@]}-3;i++)); 
do
    temp=$((${lista[$i]} + ${lista[$i+1]} + ${lista[$i+2]}))
    # Se il valore della somma attuale è maggiore della precedente, incremento di 1 la risposta
    if [[ $temp -gt $prev ]]
    then
        risposta=$(($risposta+1))
    fi
    # Aggiorno la somma precedente per il confronto successivo
    prev=$temp
done
echo $risposta

#TODO: Migliorare il codice dinamicizzandolo per una finestra di N valori (ora come ora è hardcodato a 3)