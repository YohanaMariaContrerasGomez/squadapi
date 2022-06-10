import math

def CalculateLCM(listNumbers):
    numbers = [int(i) for i in listNumbers.split(',')]
    lcm = numbers[0]

    for i in range(1,len(numbers)):
        lcm = lcm*numbers[i]//math.gcd(lcm, numbers[i])

    return lcm
