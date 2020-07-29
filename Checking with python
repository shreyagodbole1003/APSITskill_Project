def menu():
    print("=====MAIN MENU=====")
    print()
    program = input("""
A: To check if the given year is a leap year.
B: To find if the given number is prime or composite.
C: To find prime numbers between the given interval.
D: To test if the given letter is a vowel or a consonent.
E: To check if the given string is Palindrome
F: To check if the given number is Palindrome.
Please enter your choice:  """)
    if program == "A" or program == "a" :
        year = int(input("ENTER A YEAR: "))
        if(test_year(year)): 
            print(year,"IS A LEAP YEAR.") 
        else: 
            print(year,"IS NOT A LEAP YEAR.") 

    elif program == "B" or program == "b" :
        prime_num()
        
    elif program == "C" or program == "c" :
        PrimeNum()
    
    elif program == "D" or program == "d" :
        x=str(input("ENTER AN ALPHABET: "))
        if len(x)>1:
            print("ENTER ONLY ONE ALPHABET")
        elif(test_vowel(x)==True):
            print(x,"IS A VOWEL.")
        else:
            print(x,"IS A CONSONANT")
    elif program == "E" or program == "e" :
        s = str(input("ENTER A STRING: "))
        if(is_palindrome(s)==True):
            print(s,"IS PALINDROME.")
        else:
            print(s,"IS NOT A PALINDROME.") 
    elif program == "F" or program == "f" :
        n = int(input("ENTER A NUMBER: "))
        a = n
        res = rev(a)
        if (res == n):
            print(n,"IS A PALINDROME.")
        else:
            print(n,"IS NOT A PALINDROME.")      
            
    else:
        print("PLEASE ENTER A VALID CHOICE!!")
    ch=input("DO YOU WANT TO TRY AGAIN??(Y/N)")
    if(ch=='y'or ch=="Y"):
        menu()
