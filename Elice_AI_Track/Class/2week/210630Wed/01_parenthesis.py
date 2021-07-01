# def checkParen(p):
#     '''
#     괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
#     '''
    
#     # 이문제 꼭 스택/리스트를 써야하나요?
#     stack = []
    
#     for item in p:
        
#         if item == '(':
#             stack.append(item)
#         else:
#             if len(stack) == 0:
#                 return 'NO'
#             stack.pop()
    
#     if len(stack) == 0:
#         return "YES"
#     else:
#         return 'NO'

def checkParen(p):
    '''
    괄호 문자열 p의 쌍이 맞으면 "YES", 아니면  "NO"를 반환
    '''
    # p 문자열이 1, 100, 1억 O(1)
    left = 0
    
    for item in p:
        if item == '(':
            left += 1
        else:
            if left == 0:
                return 'NO'
            left -= 1
    
    if left == 0:
        return 'YES'
    else:
        return 'NO'
    

def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


