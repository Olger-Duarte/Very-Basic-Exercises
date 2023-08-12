def flattenArray(arr):
    flat = []
    for item in arr:
        if isinstance(item, list):
            flat.extend(flattenArray(item))
        else:
            flat.append(item)
    return flat

arr = [1, [2, 3, [4, 5], [[6, [7]], 8, 9]]]
print(flattenArray(arr))  # Output: [1, 2, 3, 4, 5]
