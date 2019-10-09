def insertion_sort(A):
    """
    [idea]
    1. i번째 아이템을 정렬되어있는 i-1번째 까지의 리스트와 비교해서 적절할 위치에 넣는다.
    2. 0번째부터 탐색하면 i를 탐색할 때 i-1번째까지의 리스트는 항상 정렬되어 있다.
    """
    for i, a in enumerate(A):
        if not i:
            continue
        for i_, a_ in enumerate(A[:i]):
            if a <= a_:
                A[i_:i+1] = [a] + A[i_:i]
                break
    return A


if __name__ == "__main__":
    A = [1, 5, 34, 4, 2, 4, 3, 21, 205, 3]
    print(insertion_sort(A))
