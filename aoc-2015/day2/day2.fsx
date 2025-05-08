open System.IO

type Box =
    { Length: int; Width: int; Height: int }

let toBox length width height =
    { Box.Length = length;
        Box.Width = width;
        Box.Height = height }

let input =
    File.ReadAllLines(Path.GetFullPath(".") + "/input/day2.txt")
    |> Array.toList
    |> List.map (fun str -> str.Split("x") |> Array.toList |> List.map int)
    |> List.map (fun lst -> toBox lst[0] lst[1] lst[2])

let computeArea box =
    let sideA = box.Length * box.Width
    let sideB = box.Length * box.Height
    let sideC = box.Width * box.Height
    let shortestSide = [sideA; sideB; sideC] |> List.sort |> List.head
    2 * (sideA + sideB + sideC) + shortestSide
    
let partOne = 
    input 
    |> List.map computeArea 
    |> List.sum

let computeArea' box =
    let shortestSides = [box.Length; box.Height; box.Width] |> List.sort
    let ribbon = box.Length * box.Width * box.Height
    2 * (shortestSides[0] + shortestSides[1]) + ribbon

let partTwo = 
    input 
    |> List.map computeArea'
    |> List.sum