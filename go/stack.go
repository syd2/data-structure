package main

import "fmt"

func main() {

	var stack Stack
	stack.Push(10)
	stack.Push(20)
	stack.Push(40)
	fmt.Println(stack)
	stack.Pop()
	fmt.Println(stack)
	fmt.Println(stack.Len())

}

type Stack []interface{}

func (s *Stack) Push(val interface{}) interface{} {
	*s = append(*s, val)
	return val
}

func (s *Stack) Pop() interface{} {
	*s = (*s)[:len(*s)-1]
	return (*s)[len(*s)-1]
}
func (s *Stack) Len() int {
	return len(*s)
}
func (s *Stack) isEmpty() bool {
	if len(*s) == 0 {
		return true
	}
	return false
}
