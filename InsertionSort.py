def insertion_sort(list):
    for i in range(len(list)):
        # set each item an insertion value
        tmp_min = list[i]

        if i is not 0:
            # compare the insertion location from the sorted list
            for idx, item in enumerate(list[:i]):
                if tmp_min < item:
                    # is it meaningful? 
                    list.remove(tmp_min)
                    list.insert(idx, tmp_min)
                    break


if __name__ == "__main__":
    test_list = [6, 4, 10, 1, 2, 5]
    insertion_sort(test_list)
    print(test_list)