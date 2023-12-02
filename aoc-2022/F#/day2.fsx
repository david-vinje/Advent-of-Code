let lines =
    System.IO.File.ReadAllLines("input/day2.txt")
    |> Array.map (fun s -> s.Split " ")
    |> Array.map (fun arr -> (arr.[0]), (arr.[1]))

type Hand = Rock | Paper | Scissors 

let parseLine (A, B) = 
    match A, B with
    | "A", "X" -> Rock, Rock
    | "A", "Y" -> Rock, Paper
    | "A", _ -> Rock, Scissors
    | "B", "X" -> Paper, Rock
    | "B", "Y" -> Paper, Paper
    | "B", _ -> Paper, Scissors
    | _, "X" -> Scissors, Rock
    | _, "Y" -> Scissors, Paper
    | _, _ -> Scissors, Scissors

let battle (A, B) = 
    match B, A with
    | Rock, Rock -> 1 + 3
    | Rock, Paper -> 1 + 0
    | Rock, Scissors -> 1 + 6
    | Paper, Rock -> 2 + 6
    | Paper, Paper -> 2 + 3
    | Paper, Scissors -> 2 + 0
    | Scissors, Rock -> 3 + 0
    | Scissors, Paper -> 3 + 6
    | Scissors, Scissors -> 3 + 3

let partOne = 
    lines
    |> Array.map parseLine
    |> Array.fold 
        (fun acc elem ->
            let score = battle elem 
            let res = score + acc
            res
        ) 0

partOne

let reparseLine (A, B) = 
    match A, B with
    | "A", "X" -> Rock, Scissors
    | "A", "Y" -> Rock, Rock
    | "A", _ -> Rock, Paper
    | "B", "X" -> Paper, Rock
    | "B", "Y" -> Paper, Paper
    | "B", _ -> Paper, Scissors
    | _, "X" -> Scissors, Paper
    | _, "Y" -> Scissors, Scissors
    | _, _ -> Scissors, Rock
let partTwo = 
    lines
    |> Array.map reparseLine
    |> Array.fold 
        (fun acc elem ->
            let score = battle elem 
            let res = score + acc
            res
        ) 0

partTwo