def selection_sort(a):    
    """
    [idea]
    배열의 모든 아이템에 대하여 순차 탐방을 하는데,
    매 i번째를 탐색하고, i+1부터의 리스트 중 최소값을 선택해 바꾼다.
    매번 탐방 중인 값과 그 이후의 값들을 비교해서 
    앞에서부터 차례대로 가장 작은 값들이 나온다. 
    """
    for i, item in enumerate(a):
        tmp_idx = i
        tmp_min = item
        for i_, item_ in enumerate(a[i+1:]):
            if item_ < tmp_min:
                tmp_min = item_
                tmp_idx = i + i_ + 1
        a[i], a[tmp_idx] = a[tmp_idx], a[i]

    return a
        
if __name__ == "__main__":
    a = [2,5,1,10,3,9]
    print(selection_sort(a))
    
    
