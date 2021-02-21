import time;

class Node:
    def __init__(self, element, next = None):
        self.element = element;
        self.next = next;
class LinkedList:
    def __init__(self):
        self.head = None;
        self.size = 0;
    def add(self, element):
        node = Node(element);
        if self.head is None:
            self.head = node;
        else:
            currentNode = self.head;
            while currentNode.next:
                currentNode = currentNode.next;
            currentNode.next = node;
        self.size+=1;
    def insertAt(self, element, index):
        if index > self.length() or index < 0:
            return -1;
        node = Node(element);
        if index == 0:
            node.next = self.head;
            self.head = node;
        else:
            currentNode = self.head;
            previous = None;
            for i in range(index):
                previous = currentNode;
                currentNode = currentNode.next;
            previous.next = node;
            node.next = currentNode;
        self.size+=1;
    def removeFrom(self, index):
        if self.isEmpty() or index > self.length() or index < 0:
            return -1;
        currentNode = self.head;
        if index == 0:
            self.head = self.head.next;
        else:
            previous = None;
            for i in range(index):
                previous = currentNode;
                currentNode = currentNode.next;
            if currentNode:
                previous.next = currentNode.next;
            else:
                currentNode = previous;
        self.size-=1;
        return currentNode.element;
    def removeElement(self, element):
        if self.isEmpty():
            return -1;
        currentNode = self.head;
        index = -1;
        if currentNode.element == element:
            self.head = currentNode.next;
            index = 0;
        else:
            previous = None;
            count = 0;
            while currentNode and currentNode.element != element:
                count+=1;
                previous = currentNode;
                currentNode = currentNode.next;
            if currentNode:
                previous.next = currentNode.next;
                index = count;
            elif previous.element == element:
                previous.next = currentNode;
                index = count;
            else:
                return index;
        self.size-=1;
        return index;
    def getLast(self):
        lastNode = self.head;
        if lastNode:
            while lastNode.next:
                lastNode = lastNode.next
        if lastNode:
            return lastNode.element
        else: 
            return None;
    def getFirst(self):
        if self.head:
            return self.head.element;
        else: 
            return None;
    def isEmpty(self):
        return self.length() == 0;
    def length(self):
        return self.size;
    def clear(self):
        self.head = None;
        self.size = 0;
    def printList(self):
        currentNode = self.head;
        while currentNode:
            print(currentNode.element)
            currentNode = currentNode.next;

# tests 
linkedList = LinkedList();
linkedListStartTime = round(time.time()) * 1000;
for i in range(10000):
    linkedList.add(i);
linkedListEndTime = round(time.time()) * 1000;
print("push 10000 integer: time = ", linkedListEndTime - linkedListStartTime, "milliseconds");
print("isEmpty()", linkedList.isEmpty());
print("length()", linkedList.length());
print("getLast()", linkedList.getLast());
print("getFirst()", linkedList.getFirst());
print("length()", linkedList.length());
print("clear()", linkedList.clear());
print("isEmpty()", linkedList.isEmpty());
print("insertAt(1, 0)", linkedList.insertAt(1, 0));
print("insertAt(5, 1)", linkedList.insertAt(5, 1));
print("insertAt(3, 2)", linkedList.insertAt(3, 2));
print("printList()");
linkedList.printList();
print("removeFrom(0)", linkedList.removeFrom(0));
print("removeElement(3)", linkedList.removeElement(3));
print("printList()");
linkedList.printList();