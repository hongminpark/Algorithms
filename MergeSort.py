def merge_sort(list):
    # recursion
    # 1) split
    left, right = split(list)

    # 2) (if the split size is 1)merge
    if len(left) is 1 and len(right) is 1:
        merged = merge(left, right)
        return merged
    else:
        merge_sort(left)
        merge_sort(right)

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
            result.append(left[r_idx])
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
    left, right = split([1,4,3,6,2,4,7,8,2])
    print(left, right)
    print(merge(left, right))