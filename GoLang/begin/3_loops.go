package main

import (
	"fmt"
)


func main(){
	// for i := 0; i < 3; i++ {
	// 	fmt.Println(i)
	// }
	// arr := []string{"samir", "hello"}
	// for index, value := range arr {
	// 		fmt.Println(index, value)
	// }

	dictionary := make(map[string]int)
	dictionary["id"] = 2
	for key, value := range dictionary {
		fmt.Println(key, value)
	}
}