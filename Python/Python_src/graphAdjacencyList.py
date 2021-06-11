# 행(row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3) ]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)