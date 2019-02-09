def pushZerosToEnd(arr, n):
    count = 0 # Count of non-zero elements

    # Traverse the array. If element
    # encountered is non-zero, then
    # replace the element at index
    # 'count' with this element
    for i in range(n):
        print(arr)
        if arr[i] != 0:

            # here count is incremented
            arr[count] = arr[i]
            count+=1

    # Now all non-zero elements have been
    # shifted to front and 'count' is set
    # as index of first 0. Make all
    # elements 0 from count to end.
    while count < n:
        arr[count] = 0
        count += 1

# Driver code
arr = [1, 0, 0, 3,5,0,1]
n = len(arr)
pushZerosToEnd(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)