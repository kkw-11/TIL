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
