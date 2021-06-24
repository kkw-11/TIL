'''
함수의 기능
하나의 함수에는 하나의 기능만 있는 경우 여러 장점이 있습니다.

먼저 함수명을 보고 어떠한 기능을 하는지 파악하기가 쉽습니다. 기능이 복잡한 함수는 명확한 함수명을 짓는 것도 어렵습니다.

또한 코드의 재사용이 용이합니다. 기능이 작을수록 다른 곳에서 사용하기가 쉽습니다.

차의 속도를 올리고 출력하는 car_set() 함수의 기능을 분리해볼까요?

지시사항
car_set() 함수에서 speed를 10올리고 반환하는 기능을 대신하는 함수 speed_up()을 정의하세요.
car_set() 함수에서 speed 출력 기능을 대신하는 함수 print_speed()를 정의하세요.
주석된 코드가 정상적으로 실행되어 아래와 같은 결과가 출력되도록 하세요.
'''

def car_set(speed):
    	speed += 10
    
	print("차의 속도는 " + str(speed) + " 입니다.")
	
	return speed
    
def speed_up(speed):
    speed += 10
    
    return speed

def print_speed(speed):
	print("차의 속도는 " + str(speed) + " 입니다.")

my_speed1 = 0
car_set(my_speed1)

# 아래 코드가 정상적으로 실행되도록 speed_up() 함수와 print_speed()를 만드세요.

my_speed2 = 0
my_speed2 = speed_up(my_speed2)
print_speed(my_speed2)