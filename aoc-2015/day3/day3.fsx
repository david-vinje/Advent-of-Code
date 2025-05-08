// read input
let input = System.IO.File.ReadAllText("aoc-2015/input/day3.txt").ToCharArray()

// part one
let move (r, c) elem =
    match elem  with
    | '<' -> (r, c-1)
    | '>' -> (r, c+1)
    | '^' -> (r-1, c)
    | _  -> (r+1, c)
    
let rec partOne arr pos i S =
    match Array.length arr = i with
    | true -> Set.count S
    | false -> 
        let newPos = move pos arr[i]
        partOne arr newPos (i+1) (Set.add newPos S)

let S = Set.empty.Add((0, 0))
partOne input (0,0) 0 S
    
let rec partTwo arr one two i S =
    match Array.length arr = i with
    | true -> Set.count S
    | false -> 
        let one' = move one arr[i]
        let two' = move two arr[i+1]
        let S': Set<int * int> = (Set.add one' S).Add two'
        partTwo arr one' two' (i+2) S'

let S' = Set.empty.Add((0, 0))
partTwo input (0,0) (0,0) 0 S'