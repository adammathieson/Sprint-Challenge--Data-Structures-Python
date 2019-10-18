import random


def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    for i in range(elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)

    return merged_arr

def merge_sort( arr ):
    if len(arr) > 1:
        right = merge_sort(arr[(len(arr)//2):])
        left = merge_sort(arr[:(len(arr)//2)])
        
        return merge(left, right)
    
    return arr

