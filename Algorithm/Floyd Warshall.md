# 플로이드 와샬 알고리즘
* 거쳐가는 정점을 기준으로 최단거리를 구하는 알고리즘

# n = 노드 개수
```
for k in range(n):			# 모든 노드를 중간점으로 삼으면서
	for i in range(n):		# 거리행렬을 순회
    	for j in range(n):	
            if arr[i][j] > arr[i][k] + arr[k][j]:	# 이때, 원래 저장돼 있던 i부터 j까지의 거리보다 
                arr[i][j] = arr[i][k] + arr[k][j]	# k를 거쳐가는 i-k-j 거리가 더 짧다면 갱신함

#거리행렬? https://zetawiki.com/wiki/%EA%B1%B0%EB%A6%AC_%ED%96%89%EB%A0%AC
```


