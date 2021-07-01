import sys
from collections import deque
sys.setrecursionlimit(100000)


INF = float('inf')

def SNS(n_nodes, myInput, a, b):
    '''
    엘리스친구의 친구관계가 myInput으로 주어지고, 사용자 a, b가 주어질 때 둘 사이의 촌수를 반환합니다.
    '''
    
    adj = [set() for _ in range(n_nodes)]
    
    for u, v in myInput:
        adj[u].add(v)
        adj[v].add(u)
    
    visited = set()
    
    q = deque()
    
    q.append(a)
    
    
    depth = 0
    
    while q:
        nq = deque()
        
        for node in q:
            
            if node == b:
                return depth
                
            for adj_node in adj[node]:
                if adj_node in visited:
                    continue
                nq.append(adj_node)
        
        depth += 1
        q = nq
    
    return -1