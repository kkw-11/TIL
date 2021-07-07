# defaultdict()
* 딕셔너리 자료형의 기본값을 줄 수 있는 함수

* 파이썬에서 dict()함수는 딕셔너리 자료형을 선언하는 함수이다. 이때 딕셔너리를 선언해주고 해당 key값이 없는 경우 없는 eky값을 이용해 값을 출력할경우 에러가 발생한다.
```python
dic1 = dict()
print(dic1['a'])

```

* 그리고 없는 key값에 append를 이용해 리스트 value를 추가하는 행위는 할 수 없다.
```python
dic1 = dict()
dic1['a'].append(1)
```

* 이 경우에는 해당 key가 딕셔너리 자료에 없는 경우 새로 key값과 value를 할당해주는 예외처리 코드를 써주어야 한다.
```python
dict1 = dict()
dict1 = {'a':[]}
if 'a' in dict1: # 'a' 키가 dict1 딕셔너리 변수에 존재한다면
    dict1['a'].append(1)
else:
    dict1['a'] = [1]
``` 

* defaultdict()는 key가 존재하는지 확인하지 않고 기본값을 설정해줄 수 있기 때문에 예외처리 if,else문을 사용하지 않아도 된다.
```python
from collections import defaultdict
defaultDict1 = defaultdict(list) #key값이 없는 경우 빈리스트를 value값으로 설정
defaultDict1['a'].append(1)
print(defaultDict1['a'])
```
