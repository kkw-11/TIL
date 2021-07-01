
# 월요일 오후 실습 수업 때 했던 방식
def quickSort(li):
    
    # 리스트 길이
    l = len(li)
    
    if l <= 0:
        return li
    
    pivot = li[0]
    
    left = []
    right = []
    
    for item in li[1:]:
        if item <= pivot:
            left.append(item)
        else:
            right.append(item)
    
    return quickSort(left) + [pivot] + quickSort(right)
        

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
