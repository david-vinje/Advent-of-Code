$input = Get-Content -Path ./aoc-2022/input/day2.txt 

enum Hand {
  Paper
  Scissors
  Rock 
}

function ParseLine {
  param ($MatchUp)
  $Opponent = Transform($MatchUp[0])
  $Me = Transform($MatchUp[1])
  return @($Opponent, $Me)
}

function Transform {
  param ($Hand) 
  if ($Hand -eq "A" -or $Hand -eq "X") {
    return Rock
  }
  if ($Hand -eq "B" -or $Hand -eq "Y") {
    return Paper
  }
  if ($Hand -eq "C" -or $Hand -eq "Z") {
    return Scissors
  }
  return $null
}

foreach ($line in $input) {
  ParseLine($line.Split())
}