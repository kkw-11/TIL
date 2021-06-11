from itertools import permutations

def permu(numbers):
    a = set()
    for i in range(len(numbers)):
        a |= set(map(int, map("".join, permutations(numbers, i + 1))))
    return a
 
print(permu(list("011")))

# print(list("17"))



