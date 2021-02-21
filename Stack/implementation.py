import time;

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

# tests
stack = Stack();
pushStartTime = round(time.time()) * 1000;
for i in range(100000):
    stack.push(i);
pushEndTime = round(time.time()) * 1000;
print("push 100000 integer: time = ", pushEndTime - pushStartTime, "milliseconds");
print("isEmpty()", stack.isEmpty());
print("length()", stack.length());
print("dequeue()", stack.pop());
print("top()", stack.top());
print("back()", stack.back());
print("length()", stack.length());
print("clear()", stack.clear());
print("isEmpty()", stack.isEmpty());