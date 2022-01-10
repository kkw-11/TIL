# Dictionary
* 파이썬에서는 연관된 값들을 묶어서 저장하는 용도로 딕셔너리라는 자료형을 제공합니다.
* 아래와 같이 lux 라는 리스트 자료형에서 인덱스 0은 체력, 인덱스 1은 마나, 인덱스 2는 사거리, 인덱스 3은 방어력이라고 했을 때 리스트만 봐서는 각 값이 어떤 능력치인지 쉽게 알기가 힘듭니다. 이럴 때 각 데이터들을 명확히 구분하여 저장하기 위해서 딕셔너리라는 사용합니다.
```python
lux = [490,334,550,18,72]
```
* 딕셔너리 자료형을 이용해서 게임 능력치를 저장해 보면 아래와 같습니다.
```python
lux = {'health':490, 'mana':334, 'melee':550,'armor':18.72}
```
* 이렇게 딕셔너리에 값을 저장하면 lux라는 캐릭터의 health(체력)은 490, mana는 334, melee(사거리)는 550, armor(방어력)은 18.72라는 것을 쉽게 알 수 있씁니다. 이처럼 딕셔너리는 값마다 이름ㅇ르 붙여서 저장하는 방식입니다.

## 빈 딕셔너리 만들기
* 빈 딕셔너리를 만들 때는 {}만 지정하거나 dict를 사용하면 됩니다.
* 그리고 빈 딕셔너리에 키값과 value는 직접 할당해줄 수 있습니다.
'''python
x = {}
y = dic()
x['health'] = 490
x['mana'] = 334
'''

## dict로 딕셔너리 만들기
* dict는 다음과 같이 키와 값을 연결하거나, 리스트 튜플, 딕셔너리로 딕셔너리를 만들 때 사용합니다.
    * x1 = dict(key1=value1, key2:value2)
    * x2 = dict(zip[key1,key2],[value1,value2])
    * x3 = dict([(key1,key2),(value1,value2)])
    * x4 = dict({key1:value1,key2:value2})

### x1 = dict(key1=value1, key2:value2)
* 첫 번째 방식은 dict에서 key = value 형식으로 딕셔너리를 만들 수 있습니다.
* 이때는 키에 ''(작은 따옴포)나 ""(큰따옴표)를 사용하지 않아야 합니다. 키는 딕셔너리를 만들고 나면 문자열로 바뀝니다.
```python
x1 = dict(health=290,mana=334,melee=550,armor=18.72)
```

### x2 = dict(zip[key1,key2],[value1,value2])
* 두 번째 방식은 dict에서 zip 함수를 이용하는 방법입니다. 다음과 같이 키가 들어 있는 리스트와 값이 들어있는 리스트를 차례대로 zip에 넣은뒤 다시 dict에 넣어주면 됩니다.
* 물론 키와 값을 리스트가 아닌 튜플에 저장해서 zip에 넣어도 됩니다.
```python
x2 = dict(zip(['health','mana','melee','armor'],[490,330,550,18.72]))
```

### x3 = dict([(key1,value),(key2,value)])
* 세번 째 방법은 리스트 안에 (키,값)형식의 튜플을 나열하는 방법입니다.
```python
x3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
```

### x4 = dict({'key1':value1,'key2':value2})
* 네 번째 방법은 dict 안에서 중괄호로 딕셔너리를 생성하는 방법입니다.
```python
x4 = dict({'health':490,'mana':334,'melee':550,'armor':18.72})
```
