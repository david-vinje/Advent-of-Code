let lines = 
    System.IO.File.ReadAllText("aoc-2022/input/day1.txt")
    |> fun s -> s.Split "\n\n"        
    |> Array.map (fun s -> s.Split "\n")
    |> Array.map (Array.map int)
    |> Array.map Array.sum
    |> Array.max