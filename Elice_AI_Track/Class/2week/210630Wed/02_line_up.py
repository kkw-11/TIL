MOD = 1_000_000_007
# modulo??

def lining(n) :
    '''
    n명의 학생을 일렬로 줄세우는 경우의 수를 1,000,000,007 로 나눈 나머지를 반환하는 함수를 작성하세요.
    '''
    # 목표 : end_man[n] + end_woman[n] : n명 세우는 경우의 수
    # end_man[1] ~ end_man[n] 까지 구해야한다
    
    
    end_man = [None] * (n + 1) # end_man[k] : k명 세울 때 끝이 남자인 경우의 수
    end_woman = [None] * (n + 1) # end_woman[k] : k명 세울 때 끝이 여자인 경우의 수
    # end_man = [None, None, ..., None] (n+1) 길이만큼 필요 0번째 인덱스는 사용하지 않음
    
    # 0부터 하면 아무도 안 세우는 방법 1가지를 중복으로 세기 때문에 안 됨
    # end_man[0] = 1
    # end_woman[0] = 1
    
    end_man[1] = 1 # [None, 1, ..., None]
    end_woman[1] = 1 # [None, 1, ..., None]
    
    for k in range(2, n + 1):
        end_man[k] = end_woman[k-1]
        end_woman[k] = end_man[k-1] + end_woman[k-1]
        
        # end_man.append(end_woman[k-1])
        # end_woman.append(end_man[k-1] + end_woman[k-1])
    
    return (end_man[n] + end_woman[n]) % MOD
