def bubble_sort(A):
    """
    [idea]
    1. 1번과 2번, 2번과 3번, 3번과 4번, ... 과 같이 비교해서 끝까지 도달한다
    2. 첫 번째 루프에서는 제일 큰 수가 마지막에 오게 된다.
    3. 이 과정을 각 순회당 N, N-1, N-2, ... 번 하게 된다.
    """
    for k in range(len(A)):
        for i in range(1, len(A)-k):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
    return A

if __name__ == "__main__":
    A = [1,5,34,4,2,4,3,21,205,3]
    print(bubble_sort(A))
