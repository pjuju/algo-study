# import sys
# read = sys.stdin.readline()
# N = int(read)
# queue = list(range(1,N+1))
# rear = 0
#
# while True:
#     rear += 1
#     if rear+1 == len(queue):
#         break
#     queue.append(queue[rear])
#     rear += 1
#
# print(queue[rear])


from collections import deque
d = deque()
for i in range(int(input())):
    d.append(i+1)
while len(d) > 1:
    d.popleft()
    d.append(d.popleft())
print(*d)