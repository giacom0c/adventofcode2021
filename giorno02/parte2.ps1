$Depth = 0
$Distance = 0
$Aim = 0
Get-Content .\input.txt | ForEach-Object {
	$Move = $_.Split()
	if ($Move -eq "up") {
		$Aim = $Aim - $Move[1]
	}
	elseif ($Move -eq "down") {
		$Aim = $Aim + $Move[1]
	}
	elseif ($Move -eq "forward") {
		$Distance = $Distance + $Move[1]
		$Depth = $Depth + $Aim * $Move[1]
	}
	else {
		echo "Mossa non riconosciuta nella lettura del file"
	}
}
echo $($Depth * $Distance)