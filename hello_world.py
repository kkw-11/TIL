def quick_sort(data):
    if len(data) == 1:
        return
    pivot = 0

    left = pivot+1
    right = len(data)-1

    while left <= right:
        while data[pivot] >= data[left]:
            left += 1

        while data[pivot] < data[right]:
            right -= 1
        if left > right:
            break
        data[right], data[left] = data[left], data[right]
    data[left-1],data[pivot]= data[pivot],data[left-1]
    quick_sort(data[:left])
    quick_sort(data[left:])
    return data

data = [5,2,7,3,6,4,10]

print(quick_sort(data))


        while int(data[pivot] + data[left]) <= int(data[left] + data[pivot]) :
            left += 1

        while int(data[pivot] + data[right]) > int(data[right] + data[pivot]):
            right -= 1