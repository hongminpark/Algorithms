def merge_sort(A):
    """
    [idea]
    1. 리스트를 계속 반으로 쪼갠다.
    2. 왼쪽을 merge_sort에 넣고 오른쪽을 merge_sort에 넣는다.(Divide and Conquer)
    3. 정렬된 두 리스트를 merge할 때는 두 리스트를 함께 비교한다.
    """
    if len(A) <= 1:
        return A

    left = merge_sort(A[:len(A) // 2])
    right = merge_sort(A[(len(A) // 2):])
    l, r = 0, 0
    A_sorted = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            A_sorted.append(left[l])
            l += 1
        else:
            A_sorted.append(right[r])
            r += 1
        if l == len(left):
            A_sorted += right[r:]
            break
        elif r == len(right):
            A_sorted += left[l:]
            break
    return A_sorted


if __name__ == "__main__":
    A = [1, 5, 34, 4, 2, 4, 3, 21, 205, 3]
    print(merge_sort(A))
