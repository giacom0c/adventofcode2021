$Gamma = $Epsilon = ''
# Leggo la prima riga del file (mi serve per capire la grandezza dei numeri binari)
$Binario = Get-Content input.txt -First 1
# Ottengo il totale dei numeri binari
$Righe = Get-Content input.txt | Measure-Object -line | Select-Object Lines
# Creo un array e lo inizializzo con N zeri in base alle cifre del binario letto in precedenza
$Array = @()
For ($i = 0; $i -lt $Binario.Length; $i++) {
	$Array += 0
}
# Scorro il file
Get-Content .\input.txt | ForEach-Object {
  # Spezzo ogni riga per leggere i caratteri singolarmente
	$Temp = $_.ToCharArray()
	For ($i = 0; $i -lt $Array.Length; $i++) {
    # Converto in int e accumulo i valori
		$Array[$i] = $Array[$i] + [int][string]$Temp[$i]
	}
}
# Riesamino i valori per costruire Gamma ed Epsilon
For ($i = 0; $i -lt $Array.Length; $i++) {
	If ($Array[$i] -gt $Righe.Lines / 2) {
		$Gamma = -join($Gamma, '1')
		$Epsilon = -join($Epsilon, '0')
	}
	Else {
		$Gamma = -join($Gamma, '0')
		$Epsilon = -join($Epsilon, '1')
	}
}
# Conversione da stringa in base 2 a int
$GInt = [Convert]::ToInt32($Gamma, 2)
$EInt = [Convert]::ToInt32($Epsilon, 2)
echo $Gamma $Epsilon
echo $($GInt * $EInt)
