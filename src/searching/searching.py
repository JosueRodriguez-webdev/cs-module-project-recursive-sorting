# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    print(f"array:{arr}, target:{target} start:{start} end:{end}")
    # calculate the middle by adding start and end and // 2
    middle = (start + end) // 2

    if len(arr) < 1:
        return -1

    # if the target value is > middle value
    # move the start middle + 1
    # make recursive call!
    if target > arr[middle]:
        new_start = middle + 1
        return binary_search(arr, target, new_start, end)
    # if the target value is < middle value
    # move the highest middle - 1
    # make recursive call!
    if target < arr[middle]:
        new_end = middle - 1
        return binary_search(arr, target, start, new_end)

    # if target value == middle value:
    # then return middle value index!
    if target == arr[middle]:
        return middle


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    pass
    # Your code here
