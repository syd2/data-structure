def BinarySearch(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low +high)//2
        if data[mid] == target:
            return data[mid]
        elif target< data[mid] :
            return BinarySearch(data, target, low, mid-1)
        else:
            return BinarySearch(data, target,  mid+1, high)


print(BinarySearch([2, 4, 5 ,7, 8, 12, 14 ,17, 19, 22, 25, 27, 28, 33, 37 ], 1, 0, 15))
