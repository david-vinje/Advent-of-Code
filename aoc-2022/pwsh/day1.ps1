$list = Get-Content -Path /Users/davidvinje/Developer/Advent-of-Code/aoc-2022/input/day1.txt

$tmp = [System.Collections.ArrayList]::new()
$sum = 0
foreach ($calories in $list) {
  $calories = [int]$calories
  if ($calories -eq 0) {
    [void] $tmp.Add($sum)
    $sum = 0
  }
  else {
    $sum += $calories
  }
}
[void] $tmp.Add($sum)

$tmp | Sort-Object -Descending -Top 1
($tmp | Sort-Object -Descending -Top 3 | Measure-Object -Sum).Sum