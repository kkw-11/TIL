# dictionary
* 짝꿍이 있는 자료형 
* {key:value}의 형식, key를 알면 value를 알 수 있음
* key는 열쇠처럼 자료를 꺼낼 수 있는 도구
* value는 dictionary에서 꺼낸 자료 dictionary\[key\]
* 딕셔너리의 특징은 key는 변할 수 없는 자료형이여야 한다. -> key에 튜플은 되지만 리스트는 올 수 없다..

```python
dict_zoro = {}
person = {'name':'Michael','age':10}

#딕셔너리에서 자료 꺼내기
print(person['name']) # Michael 
print(person['age']) # 10

#딕셔너리에 자료 추가하기
person['hometown'] = 'Seoul'

#del 함수로 딕셔너리에서 원소 삭제
del person['age']
print(person) # {'name': 'Michael', 'hometown': 'Seoul'}

datas = {[1,2,3]:'Alphabe'} # Error
datas = {(1,2,3):'Number'} # OK
```

# 실습