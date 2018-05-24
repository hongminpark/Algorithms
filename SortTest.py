import BubbleSort
import SelectionSort
import InsertionSort
import QuickSort
import time

if __name__ == "__main__":
    test_list = [1,5,52,4,23,1,32,4,5,6,19,4234,100,2,3,45,68,125,37,54614,2,46,67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67]
    start = time.time()
    BubbleSort.bubble_sort(test_list)
    finish = time.time()
    print("********************************")
    print("BubbleSort: ", test_list)
    print("time: %f" % (finish - start))
    print("\n")

    test_list = [1,5,52,4,23,1,32,4,5,6,19,4234,100,2,3,45,68,125,37,54614,2,46,67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67]
    start = time.time()
    SelectionSort.selection_sort(test_list)
    finish = time.time()
    print("********************************")
    print("SelectionSort: ", test_list)
    print("time: %f" % (finish - start))
    print("\n")

    test_list = [1,5,52,4,23,1,32,4,5,6,19,4234,100,2,3,45,68,125,37,54614,2,46,67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67]
    start = time.time()
    InsertionSort.insertion_sort(test_list)
    finish = time.time()
    print("********************************")
    print("InsertionSort: ", test_list)
    print("time: %f" % (finish - start))
    print("\n")

    test_list = [1,5,52,4,23,1,32,4,5,6,19,4234,100,2,3,45,68,125,37,54614,2,46,67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67,
                 1, 5, 52, 4, 23, 1, 32, 4, 5, 6, 19, 4234, 100, 2, 3, 45, 68, 125, 37, 54614, 2, 46, 67]
    size = len(test_list)
    start = time.time()
    QuickSort.quick_sort(test_list, 0, size-1)
    finish = time.time()
    print("********************************")
    print("QuickSort: ", test_list)
    print("time: %f" % (finish - start))
    print("\n")
