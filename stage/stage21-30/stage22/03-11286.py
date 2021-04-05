import sys


def heapappend(heap, num):
    heap.append(num)

    i = len(heap) - 1
    while i > 1:
        if abs(heap[i]) < abs(heap[i // 2]) or (abs(heap[i]) == abs(heap[i // 2]) and heap[i] < heap[i // 2]):
            tmp = heap[i]
            heap[i] = heap[i // 2]
            heap[i // 2] = tmp
            i = i // 2
        else:
            break


def heappop(heap):
    popvalue = heap[1]
    tmp = heap.pop()

    parent = 1
    child = 2
    while child <= len(heap) - 1:
        if child < len(heap) - 1 and (abs(heap[child]) > abs(heap[child + 1])
                                      or (abs(heap[child]) == abs(heap[child + 1]) and heap[child] > heap[child + 1])):
            child += 1
        if abs(heap[child]) > abs(tmp) or (abs(heap[child]) == abs(tmp) and heap[child] > tmp):
            break
        heap[parent] = heap[child]
        parent = child
        child *= 2

    if len(heap) != 1:
        heap[parent] = tmp
    return popvalue


n = int(sys.stdin.readline())
a = [0]
for _ in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        if len(a) == 1:
            print(0)
        else:
            print(heappop(a))
    else:
        heapappend(a, m)