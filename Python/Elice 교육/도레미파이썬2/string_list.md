# 문자열_리스트 활용
* list.pop(i)
    * list에서 원소를 제거할 때 인덱스번호로 제거하는 방법
    * list에서 인덱스 i의 원소를 제거하고 반환
    * str.pop() str에서 마지막 원소를 제거한다.
    * str.pop(0) str에서 0번 인덱스에 있는 원소를 제거한다.
```python
my_list = [1,2,3,4,5]

print(my_list.pop()) # 5

print(my_list.pop(0)) # 1
```

* seq.count(d)
    * 시퀀스 내부에서 특정 원소의 개수를 반환한다.
    * 시퀀스에서 자료 d의 개수를 반환한다.
```python
my_seq = [1,2,2,3,2,5]
print(my_seq.count(2)) # 3
```

* str.split(c)
    * 문자열 -> 리스트 : 쪼갤 문자열.split(기준 문자열)
    * c를 기준으로 문자열을 쪼개서 리스트 반환 (괄호 비울시 공백 기준)
```python
my_str = "1 2 3 4 5"
print(my_str.split()) #['1','2','3','4','5']

element = "Na,Mg,Al,Si"
print(element.split(',')) #['Na','Mg', 'Al','Si']
```

* str.join(list)
    * 리스트 -> 문자열 : 연결할 문자열.join(리스트)
    * str을 기준으로 리스트를 합쳐서 문자열을 반환 (괄호를 비울시 공백 기준)
```python
my_list = ['a','p','p','l','e']
print(''.join(my_list)) # apple

friend = ["Pat","Mat"]
print('&'.joint(friend)) # Pat&Mat 
```


# 실습
## pop, count
```python
'''
이렇게 해봐요!
숫자 1, 2, 2, 3, 3, 3이 담긴 리스트 my_list를 하나 선언해봅시다.

my_list 안의 숫자 3의 개수를 변수 var1에 넣어봅시다.

일부 원소를 제거하여 my_list가 [1, 2, 3]이 되도록 해봅시다.

Tip!
my_list.pop(__)을 사용할 때, pop하는 순서가 매우 중요해요!
리스트의 내용을 확인하려면 이를 출력해보면 되겠죠?
'''
my_list = [1,2,2,3,3,3]
var1 = my_list.count(3)
print(var1)
my_list.pop()
my_list.pop()
my_list.pop(-2)
print(my_list)
```

## split, join
```python
'''
이렇게 해봐요!
문자열 “beetea”가 담긴 변수 my_str를 선언해봅시다.

문자열 ‘e’를 기준으로 my_str를 리스트로 만든 다음, 이를 변수 var1에 담아봅시다.

리스트 ["Seeing", "is", "Believing"]이 담긴 변수 my_list를 선언해봅시다.

공백( )을 기준으로 my_list를 문자열로 만들어보고, 이를 변수 var2에 담아봅시다.

Tip!
split과 join은 어느 자리에 어떤 문자열이 들어가는지 굉장히 헷갈려요! 잘 익혀놓아야겠죠?
각 문자열의 철자와 대소문자 구분에 주의하세요!
'''


my_str = "beetea"
var1 = my_str.split('e')
print(var1) # ['b', '', 't', 'a']


my_str = "be"
var1 = my_str.split('e')
print(var1) # ['b','']

my_str = "bee"
var1 = my_str.split('e')
print(var1) # ['b','','']

my_str = "beet"
var1 = my_str.split('e')
print(var1) # ['b','','t']

my_str = "beetea"
var1 = my_str.split()
print(var1) # ["beetea"]

my_str = "beetea"
var1 = my_str.split('')
print(var1) # error

my_str = "beetea"
var1 = my_str.split('t')
print(var1) # ['bee','ea']


my_list_String_element = ["Seeing", "is", "Believing"]
var2 = " ".join(my_list_String_element)    
print(var2) # Seeing is Believing

Seeing = 1
Believing =2
my_list = [Seeing, 'is', Believing] # Seeing과 Beleiving은 따옴표가 없으므로 변수로 인식됨

var2 = " ".join(map(str,my_list)) # join의 매개변수로는 문자열 요소로만 구성된 리스트가 있어야 각 문자열 요소들을 합쳐서 문자열을 만들어 낼 수 있다. 그렇게 하기 위해서 map 함수를 통해 리스트의 각 요소들을 string으로 매핑해주어야 한다.
print(var2)


'''
이렇게 해봐요!
다음 노래의 가사가 콤마(,)를 기준으로 나뉘어 변수 lyric에 담겨있습니다.

♬ 낙엽을 닮은 - 숨의숲

문자열 lyrics를 콤마를 기준으로 나누어 리스트를 만들어봅시다.

이 리스트의 46번째 구절을 출력해봅시다.

Tip!

46번째 구절을 출력하기 위해서는 인덱스를 어떻게 설정해야 할까요?
'''
lyrics = "낙엽을,닮은,너의,눈동자를,나는,정말,정말,좋아했었어,가을을,닮은,너의,목소리를,나는,아직,아직,잊지,못했어,같이,걸으면서,들었던,낙엽,소리가,내,귓가에,들려오는,것만,같아,함께,앉아,있던,좁다란,나무,벤치엔,너의,온기가,남아있는,것만,같아,낙엽을,닮은,너의,눈동자를,나는,정말,정말,좋아했었어,가을을,닮은,너의,목소리를,나는,아직,아직,잊지,못했어"

my_list =  lyrics.split(',')

print(my_list[45])
```
