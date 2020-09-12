

def binary_search(array, low, high, item):
    """ returns index of item in array if found, else -1 """
    if high < low: return -1

    mid = (high + low)//2
    if item == array[mid]: return mid
    if item < array[mid]: return binary_search(array, low, mid-1, item)
    return binary_search(array, mid+1, high, item)

array = list(map(int, input().split()))
item = int(input())

print(array)
print(item)

print(binary_search(array,0, len(array)-1, item))
