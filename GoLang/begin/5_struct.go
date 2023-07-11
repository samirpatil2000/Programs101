package main

import (
	"fmt"
)


type Person struct {
	Name string
	Age int
}

func main() {
	p := Person{Name: "Samir", Age: 22}
	fmt.Println(p.Age)
}