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
```python
'''
이렇게 해봐요!
다음 대응관계가 담긴 Dictionary를 하나 만들고, 이를 변수 my_dict에 넣어봅시다.
“사과” → “apple”
“바나나” → “banana”
“당근” → “carrot”
사과를 영어로 뭐라고 할까요? my_dict에서 “사과”를 Key로 넣어 나온 Value를 변수 var1에 넣어봅시다.
당근은 싫어요! my_dict에서 당근-carrot을 제거해봅시다.
체리는 좋아요! my_dict에서 체리-cherry를 추가해봅시다.
Tip!
Dictionary의 Key나 Value를 문자열로 설정할 땐 “”, ‘’(따옴표)를 잊지 마세요!
Dictionary를 어디에 활용할 수 있을까요? 한번 생각해봅시다!
Dictionary의 원소를 제거할 때는del Keyword를 사용합니다.
'''
my_dict = {"사과":"apple","바나나":"banana","당근":"carrot"}
print(my_dict)
var1 = my_dict["사과"]
print(var1)
del my_dict["당근"]
my_dict["체리"] = "cherry"
print(my_dict)

```


```python
'''
이렇게 해봐요!
빈 Dictionary를 만들고, 이를 변수 my_dict에 넣어봅시다.

my_dict에 다음 대응관계를 넣어봅시다.

1 → “Integer”
‘a’ → “String”
(1, 2, 3) → “Tuple”
my_dict에 다음 대응관계를 추가하는 코드를 10번째 줄에 작성해봅시다.
[1, 2, 3] → “List”
Tip!
try-except는 예외 처리구문입니다. 이는 추후 강좌에서 다룰 내용이에요! 조금만 기다려 주세요 :)
Key와 Value의 문자열의 철자와 대소문자에 주의하세요!
'''

my_dict = {}
my_dict[1] = "Integer"
my_dict['a'] = "String"
my_dict[(1,2,3)] = "Tuple"

print(my_dict)
try:
    #여기에 [1, 2, 3] → "List"의 대응관계를 만들어봅시다.
    my_dict[[1,2,3]] = "List"
    
except TypeError:
    print("List는 Dictionary의 Key가 될 수 없습니다.")
```


```python
'''
Bello, Tulaliloo ti amo!
영화 <슈퍼 배드>에 나오는 미니언즈는 Minionese라고 하는 신기한 언어를 사용합니다.
우리가 미니언 용어를 모르기 때문에 Minionese를 한국어로 번역해주는 사전을 하나 만들고자 합니다.

아래 미니언 용어 사전을 참고해서
key = Minionese, value = 한국어인 Dictionary를 변수 miniWord에 담아봅시다.

Minionese	한국어
Bello	안녕
Poopaye	잘가
Tank_yu	고마워
Tulaliloo_ti_amo	우린 너를 사랑해
이렇게 해봐요!
변수 cvs에 미니언들이 한 말들이 리스트에 담겨 있습니다. 이를 수정하지 마세요!

위 대응관계 (Minionese→한국어)를 가진 DIcitionary - miniWord를 만들어봅시다.

miniWord를 이용해 cvs에 담긴 리스트를 이를 한국어로 한 줄에 하나씩 번역하여 출력해봅시다.
'''

cvs = ["Bello", "Bello", "Tulaliloo_ti_amo", "Tank_yu", "Poopaye", "Poopaye"]

# Minionese와 한국어가 담긴 miniWord 딕셔너리를 만드세요.
miniWord = {}
miniWord["Bello"] = "안녕"
miniWord["Poopaye"] = "잘가"
miniWord["Tank_yu"] = "고마워"
miniWord["Tulaliloo_ti_amo"] = "우린 너를 사랑해"


for i in range(len(cvs)):
    print(miniWord[cvs[i]])

```
