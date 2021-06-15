a = ['A','B','C']
aLen = len(a)
visited = [0]*aLen
res = [0]*aLen
res_arr = []

def permutaion(depth):
    if depth >= aLen:
        #print(res)
        res_arr.append("".join(res))
        # print(res_arr)

    for i in range(aLen):
        if visited[i]:continue
        visited[i] = 1
        res[depth] = a[i]
        permutaion(depth+1)
        visited[i] = 0
        res[depth] = 0 

permutaion(0)


print(res_arr)

dict_zoro = {}
person = {'name':'Michael','age':10}

#딕셔너리에서 자료 꺼내기
print(person['name']) # Michael 
print(person['age']) # 10

#딕셔너리에 자료 추가하기
person['hometown'] = 'Seoul'

#del 함수로 딕셔너리에서 원소 삭제
del person['age']
print(person) # 