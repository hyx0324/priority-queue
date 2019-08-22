import numpy as np


def parent(i):
    return int((i-1)/2)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * (i + 1)


def max_heapify(A, i):
    l = left(i)
    r = right(i)

    if l + 1 <= A_heapsize and A[l] > A[i]:
        largest = l

    else:
        largest = i

    if r + 1 <= A_heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp_2 = A[i]
        A[i] = A[largest]
        A[largest] = temp_2

        max_heapify(A, largest)

def build_max_heap(A):
    for i in reversed(range(int(len(A)/2))):
        max_heapify(A, i)


def heap_maximum(A):
    return A[0]


def heap_extract_max(A):
    global A_heapsize

    if A_heapsize < 1:
        print('Error: heap underflow')
        return True

    max = A[0]
    A[0] = A[A_heapsize-1]
    A_heapsize -= 1

    max_heapify(A, 0)
    return max


def heap_increase_key(A, i, key):
    if key < A[i]:
        print('Error: new key is smaller than current key')
        return True

    A[i] = key

    # exchage 操作
    '''
    while i > 0 and A[parent(i)] < A[i]:
        temp = A[parent(i)]
        A[parent(i)] = A[i]
        A[i] = temp
        i = parent(i)
    '''

    # 插入排序中的内循环思想
    while i > 0 and A[parent(i)] < key:
        A[i] = A[parent(i)]
        i = parent(i)
    A[i] = key


def max_heap_insert(A, key):
    global A_heapsize
    A_heapsize += 1
    A[A_heapsize-1] = float('-inf')
    heap_increase_key(A, A_heapsize-1, key)


if __name__ == '__main__':
    A_size = 16
    A = list(np.random.randint(-100, 100, size=A_size))

    A_heapsize = len(A)

    print('The original list is:', A)

    build_max_heap(A)
    max = heap_extract_max(A)

    print('\nThe maximum number of the list is:', max)
    print('\nThe list after extracting max:', A[:A_heapsize])

    heap_increase_key(A, 8, 15)
    print('\nThe list after increasing number:', A)

    max_heap_insert(A, 1000)
    print('\nThe list after insert 1000:', A)