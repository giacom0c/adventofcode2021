$VecchioPesce = 6
$NuovoPesce = 8
$Conta = 0
$Giorni = 80
# Leggo l'input dal file, inserisco i vari numeri in un array
Get-Content .\input.txt | ForEach-Object {
	$Pesci = $_.Split(",")
}
# Ciclo i giorni richiesti
While ($Giorni -gt 0) {
    # Scorro i pesci e decremento i relativi contatori
    # se trovo uno 0, lo reinizializzo a 6 e segno un nuovo pesce 
	For ($j = 0; $j -lt $Pesci.Length; $j++) {		
		If ($Pesci[$j] -gt 0) {
			$Pesci[$j] -= 1
		}
		Else {
			$Pesci[$j] = $VecchioPesce
			$Conta += 1
		}
	}
    # Aggiungo i pesci all'array
	While ($Conta -gt 0) {
		$Pesci += $NuovoPesce
		$Conta -= 1
	}
	$Giorni -= 1
    # Echo di debug: mi dice quanti giorni mancano al termine
	echo $Giorni
}
echo $Pesci.Length