def sortByMaxMin(arr):
    sorted_arr = sorted(arr)
    result = []
    for i in range(len(arr)//2):
        result.append(sorted_arr[-(i+1)])
        result.append(sorted_arr[i])
    if len(arr) % 2 != 0:
        result.append(sorted_arr[len(arr)//2])
    return result
