#To find if the given number is prime or composite.
def prime_num():
    num = int(input("Enter any number : "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is a COMPOSITE number")
                break
        else:
            print(num, "is a PRIME number")
