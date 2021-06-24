max_time = 100
count = 0

for number in range(max_time):
    print("영희:", number)
    
    if number == 10:
        break
        
for number in range(max_time):
    print("철수:", number)
    
    if number == 10:
        break
        
# 아래 코드가 정상적으로 실행되도록 print_number() 함수를 만드세요.
def print_number(name):
    for number in range(max_time):
        print(name,":",number)
    
        if number == 10:
            break
print_number("영희")
print_number("철수")


        