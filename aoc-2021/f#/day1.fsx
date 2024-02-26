let measurements = 
    System.IO.File.ReadAllLines("./input/day1.txt")
    |> Array.map int

let partOne arr = 
    Array.pairwise arr
    |> Array.fold (fun acc elem -> 
        if snd elem > fst elem
        then acc + 1 else acc) 0

// partOne measurements

let partTwo = 
    Array.windowed 3 measurements
    |> Array.map Array.sum
    |> partOne