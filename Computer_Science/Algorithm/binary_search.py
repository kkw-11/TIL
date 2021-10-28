def binary_search(array,target,start,end):
    array.sort()
    while start<=end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid +1
        else:
            end = mid - 1

    return -1

input_data = list(map(int,input().split()))
target = int(input())

if binary_search(input_data,target, 0,len(input_data)-1) != -1:
    print("index:",binary_search(input_data,target,0,len(input_data)-1))
else:
    print("fail")
