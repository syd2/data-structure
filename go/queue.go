package main

import "fmt"

func main() {
	var queue Queue
	for i := 1; i < 9; i++ {
		queue.Enqueue(i)
	}
	fmt.Println(queue)
	fmt.Println(queue.Len())
	queue.Dequeue()
	queue.Dequeue()
	fmt.Println(queue)

}

type Queue []interface{}

func (q *Queue) Enqueue(val interface{}) interface{} {
	*q = append(*q, val)
	return val
}

func (q *Queue) Dequeue() interface{} {
	*q = (*q)[1:]
	return (*q)[0]
}

func (q *Queue) isEmpty() bool {
	if len(*q) == 0 {
		return true
	}
	return false
}
func (q *Queue) Len() int {
	return len(*q)
}
