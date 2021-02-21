# import sys;
# # sys.path.append('./../Stack/implementation');
# from ..Stack.implementation import Stack;

class Node:
    def __init__(self, value, prev = None):
        self.value = value;
        self.prev = prev;

class Stack:
    def __init__(self):
        self.element = None;
        self.size = 0;
    def push(self, value):
        self.element = Node(value, self.element);
        self.size+=1;
    def pop(self):
        if self.isEmpty():
            return None;
        deleted = self.element.value;
        self.element = self.element.prev;
        self.size-=1;
        return deleted;
    def top(self):
        if self.isEmpty():
            return None;
        else: 
            return self.element.value;
    def back(self):
        if self.isEmpty():
            return None;
        while self.element.prev != None:
            self.element = self.element.prev;
        return self.element.value;
    def isEmpty(self):
        return self.size == 0;
    def length(self):
        return self.size;
    def clear(self):
        self.element = None;
        self.size = 0;
    def printStack(self):
        currentNode = self.element;
        while currentNode:
            print(currentNode.value);
            currentNode = currentNode.prev;
            
class Queue:
    def __init__(self):
        self.pushStack = Stack();
        self.popStack = Stack();
        self.size = 0;
    def enqueue(self, value):
        self.pushStack.push(value);
        self.size+=1;
    def dequeue(self):
        if not self.popStack.isEmpty():
            return self.popStack.pop();
        while not self.pushStack.isEmpty():
            self.popStack.push(self.pushStack.pop());
        self.size-=1;
        return self.popStack.pop();
    def front(self):
        if not self.popStack.isEmpty():
            return self.popStack.top();
        elif not self.pushStack.isEmpty():
            return self.pushStack.back(); 
        else: 
            return None;
    def back(self):
        if not self.pushStack.isEmpty():
            return self.pushStack.top();
        elif not self.popStack.isEmpty():
            return self.popStack.back();
        else: 
            return None;
    def isEmpty(self):
        return self.size == 0;
    def length(self):
        return self.size;
    def clear(self):
        self.popStack.clear();
        self.pushStack.clear();
        self.size = 0;
    def printQueue(self):
        self.popStack.printStack();
        self.pushStack.printStack();