def selection_sort(list):
    for i in range(len(list)-1):
        min_idx = i
        min_val = list[min_idx]

        for idx, item in enumerate(list[i:]):
            if item < min_val:
                min_val = item
                min_idx = idx + i # Because of the list[i:], must need to sum current 'i' to get current idx
        list[i], list[min_idx] = list[min_idx], list[i]


if __name__ == "__main__":
    test_list = [2,5,1,10,3,9]
    selection_sort(test_list)
    print(test_list)