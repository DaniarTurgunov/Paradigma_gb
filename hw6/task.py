def binsearch(arr,num):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == num:
            return mid
        if guess > num:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [1,2,3,4,5,6]
num = 6

print(binsearch(arr,num))