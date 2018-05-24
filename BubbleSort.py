def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            # swap between the two right next items
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


if __name__ == "__main__":
    test_list = [2,5,1,10,3,9]
    bubble_sort(test_list)
    print(test_list)