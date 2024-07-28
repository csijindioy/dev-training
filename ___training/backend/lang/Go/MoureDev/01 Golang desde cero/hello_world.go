package main

import (
	"container/list"
	"fmt"
	"reflect"
)

func main() {
	// Hola mundo

	/*
		Hola mundo
		en dos lineas
	*/

	fmt.Println("Hello GO World!")

	var myString string = "Esto es una cadena"
	fmt.Println(myString)

	myString = "Aqui cambio el valor de la cadena de texto"
	fmt.Println(myString)

	var myInt int = 7
	myInt = myInt + 4
	fmt.Println(myInt)
	fmt.Println(myInt - 1)
	fmt.Println(myInt)

	fmt.Println(myString, myInt)
	fmt.Println(reflect.TypeOf(myInt))

	var myFloat float64 = 6.5
	fmt.Println(myFloat)
	fmt.Println(reflect.TypeOf(myFloat))

	fmt.Println(float64(myInt) + myFloat)

	var myBool bool = false
	myBool = true
	fmt.Println(myBool)

	// Variable declarada e inicializada de manera abreviada
	myString3 := "Esto es una cadena de texto"
	fmt.Println(myString3)

	// Constantes
	const myConst = "Esto es una constante"
	fmt.Println(myConst)

	// Control de flujo
	if myInt == 10 {
		fmt.Println("El valor de myInt es 10")
	} else if myInt == 11 {
		fmt.Println("El valor de myInt es 11")
	} else {
		fmt.Println("El valor de myInt NO es ni 10 ni 11")
	}

	// && operador "and" lógico
	// || operador "or" lógico

	var myArray [3]int
	myArray[0] = 1
	myArray[1] = 2
	myArray[2] = 3
	fmt.Println(myArray)
	fmt.Println(myArray[2])

	// Map
	//myMap := make(map[string]int)
	myMap := map[string]int{"Brais": 36, "crais01": 35, "hoz98": 24}
	myMap["Brais"] = 36
	myMap["crais01"] = 35
	myMap["hoz98"] = 24
	fmt.Println(myMap)
	fmt.Println(myMap["Brais"])

	// List
	myList := list.New()
	myList.PushBack(1)
	myList.PushBack(2)
	myList.PushBack(3)
	fmt.Println(myList.Back().Value)

	// Bucles
	for i := 0; i < len(myArray); i++ {
		fmt.Println(myArray[i])
	}

	for key, value := range myMap {
		fmt.Println(key, value)
	}

	// Función
	// myFunction()
	fmt.Println(myFunction())

	// Estructura
	type MyStruct struct {
		name string
		age  int
	}

	myStruct := MyStruct{"Brais", 36}
	fmt.Println(myStruct)
}

// func myFunction() {
// 	fmt.Println("Mi función")
// }

func myFunction() string {
	return "Mi función"
}
