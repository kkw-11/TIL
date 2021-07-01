import sys
sys.setrecursionlimit(100000)

def numStudents(n_nodes, myInput) :
    '''
    학생들 사이의 친구관계가 myInput으로 주어질 때, 정원이가 퍼트린 소문을 듣게되는 학생의 수를 반환합니다.
    '''
    
    print(n_nodes, myInput)
    # 친구 1 ~ 7
    
    adj_matrix = [None] * (n_nodes + 1)
    # 7 x 7 행렬이지만 0번째 인덱스를 사용하지 않을 거기 때문에 (7 + 1) x (7 + 1)
    for i in range(1, n_nodes + 1):
        adj_matrix[i] = [0] * (n_nodes + 1)
    
    for a, b in myInput:
        adj_matrix[a][b] = 1
        adj_matrix[b][a] = 1
    
    count = 0
    visited = set()
    
    def dfs(cur_node):
        nonlocal count
        
        visited.add(cur_node)
        
        for friend in range(1, n_nodes + 1):
            # 친구이다
            if adj_matrix[cur_node][friend] == 1 and friend not in visited:
                count += 1
                dfs(friend)
        
    dfs(1)

    return count
 