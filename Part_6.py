#To check if the given number is Palindrome.    
def rev(a):
    remainder = 0
    reverse = 0
    while(a != 0):
        remainder = a % 10
        reverse = reverse * 10 + remainder
        a = int(a / 10)
    return reverse

    n = int(input("Enter the number: "))
    a = n
    res = rev(a)
    if (res == n):
        print(n,"IS A PALINDROME")
    else:
        print(n,"NOT A PALINDROME")
