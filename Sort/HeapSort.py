def heap_sort(A):
    """
    [idea]
    1. 정렬되지 않은 리스트를 Upward 방식으로 노드를 붙여가며 Build Max Heap 한다.
    2. Max Heap에서 첫번째 노드와 마지막 노드를 교환하면 가장 큰 수가 뒤로 간다.
    3. 0번째 노드로 인해 Max-Heap이 깨졌으므로 0번째 노드를 가장큰 수 이전까지 Downward 방식으로 Heapify한다
    """

    for i in range(len(A)):
        child = i
        parent = i//2 + i%2 - 1
        while parent >= 0:
            if A[child] <= A[parent]:
                break
            A[child], A[parent] = A[parent], A[child]
            child = parent
            parent = child//2 + child%2 - 1

    for i in range(len(A)-1):
        parent = 0
        last = len(A) - 1 - i
        A[parent], A[last] = A[last], A[parent]

        while parent <= (last-1)//2 + (last-1)%2 - 1:
            child1 = 2*parent + 1
            child2 = 2*parent + 2
            if child2 == last:
                maxchild = child1
            else:
                if A[child1] >= A[child2]:
                    maxchild = child1
                else:
                    maxchild = child2

            if A[parent] < A[maxchild]:
                A[parent], A[maxchild] = A[maxchild], A[parent]
                parent = maxchild
            else:
                break
    return A


if __name__ == "__main__":
    A = [1, 5, 34, 4, 2, 4, 3, 21, 205, 3]
    print(heap_sort(A))
