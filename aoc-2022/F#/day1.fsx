let sums = 
    System.IO.File.ReadAllText("aoc-2022/input/day1.txt")
    |> fun s -> s.Split "\n\n"        
    |> Array.map (fun s -> s.Split "\n")
    |> Array.map (Array.map int)
    |> Array.map Array.sum

let partOne = 
    sums
    |> Array.max
    
let partTwo = 
    sums 
    |> Array.sortDescending
    |> Array.take 3
    |> Array.sum