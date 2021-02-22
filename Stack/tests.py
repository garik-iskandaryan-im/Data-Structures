import time;
from implementation import Stack;

stack = Stack();
pushStartTime = time.time();
for i in range(100000):
    stack.push(i);
pushEndTime = time.time();
print("push 100000 integer: time = ", round((pushEndTime - pushStartTime) * 1000), "milliseconds");
print("isEmpty()", stack.isEmpty());
print("length()", stack.length());
print("dequeue()", stack.pop());
print("top()", stack.top());
print("back()", stack.back());
print("length()", stack.length());
print("clear()", stack.clear());
print("isEmpty()", stack.isEmpty());