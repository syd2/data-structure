package main

import "fmt"

func main() {
	fmt.Println()
	l1 := new(LinkedList)
	fmt.Println(l1)
	l1.PushToHead(2)
	l1.PushToHead(3)
	l1.PushToHead(4)
	l1.Append(5)
	l1.Print()
}

type node struct {
	data interface{}
	next *node
}

type LinkedList struct {
	head *node
}

func (l *LinkedList) PushToHead(val interface{}) {
	if l.head == nil {
		n := &node{data: val, next: l.head}
		l.head = n
	} else {
		new_node := new(node)
		new_node = l.head
		n2 := &node{data: val, next: new_node}
		l.head = n2

	}
}
func (l *LinkedList) Append(val interface{}) {
	if l.head == nil {
		l.head = &node{data: val, next: nil}
	}
	curr := l.head
	for curr.next != nil {
		curr = curr.next
	}
	curr.next = &node{data: val, next: nil}
}

func (l *LinkedList) Print() {
	curr := l.head
	for curr != nil {
		fmt.Println(curr.data)
		curr = curr.next
	}
}
