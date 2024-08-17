package main

import "fmt"

func main() {
	var myArray [4]string
	fmt.Println(myArray)

	myArray = [4]string{"Angular", "React", "Vue", "Svelte"}
	fmt.Println(myArray)

	myArray[2] = "VueJS"
	fmt.Println(myArray[0])
	fmt.Println((myArray[2]))

	myArray2 := myArray
	myArray[2] = "Ember"

	fmt.Println(myArray)
	fmt.Println(myArray2)

	
}
