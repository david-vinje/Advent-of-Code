// FS er ikke bare funktioner, det er også stærke typesystemer.
// Udover de sædvanelige primitive typer, void/unit typer, funktioner og generiske typer, så har vi også
// * Tuples og records (product types)
// * Unions, options og enums (sum types). 

// OOP fokuserer tit på adfærd fremfor data og bruger polymorfi til duck-typing.
// FS har derimod fokus på data typer fremfor adfærd. 
// De bruges både til annotering og compile-time checks, men også som domæner til data modellering. 

// F# bruger både CLI typer: value types, reference types, grouping/structs, klasser, interfaces, delegates, arrays.
// Men også sine enge F# typer: funktioner, unit, tuples, records, unions, options og lists. 
// Man skal stile efter at bruge F# typerne. 

// Det vigtige ved typer er at forstå, at de kan sammensættes af andre typer - og at de består af product og sum types. 

// Alias: 
type Name = string
type Coordinates = int * int
type transform<'a> = 'a -> 'b

// Tuple
let coordinates = (1, 2)

// Record
type Player = { name: Name; coordinates: Coordinates }
