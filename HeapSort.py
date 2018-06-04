def heapsort(list):
    for i in range(len(list)):
        list[0], list[-i-1] = list[-i-1], list[0]
        if len(list)-i-2 > 0:
            siftdown(list, 0, len(list)-i-2)

def heapify(list):
    size = len(list)
    for i in range(size/2-1, -1, -1):
        siftdown(list, i, size)

def siftdown(list, i, end):
    if i >= end/2:
        return

    if list[2*i+1] > list[2*i+2]:
        if list[2*i+1] > list[i]:
            list[2*i+1], list[i] = list[i], list[2*i+1]
            siftdown(list, 2*i+1, len(list))
    else:
        if list[2*i+2] > list[2*i+1]:
            list[2*i+2], list[i] = list[i], list[2*i+2]
            siftdown(list, 2*i+2, len(list))

if __name__ == "__main__":
    a = [7,6,5,4,2,1,3]
    # heapify(a)
    # print(a)
    heapsort(a)
    print(a)