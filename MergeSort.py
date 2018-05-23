def merge_sort(list):
    # recursion
    # 1) split
    size = len(list)
    while size > 1:
        mid = size//2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)

    # 2) merge

def split(list):

def merge(left, right):


