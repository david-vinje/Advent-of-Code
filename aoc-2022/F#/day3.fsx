System.IO.File.ReadAllLines("aoc-2022/input/day3.txt")
|> Array.map (fun s -> (s.Substring(0, s.Length/2), s.Substring(s.Length/2)))
|> Array.map (fun (a, b) -> (a.ToCharArray(), b))
|> Array.fold (fun acc elem -> 
    let a, b = elem
    let item = string (Array.filter (fun c -> b.Contains(string c)) a).[0]
    let value = if item = item.ToUpper() then int (char item) - 38 else int (char item) - 96 
    acc + value) 0

// int (char "A") - 38