// read input
let input = 
    System.IO.File.ReadAllLines("aoc-2015/input/day2.txt") 
    |> Array.map (fun s -> s.Split("x"))
    |> Array.map (fun a -> Array.map int a)

// part one
let area l w h = 
    let s1 = l*w
    let s2 = w*h
    let s3 = h*l
    2*s1 + 2*s2 + 2*s3 + min s1 (min s2 s3)

let partOne = 
    input 
    |> Array.map (fun (a: array<int>) -> area a[0] a[1] a[2])
    |> Array.sum

let area' (dims: array<int>) =
    let l, w, h = dims[0], dims[1], dims[2]
    let sorted = Array.sort dims
    l*w*h + sorted[0]*2 + sorted[1]*2

let partTwo =
    input 
    |> Array.map (fun (a: array<int>) -> area' a)
    |> Array.sum