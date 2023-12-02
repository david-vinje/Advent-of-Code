// read input
let input = System.IO.File.ReadAllText("aoc-2015/input/day1.txt").ToCharArray()

// part one
input |> Array.fold (fun acc elem -> (if elem = '(' then 1 else -1) + acc) 0

// part two
let rec getPos floor (ins: array<char>) pos =
    match floor < 0 with
    | false -> 
        if ins[pos] = '(' 
        then getPos (floor+1) ins (pos+1)
        else getPos (floor-1) ins (pos+1)
    | true -> pos

getPos 0 input 0