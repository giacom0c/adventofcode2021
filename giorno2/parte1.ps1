$Depth = 0
$Distance = 0
# Scorro il file riga per riga
Get-Content .\input.txt | ForEach-Object {
  # Divido ogni riga con Split() e ottengo un array con 2 elementi, in posizione 0 la mossa, in posizione 1 il valore
	$Move = $_.Split()
  # Controllo tutte le possibili mosse e stampo errore in caso di mossa non riconosciuta
	if ($Move -eq "up") {
		$Depth = $Depth - $Move[1]
	}
	elseif ($Move -eq "down") {
		$Depth = $Depth + $Move[1]
	}
	elseif ($Move -eq "forward") {
		$Distance = $Distance + $Move[1]
	}
	else {
		echo "Mossa non riconosciuta nella lettura del file"
	}
}
# Stampo il risultato finale
echo $($Depth * $Distance)
