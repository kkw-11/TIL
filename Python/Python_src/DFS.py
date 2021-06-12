def dfs(graph, vertex, visited):

    visited[vertex] = True 
    print(vertex,end = ' ') # 현재 방문한 노드 출력
    
    # 현재 방문한 노드(vertex)에 연결된 정보 그래프 리스트에서 꺼내면서(i) 그곳(i)이 방문 하지 않았다면 다음 그래프 깊이우선탐색 진행
    for i in graph[vertex]: 
        if not visited[i]:
            dfs(graph, i, visited)


#그래프 연결 정보 인접리스트로 표현
graph = [[], # 노드 0에 연결된 노드
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

startVertex = 1
dfs(graph,startVertex,visited)


print(graph)
graph2 = [[] for _ in range(9)]
print(graph2)
graph2[1].append(2)
graph2[1].append(3)
graph2[1].append(8)

graph2[2].append(1)
graph2[2].append(7)

graph2[3].append(1)
graph2[3].append(4)
graph2[3].append(5)

graph2[4].append(3)
graph2[4].append(5)

graph2[5].append(3)
graph2[5].append(4)


graph2[6].append(7)

graph2[7].append(2)
graph2[7].append(6)
graph2[7].append(8)

graph2[8].append(1)
graph2[8].append(7)


print(graph2)

if graph == graph2:
    print("graph 같다")



