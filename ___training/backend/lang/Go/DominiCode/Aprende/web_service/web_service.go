package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Dominicode")
}

func main() {
	http.HandleFunc("/", handler)
	log.Println("Server on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
