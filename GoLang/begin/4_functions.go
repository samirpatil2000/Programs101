package main


import (
	"fmt"
	"errors"
	"math"
)


func main() {
	result, error := sqrtFunc(-5)
	if error == nil {
		fmt.Println(result)
	} else {
		fmt.Println(error)
	}
}

func sqrtFunc(x float64) (float64, error) {
	if x < 0 {
		return 0, errors.New("Invalid input ")
	}
	return math.Sqrt(x), nil
}