from collections import deque
def bfs(graph, startVertex, visited):

    queue = deque([startVertex])

    visited[startVertex] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end = ' ')

        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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
bfs(graph,start,visited)