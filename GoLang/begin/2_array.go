package main


import (
	"fmt"
)


func mapCreation() map[string]string {
	dictionary := make(map[string]string)
	dictionary["name"] = "Samir"
	dictionary["age"] = "22"
	dictionary["gender"] = "male"

	// fmt.Println("Dictionary => ", dictionary)
	// fmt.Println("Name => ", dictionary["name"])
	return dictionary
}


func main()  {
	var a [3]int
	arr := []int{1, 2, 3, 4}
	fmt.Println("Array => ", a, arr)
	newArr := append(arr, 5)
	fmt.Println("New Array => ", newArr)
	fmt.Println("Map", mapCreation())
}