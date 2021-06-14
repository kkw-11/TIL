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




# 실수한 코드
'''
#     #BFS에서 큐에 넣는 의미가 인접한 애들을 탐색했고 이 탐색한 애들로 부터 순서대로 꺼내서 다시 인접한 vertex를 탐색하기 위함이기 때문에 큐에 넣으면서 방문처리를 해주어야한다.
#     #BFS에서 방문처리한 애들을 넣기위해 큐 자료구조를 사용하는 것이기 때문이다. 큐는 먼저 넣은 애들을 먼저 꺼내는 자료구조이기 때문이다. 
#     # 위의 설명을 생각하면 아래의 설명은 의미가 없는 설명이다. BFS에서 큐를 사용한 이유를 명확히 알면 visited처리를 언제 해주어야할지 명확히 알 수 있다.
#
#     #큐에 넣으면서 방문 처리를 하지 않고 큐에서 빼내면서 방문처리를 하면 중복된 애들이 큐에 들어가는 문제 발생한다.
      #큐에서 빼면서 방금 빼낸 것과 연결된 애들을 다음에 탐색하기 위해서 큐에 넣는 작업을 할 것 인데 이때 이미 탐색을 해서 큐에 넣은 애들이 다시 탐색되는 경우가 생긴다. 
#     #인접한 vertex 중에서 visited가 true가 아닌 vertex들을 큐에 넣을 건데 방문하지 않은 vertex라는 의미가 큐에서 뽑지 않은 애들이 되어 버리므로(이유는 )
#     #중복된 애들이 겹칠 수 있다. 
#     #현재 BFS가 인접한 애들을 먼저 방문한다는 의미의 알고리즘이고 인접한 애들을 방문했고 방문한 vertex들부터 다시 연결된 애들을 탐색하기 위해 큐에 방문처리하면서 넣어주면 된다.
'''
# from collections import deque

# def bfs(graph,start, visited):
    
#     queue = deque([start])


#     while queue:
#         vertex = queue.popleft()
#         visited[vertex] = True
#         print(vertex,end=" ")
#         for i in graph[vertex]:
#             if visited[i] != True:
#                 queue.append(i)


# graph= [[] for _ in range(9)]
# visited = [False]*9
# graph[1].append(2)
# graph[1].append(3)
# graph[1].append(8)

# graph[2].append(1)
# graph[2].append(7)

# graph[3].append(1)
# graph[3].append(4)
# graph[3].append(5)

# graph[4].append(3)
# graph[4].append(5)

# graph[5].append(3)
# graph[5].append(4)

# graph[6].append(7)

# graph[7].append(2)
# graph[7].append(6)
# graph[7].append(8)

# graph[8].append(1)
# graph[8].append(7)


# bfs(graph,1,visited)







