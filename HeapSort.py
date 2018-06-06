def heapsort(list):
    heapify(list)
    size = len(list)
    for i in range(size-1):
        next = i+1
        list[0], list[-next] = list[-next], list[0]
        siftdown(list, 0, size-next-1)

def heapify(list):
    size = len(list)

    # Traverse from the half of the tree
    for i in range(size/2-1, -1, -1):
        siftdown(list, i, size-1)

def siftdown(list, i, end):
    
    l_child = 2*i+1
    r_child = 2*i+2

    # child out of end index
    if l_child > end:
        return
    # 1 child case
    elif l_child is end:
        if list[l_child] > list[i]:
            list[l_child], list[i] = list[i], list[l_child]
    else:
        if list[l_child] >= list[r_child]:
            if list[l_child] > list[i]:
                list[l_child], list[i] = list[i], list[l_child]
                siftdown(list, l_child, end)
        else:
            if list[r_child] > list[i]:
                list[r_child], list[i] = list[i], list[r_child]
                siftdown(list, r_child, end)

if __name__ == "__main__":
    a = [7,6,5,4,2,1,3]
    # b = [1, 5, 34, 4, 2, 4, 3, 21, 205, 3]
    b = [6, 2, 8, 9, 7, 5, 4]
    # heapify(b)
    print(b)
    heapsort(b)
    print(b)