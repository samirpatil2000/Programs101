package main
import (
	"fmt"
)

func main() {
	x := 5
	fmt.Println("This is the address", &x)
	increment(&x)
	fmt.Println("Hello X", x)
	
}

func increment(x *int){
	*x += 1
}