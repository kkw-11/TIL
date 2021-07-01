def factorial(num):
    
    # num ~ 1 까지 곱하는
    
    res = 1
    
    for i in range(1, num + 1):
        res *= i
    
    # res = 1 * 2 * 3 * 4 * 5 * ... * num
    
    return res

def main():
    print(factorial(5)) # should return 120

if __name__ == "__main__":
    main()