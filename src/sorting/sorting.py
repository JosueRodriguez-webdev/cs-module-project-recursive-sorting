# TO-DO: complete the helper function below to merge 2 sorted arrays

def merge(arrA, arrB):
    element = len(arrA) + len(arrB)
    merged_arr = [0] * element

    if len(arrA) == len(arrB):
        for idx in range(0, len(arrA) - 1):
            if arrA[idx] > arrB[idx]:
                merged_arr[idx] = arrA[idx]
                merged_arr[idx + 1] = arrB[idx]
            else:
                merged_arr[idx] = arrB[idx]
                merged_arr[idx + 1] = arrA[idx]

    if len(arrA) > len(arrB):
        for idx in range(0, len(arrA) - 1):
            if arrA[idx] and arrB[idx]:
                if arrA[idx] > arrB[idx]:
                    merged_arr[idx] = arrA[idx]
                    merged_arr[idx + 1] = arrB[idx]
                else:
                    merged_arr[idx] = arrB[idx]
                    merged_arr[idx + 1] = arrA[idx]
            else:
                merged_arr[idx] = arrA[idx]

    if len(arrA) < len(arrB):
        for idx in range(0, len(arrB)):
            multiply_index = idx + 2
            if idx == 0:
                multiply_index = idx + 1
            print(idx)
            if arrA[idx] and arrB[idx]:
                if arrA[idx] < arrB[idx]:
                    print('here')
                    merged_arr[multiply_index - 1] = arrA[idx]
                    merged_arr[multiply_index] = arrB[idx]
                else:
                    print('no here')
                    merged_arr[multiply_index - 1] = arrB[idx]
                    merged_arr[multiply_index] = arrA[idx]
            else:
                print('nah g here')
                merged_arr[multiply_index - 1] = arrB[idx]

    else:
        print('trigger 6?')

        # loop arrays at the same time to see which is greater than and which is less

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
hello = merge([1, 3], [2, 4, 6])
print(hello)


def merge_sort(arr):
    # merge using merge sort method
    pass
    # low = 0
    # high = len(arr)-1
    # middle = low + high // 2

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
