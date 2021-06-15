# join 함수
* join함수는 매개변수로 들어온 리스트를 하나하나 합쳐 문자열로 반환하는 함수입니다.

## join 함수 사용법
* '구분자'.join(listA)로 사용합니다. 
    * 이렇게 사용하면 listA의 각 요소들이 구분자를 사이에 두고 연결된 문자열이 됩니다.
    * ''.join(\['a','b','c'\])
    * 이때 listA의 각 요소들은 문자여야합니다.
    * 만약 list의 각 요소들이 int형이 였다면 str형으로 변환해준 후 join 함수를 사용하면 됩니다.

## join 함수 실습

```python
strA = ['1','2','3','4']
print(strA)

res = ''.join(strA)

print(res)
```
![image](https://user-images.githubusercontent.com/76929823/121509213-5f81b680-ca21-11eb-82a5-2929fc28ecf0.png)


```python
intA = [1,2,3,4]
res2 = ''.join(map(str,intA))

print(res2)
``` 

![image](https://user-images.githubusercontent.com/76929823/121509150-51339a80-ca21-11eb-9246-9787d328ddbf.png)

```python
Seeing = 1
Believing =2
my_list = [Seeing, 'is', Believing]

var2 = " ".join(map(str,my_list)) # join의 매개변수로는 문자열 요소로만 구성된 리스트가 있어야 각 문자열 요소들을 합쳐서 문자열을 만들어 낼 수 있다. 그렇게 하기 위해서 map 함수를 통해 리스트의 각 요소들을 string으로 매핑해주어야 한다.
```