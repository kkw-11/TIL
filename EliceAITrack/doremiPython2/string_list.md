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
my_str.split() # "1 2 3 4 5" -> ['1','2','3','4','5']
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
my_str = "1/2/3/4/5"
print(my_str.split('/'))

my_str = "beetea"
var1 = my_str.split('e')
print(var1)

my_list = ["Seeing", "is", "Believing"]
var2 = " ".join(my_list)
print(var2)
```

```python
'''
공백으로 구분된 5개의 숫자문자열을 쪼개서 리스트에 저장하고, 저장된 리스트의 각 요소를 5개의 변수에 int형으로 저장하기

'''

str1 = "11 22 33 44 55"
list1 = str1.split()
print(list1) # ['11', '22', '33', '44', '55']
print(type(list1[0])) # <class 'str'>
a,b,c,d,e = map(int, list1) # 인덱스마다 저장된 각각의 요소(str 타입)를 int 타입으로 mapping하여 a,b,c,d,e에 저장하기

print(a,b,c,d,e) # 11 22 33 44 55

```