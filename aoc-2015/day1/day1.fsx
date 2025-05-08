open System.IO

let path = Path.GetFullPath(".")

type Floor =
    | Down
    | Up

let parse floor =
    match floor with
    | '(' -> Up
    | _ -> Down

let count floor =
    match floor with
    | Up -> 1
    | Down -> -1

let floors =
    File.ReadAllText(path + "/input/day1.txt").ToCharArray()
    |> Array.map parse
    |> Array.map count

let partOne = floors |> Array.sum

let partTwo =
    let rec aux floor indx =
        match floor < 0 with
        | true -> indx
        | _ -> aux (floor + floors.[indx]) (indx + 1)

    aux 0 0
