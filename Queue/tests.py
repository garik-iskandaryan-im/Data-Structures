import time;
from implementation import Queue;

queue = Queue();
enqueueStartTime = time.time();
for i in range(100000):
    queue.enqueue(i);
enqueueEndTime = time.time();
print("enqueue 100000 integer time = ", round((enqueueEndTime - enqueueStartTime) * 1000), "milliseconds");
print("isEmpty()", queue.isEmpty());
print("length()", queue.length());
print("dequeue()", queue.dequeue());
print("length()", queue.length());
print("front()", queue.front());
print("back()", queue.back());
print("clear()", queue.clear());
print("isEmpty()", queue.isEmpty());