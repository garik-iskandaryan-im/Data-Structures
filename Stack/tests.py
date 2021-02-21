import time;
from implementation import Stack;

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