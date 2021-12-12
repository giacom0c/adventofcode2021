# Array che contiene i valori di ogni pesci: lo inizializzo con tutti 0
$Contatore = @()
For ($i = 0; $i -lt 9; $i++) {
	$Contatore += 0
}
$Giorni = 256
# Leggo l'input dal file, inserisco i vari numeri in un array
Get-Content .\input.txt | ForEach-Object {
	$Pesci = $_.Split(",")
}
# Reinizializzo l'array dei contatori con i valori iniziali
For ($i = 0; $i -lt $Pesci.Length; $i++) {
	$Temp = $Pesci[$i]
	$Contatore[$Temp] += 1
}
# Ciclo i giorni richiesti
While ($Giorni -gt 0) {
    $NuovoPesce = $Contatore[0]
    # "Scorro" i valori verso sinistra, poi aggiorno con i nuovi pesci
    For ($i = 0; $i -lt $Contatore.Length - 1; $i++) {
        $Contatore[$i] = $Contatore[$i + 1]
    }
    $Contatore[8] = $NuovoPesce
    $Contatore[6] += $Contatore[8]
    $Giorni -= 1
}
$Totale = 0
# Calcolo la somma finale
$Contatore | ForEach {
    $Totale += $_
}
echo $Totale