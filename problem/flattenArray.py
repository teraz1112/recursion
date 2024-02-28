def flattenArray(arr):
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flattenArray(item))
        elif isinstance(item, int) and item % 2 == 0:
            result.append(item)
    return result

print(flattenArray([1,2,3,[4,5,[6,7]],8,[9,10,11],12,13]))
