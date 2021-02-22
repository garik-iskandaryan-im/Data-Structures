import time;
from implementation import LinkedList;

linkedList = LinkedList();
linkedListStartTime = time.time();
for i in range(10000):
    linkedList.add(i);
linkedListEndTime = time.time();
print("push 10000 integer: time = ", round((linkedListEndTime - linkedListStartTime) * 1000), "milliseconds");
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