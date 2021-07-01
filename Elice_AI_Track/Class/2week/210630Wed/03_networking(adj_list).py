import sys
sys.setrecursionlimit(100000)
    
def numStudents(n_nodes, myInput) :
    '''
    학생들 사이의 친구관계가 myInput으로 주어질 때, 정원이가 퍼트린 소문을 듣게되는 학생의 수를 반환합니다.
    '''
    
    print(n_nodes, myInput)
    # 친구 1 ~ 7
    
    adj_list = [None] * (n_nodes + 1) # 7 x 7인데 0인덱스는 사용하지 않기 때문에 (7 + 1)
    
    for i in range(1, n_nodes + 1):
        adj_list[i] = []
    
    for a, b in myInput:
        # print('a:', a, 'b:', b)
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    count = 0
    visited = set()
    
    def dfs(cur_node):
        nonlocal count
        
        visited.add(cur_node)
        
        for friend in adj_list[cur_node]:
            # 친구이다
            if friend not in visited:
                count += 1
                dfs(friend)
        
    dfs(1)

    return count
    
