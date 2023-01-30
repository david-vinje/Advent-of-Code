let lines =
    System.IO.File.ReadAllLines("aoc-2022/input/day2.txt")
    |> Array.map (fun s -> s.Split " ")

let partOne =
    lines
    |> Array.fold (fun acc elem -> 
        if elem.[0] = "A" then
            if elem.[1] = "X" then 1+3+acc
            elif elem.[1] = "Y" then 2+6+acc
            else 3+0+acc
        elif elem.[0] = "B" then
            if elem.[1] = "X" then 1+0+acc
            elif elem.[1] = "Y" then 2+3+acc
            else 3+6+acc
        else
            if elem.[1] = "X" then 1+6+acc
            elif elem.[1] = "Y" then 2+0+acc
            else 3+3+acc) 0

let partTwo =
    lines
    |> Array.fold (fun acc elem -> 
        if elem.[1] = "X" then
            if elem.[0] = "A" then 0+3+acc
            elif elem.[0] = "B" then 0+1+acc
            else 0+2+acc
        elif elem.[1] = "Y" then
            if elem.[0] = "A" then 3+1+acc
            elif elem.[0] = "B" then 3+2+acc
            else 3+3+acc
        else
            if elem.[0] = "A" then 6+2+acc
            elif elem.[0] = "B" then 6+3+acc
            else 6+1+acc) 0
