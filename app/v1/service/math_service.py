import functools
from math import lcm

def CalculateMCM(listNumbers):
    numbers = [int(i) for i in listNumbers.split(',')]
    numbersProof = [1]*len(numbers)
    numberNext = numbers
    loopProof = numbers == numbersProof
    mcmList = list()
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    count = 0

    while(not loopProof):
        numbers = [i/prime[count] if i%prime[count] == 0 else i for i in numbers]
        if numbers == numberNext:
            count += 1
        else:
            mcmList.append(prime[count])
        if numbers == numbersProof:
            loopProof = False
            break
        numberNext = numbers
        if count >= len(prime):
            break

    return functools.reduce(lambda a, b: a*b, mcmList)

def CalculateLCM(listNumbers):
    pass