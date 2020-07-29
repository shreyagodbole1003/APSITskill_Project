#To find prime numbers between the given interval.
def PrimeNum():
    N = int(input("Enter lower range: "))
    M = int(input("Enter upper range: "))
    for num in range(N,M):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)
