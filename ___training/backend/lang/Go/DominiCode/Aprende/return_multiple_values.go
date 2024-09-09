package main

import "fmt"

func main() {
	result, ok := divide(100, 50)
	fmt.Println(result, ok)
}

func divide(a, b int) (result int, ok bool) {
	if b == 0 {
		// return 0, false
		return
	}

	// return a / b, true
	result = a / b
	ok = true
	return
}
