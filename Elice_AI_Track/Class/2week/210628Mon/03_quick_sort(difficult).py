# 수요일 오전 이론 강의 때 했던 방식 (더 효율이 좋음)
def quickSort(li):
    
    def _q_sort(li, start, end):
        
        if end <= start:
            return 

        pivot = li[end]
        
        # 교체가 완료된 왼쪽 지점 p와 오른쪽 지점 q
        p, q = start - 1, end
        
        while p + 1 < q:
            
            while li[p + 1] <= pivot and p + 1 < q:
                p += 1
            
            while li[q - 1] > pivot and p + 1 < q:
                q -= 1
            
            if p + 1 < q - 1:
                li[p + 1], li[q - 1] = li[q - 1], li[p + 1]
                p += 1
                q -= 1
        
        li[q], li[end] = li[end], li[q]
        
        _q_sort(li, start, p)
        _q_sort(li, q + 1, end)
    
    l = len(li)
    
    if l == 0 or l == 1:
        return li

    _q_sort(li, 0, l - 1)
    
    return li

        
def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
