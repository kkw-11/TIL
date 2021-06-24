# tuple
* 자료의 삭제, 추가, 변경이 불가능한 시퀀스 자료형
* 소괄호로 묶어서 표현
* Index 번호를 이용한 인덱싱, 슬라이싱은 가능, in 연산자로 tuple안에 원소 확인, len 연산자로 튜플의 길이 확인, +연산자로 tuple과 tuple을 연결 * 연산자로 튜플 반복은 가능하나, append, remove 등으로 자료를 추가하거나 삭제 불가, 그리고 인덱스번호로 특정위치의 값을 새로 변경하는 것도 불가능 하다.

```python
tuple_zero = ()
tuple_one = (1,)
tuple_ = (1,2,3,4,5)
tuple_ = 1,2,3,4,5 # 괄호 없이 선언해줘도 파이썬은 튜플로 인식함
```

# 실습
## Tuple 만들기
```python
'''
이렇게 해봐요!
숫자 1, 2, 3, 4, 5이 담긴 튜플 my_tuple을 하나 선언해봅시다.

my_tuple의 인덱스 2의 원소를 변수 var1에 넣어봅시다.

my_tuple의 인덱스 1, 2, 3의 원소를 슬라이싱하여 변수 var2에 넣어봅시다.

my_tuple의 길이를 변수 var3에 넣어봅시다.
'''
my_tuple = (1,2,3,4,5)


var1 = my_tuple[2]

var2 = my_tuple[1:4]

var3 = len(my_tuple)

print(var1,var2,var3)
```
## Tuple vs List
```python
'''
이렇게 해봐요!
5번째 줄에 my_tuple의 인덱스 2의 원소를 5로 바꿔치기 해봅시다.

11번째 줄에 my_tuple에 숫자 6을 추가해봅시다. (.append() 이용)

Tip!
try-except는 예외 처리구문입니다. 우선 try문 안에 있는 내용을 실행하다가, 오류가 발생하면 except문 안에 있는 내용을 실행합니다.
'''
my_tuple = (1, 2, 3)

try:
    #여기에 인덱싱을 이용해서 Tuple의 값을 변경해봅시다.
    my_tuple[2] = 5
    
except TypeError:
    print("Tuple은 값을 변경할 수 없습니다.")
    
try:
    #여기에 .append()를 이용해서 Tuple의 값을 추가해봅시다.
    my_tuple.append(6)
    
except AttributeError:
    print("Tuple은 값을 추가할 수 없습니다.")
```