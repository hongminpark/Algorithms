# low size complexity

def quick_sort(list, start, stop):

    if stop <= start:
        return

    # pick pivot (ex. the last from the list)
    pivot_idx = stop
    pivot = list[pivot_idx]
    wall_idx = start

    # Traverse the list except the pivot
    # if item < pivot: swap with the wall_idx value
    # else: nothing to do
    for tmp_idx, item in enumerate(list[start:stop]):
        if item < pivot:
            list[wall_idx], list[start + tmp_idx] = list[start + tmp_idx], list[wall_idx]
            wall_idx += 1

    # After traversing the list, swap wall and pivot
    list[wall_idx], list[pivot_idx] = list[pivot_idx], list[wall_idx]

    # quick_sort again the left and right lists
    quick_sort(list, start, wall_idx-1)
    quick_sort(list, wall_idx+1, stop)

if __name__ == "__main__":
    a = [1,5,34,4,2,4,3,21,205,3]
    quick_sort(a, 0, len(a)-1)
    print(a)