def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return index if found
    return -1  # return -1 if not found

# Test
arr = [2, 5, 7, 10, 14, 20]
target = 10
result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Test
arr = [2, 5, 7, 10, 14, 20]
target = 10
result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print("Target not found")
