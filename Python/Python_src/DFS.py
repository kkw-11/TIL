def dfs(graph, vertex, visited):

    visited[vertex] = True 
    print(vertex,end = ' ') # 현재 방문한 노드 출력
    
    # 현재 방문한 노드(vertex)에 연결된 정보 그래프 리스트에서 꺼내면서(i) 그곳(i)이 방문 하지 않았다면 다음 그래프 깊이우선탐색 진행
    for i in graph[vertex]: 
        if not visited[i]:
            dfs(graph, i, visited)

#그래프 연결 정보 인접리스트로 표현
graph = [[], #노드 0에 연결된 노드
[2,3,8], # 노드1에 연결된 노드
[1,7], # 노드 2에 연결된 노드
[1,4,5], # 노드 3에 연결된 노드
[3,5], # 노드 4에 연결된 노드
[3,4], # 노드 5에 연결된 노드
[7], # 노드 6에 연결되 노드
[2,6,8], # 노드 7에 연결된 노드
[1,7] # 노드 8에 연결된 노드
]

visited = [False] * 9

start = 1
dfs(graph,start,visited)