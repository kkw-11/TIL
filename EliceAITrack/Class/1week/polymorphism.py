'''
다형성
다형성이란 동일한 모양의 코드가 다른 동작을 하는 것을 말합니다.
코드는 하나고 기능은 여러기능을 하도록 할 수 있다.
아래 조건문을 한 번 확인해봅시다.
```python
if number == "1":
    print("1입니다.")
elif number == "2":
    print("2입니다.")
```
여기서 숫자가 계속 늘어날수록 같은 print() 함수를 계속 사용해야 합니다.

하지만 클래스와 상속을 통한 다형성을 잘 이용하면 이러한 중복 코드를 제거할 수 있습니다.

조건에 따라 동물의 종류를 출력하는 코드를 지시사항에 따라 다형성으로 구현해보세요.

지시사항
Animal 클래스를 만들고 아래 코드를 클래스 내에 추가하세요.

멤버 변수
```python
species = "모르는 동물"
```
멤버 함수
```python
def say(self):
    print(self.species + "입니다.")

```
Animal 클래스를 상속받은 Dog 클래스를 만들고 species의 값을 강아지로 설정하세요.

Animal 클래스를 상속받은 Cat 클래스를 만들고 species의 값을 고양이로 설정하세요.

Dog 클래스와 Cat 클래스의 인스턴스를 만들고 각각 say() 함수를 호출하세요.


Tips
실습은 if문이 단순하기 때문에 코드가 더 복잡해지는 것처럼 보이지만 다형성을 이용하는 것이 확장성 있는 코드를 작성하는 것입니다.
'''

# animal = "cat"

# if animal == "cat":
#     print("고양이입니다.")
# elif animal == "dog":
#     print("강아지입니다.")
# else:
#     print("모르는 동물입니다.")
    
class Animal:
    species = "모르는 동물"
    
    def say(self):
        print(self.species + "입니다.")

class Dog(Animal):
    species = "강아지"

class Cat(Animal):
    species = "고양이"
    
dog = Dog()
cat = Cat()
# say는 animal에서 작성한 같은 함수이지만  Dog와 Cat클래스에서 Animal을 상속받고 각자 기능을 하도록 하였다. 다형성
dog.say()

cat.say()
