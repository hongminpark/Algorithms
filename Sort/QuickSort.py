def quick_sort(A):
    """
    [idea]
    1. 리스트의 임의의 pivot을 고른다. -> 보통 끝값
    2. pivot보다 작은 값을 왼쪽, 큰 값을 오른쪽으로 보낸다.
    3. 왼쪽과 오른쪽을 다시 quick_sort에 넣고 2번의 결과와 합친다.(Divide and Conquer)
    """

    N = len(A)
    if N <= 1:
        return A

    pivot = A[-1]
    smaller, bigger = [], []
    for i in range(N-1):
        if A[i] <= pivot:
            smaller.append(A[i])
        else:
            bigger.append(A[i])
    return quick_sort(smaller) + [pivot] + quick_sort(bigger)
    
           
    
if __name__ == "__main__":
    A = [2,5,1,10,3,9]
    A1 = [2,4,53,1,23,41,2,3,5,6,3,43,55]
    print(quick_sort(A))
    print(quick_sort(A1))

