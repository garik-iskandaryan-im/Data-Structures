import time;
from implementation import Queue;

queue = Queue();
enqueueStartTime = round(time.time() * 1000);
for i in range(100000):
    queue.enqueue(i);
enqueueEndTime = round(time.time() * 1000);
print("enqueue 100000 integer time = ", enqueueEndTime - enqueueStartTime, "milliseconds");
print("isEmpty()", queue.isEmpty());
print("length()", queue.length());
print("dequeue()", queue.dequeue());
print("length()", queue.length());
print("front()", queue.front());
print("back()", queue.back());
print("clear()", queue.clear());
print("isEmpty()", queue.isEmpty());