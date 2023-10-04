def merge(arr, left, mid, right):
    merge_size = right - left + 1
    merged = [0] * merge_size
    # initialize pointers
    i = left #left index
    j = mid + 1 #right index
    k = 0 #merge array index

    #compare and merge
    while i <= mid and j <= right:
        if arr[i] > arr[j]:
            merged[k] = arr[i]
            i += 1
        else:
            merged[k] = arr[j]
            j += 1
        k += 1

    #merge remainings
    while i <= mid:
        merged[k] = arr[i]
        i += 1
        k += 1

    # merge remainings
    while j <= right:
        merged[k] = arr[j]
        j += 1
        k += 1


    k=0
    while k < merge_size:
        arr[left+k] =  merged[k]
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2 #split the list into 2 half
        merge_sort(arr, left, mid) #sort 1st half
        merge_sort(arr, mid+1, right) #sort 2nd half

        merge(arr, left, mid, right) #merge







list1 = [5,6,3,8,7,1,1,3,7,5,5]
print('Input: ', list1)
merge_sort(list1, 0,len(list1)-1)
print('Output: ',list1)
