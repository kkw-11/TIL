# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3) ]

# 노드 0이 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7)) # 노드 0에 노드 1이 연결 되었고 노드 0에서 노드 1로 가는데 거리가 7
graph[0].append((2,5)) # 노드 0에 노드 2가 연결 되었고 노드 0에서 노드 2로 가는데 거리가 5

# 노드 1이 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7))  # 노드 1에 노드 0이 연결 되었고 노드 1에서 노드 0으로 가는데 거리가 7

# 노드 2가 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5)) # 노드 2에 노드 0이 연결 되었고 노드 2에서 노드 0으로 가는데 거리가 5

print(graph)
'''
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
visited = [False] * 9
def DFS(graph, vertex,visited):
    visited[vertex] = True
    print(vertex,end=' ')
    for i in graph[vertex]:
        if not visited[i]:
            DFS(graph,i,visited)

DFS(graph,1,visited)

'''