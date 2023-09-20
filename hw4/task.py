from math import sqrt

def correlation(arr1, arr2):
    arr1_average = list(map(lambda x: sum(arr1)/(len(arr1)+1)-x, arr1))
    arr2_average = list(map(lambda y: sum(arr2)/(len(arr2)+1)-y, arr2))

    sum_sq_arr1 = sum(map(lambda x: pow(x, 2), arr1_average))
    sum_sq_arr2 = sum(map(lambda y: pow(y, 2), arr2_average))

    sum_diff_arr = sum(map(lambda x, y: x * y, arr1_average, arr2_average))
    
    return round(sum_diff_arr/sqrt(sum_sq_arr1 * sum_sq_arr2), 3)

arr1 = [-27, -96, -7, 63, -74, 30, -1]
arr2 = [45, 30, -9, -11, 4, 31, -60]

print(f'Result = {correlation(arr1,arr2)}')