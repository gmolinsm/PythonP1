print("Please enter the numer of primes to calculate: ")
n = int(input())

numberList = list(range(2, n+1))

for i in numberList:
    j = 2
    while(i * j <= numberList[-1]):
        if(i * j in numberList):
            numberList.remove(i*j)
        j += 1

print("The list of prime numbers is:", numberList)

