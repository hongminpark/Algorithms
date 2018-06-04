# Code concept referred (a little bit) from https://smlee729.github.io/python/algorithm/2015/03/03/1-merge-sort.html

def merge_sort(list):
    # recursion
    # 1) split
    if len(list) <= 1:
        return list

    left, right = split(list)

    left = merge_sort(left)
    right = merge_sort(right)

    # 2) (if the split size is 1)merge
    return merge(left, right)

def split(list):
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return (left, right)

def merge(left, right):
    result = []
    l_idx = 0
    r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

        if l_idx is len(left):
            for i in right[r_idx:]:
                result.append(i)
            break
        elif r_idx is len(left):
            for i in left[l_idx:]:
                result.append(i)
            break

    return result

if __name__ == "__main__":
    a = [1,5,34,4,2,4,3,21,205,3]
    print(merge_sort(a))
