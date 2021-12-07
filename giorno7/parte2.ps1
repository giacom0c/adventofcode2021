$Max = 0
$Min = [int]::MaxValue
Get-Content .\input.txt | ForEach-Object {
	$Granchi = $_.Split(",")
}
$Granchi | ForEach {
	If ([int]$_ -gt $Max) {
		$Max = [int]$_
	}
}
For ($i = 0; $i -le $Max; $i++) {
	$Fuel = 0
	For ($j = 0; $j -lt $Granchi.Length; $j++) {
		$Temp = [Math]::Abs($i - $Granchi[$j])
        # Ricalcolo il costo del carburante usando la formula di Gauss
		$Fuel += $Temp * ($Temp + 1) / 2
	}
	If ($Fuel -lt $Min) {
		$Min = $Fuel
	}
	echo $Min
}
echo $Min