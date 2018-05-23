# low size complexity

def quick_sort(list):
    # pick pivot (ex. the last from the list)
    # < pivot -> swap, > pivot -> nothing
    # quick_sort(left), quick_sort(right)
    size = len(list)
    for i in range(size):
        pivot = list[-1]
        wall = 0

        for j in