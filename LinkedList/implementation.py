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
    def clear():
        self.head = None;
        self.size = 0;
    def printList(self):
        currentNode = self.head;
        while currentNode:
            print(currentNode.element)
            currentNode = currentNode.next;

# tests 
linkedList = LinkedList();
linkedList.add(5);
linkedList.add(15);
linkedList.add(16);
linkedList.add(17);
linkedList.insertAt(156,2)
linkedList.removeFrom(2);
print(linkedList.getLast());
# linkedList.printList();