file = open('words.txt', 'r')
words = file.read().splitlines()
print('Number of words read:', len(words))

def binary_search(arr, target):
    low = 0#TODO: Implement the iterative binary search method and print the result as described on the previous slide
    high = len(arr)-1
    iterations = 0
    while low <= high:
        iterations += 1
        mid = (low + high) //2
        if target == arr[mid]:
            print('Target = {}, Found at index = {}, Number of iterations = {}'.format(target, mid, iterations))
            return
            
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print('Target = {}, Found at index = {}, Number of iterations = {}'.format(target, '-1', iterations))

target = input('Enter search key: ').lower()

while target != 'exit':
    binary_search(words, target)
    target = input('Enter search key: ').lower()


