$Max = 0
$Min = [int]::MaxValue
Get-Content .\input.txt | ForEach-Object {
	$Granchi = $_.Split(",")
}
# Scorro la lista dei valori di input e cerco il numero più grande
$Granchi | ForEach {
	If ([int]$_ -gt $Max) {
		$Max = [int]$_
	}
}
# Approccio bruteforce: scorro da 0 fino al Max number
For ($i = 0; $i -le $Max; $i++) {
	$Fuel = 0
    # Provo tutti i valori, e per ognuno calcolo la spesa di carburante
	For ($j = 0; $j -lt $Granchi.Length; $j++) {
		$Fuel += [Math]::Abs($i - $Granchi[$j])
	}
    # A ogni ciclo aggiorno con il minore
	If ($Fuel -lt $Min) {
		$Min = $Fuel
	}
}
echo $Min