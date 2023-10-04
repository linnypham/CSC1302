def partition(arr, low, high):
    pivot = arr[high]
    i = low
    print(f'Array segment before  partitioning: {arr[low:high+1]}, Pivot: {pivot}')
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]

    return i

def quick_sort(arr, start, end):
    if start >= end:
        return
    print(f'----- Quick sorting from index: {start} to {end} -----')
    k = partition(arr, start, end)
    print(f'Array segment after partitioning: {arr[start:end+1]}')
    print()
    quick_sort(arr, start, k-1)
    quick_sort(arr, k+1, end)

arr = [11, 12, 1, 9, 6, 5, 4, 7]
quick_sort(arr, 0, len(arr)-1)
print('The final sorted array', arr)
