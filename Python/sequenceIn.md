# in 
* in 연산자를 통해 시퀀스에 원소에 원하는 원소가 있는지 확인 할 수 있다.

* 아래 코드는  ["Apple", "Banana", "Chamwae", "Durian"]라는 과일 이름이 담긴 리스트에서 "Egg"가 있는지 확인하여 출력하는 코드입니다.
    * "Egg"가 my_list에 없기 때문에 False가 var에 저장됨
```python

my_list =  ["Apple", "Banana", "Chamwae", "Durian"]

var1 = "Egg" in my_list 

print(var1)
```

# 빈 시퀀스 찾기
* 시퀀스 자료형(리스트, 딕셔너리, 튜플 등)이 비어있는지 확인하는 방법에 대해 알아봅시다.

* 시퀀스 자료형은 값이 들어있으면 참, 값이 들어있지 않으면 거짓을 반환합니다.

* 따라서 len() 함수를 이용해서 반환되는 길이로 시퀀스 자료형이 비어있는지 확인할 필요가 없습니다.

* 아래 예시를 확인해보세요.

```python
# 잘못된 예시
if len(seq):
if not len(seq):

# 올바른 예시
if seq:
if not seq:

my_tuple = ()

if not my_tuple:
    print("튜플에 값이 들어있지 않습니다.")
else:
    print("튜플에 값이 들어있습니다.")
```
