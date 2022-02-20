#code for password generator function
import random
def pwd_gen(length):
    pwd=str()
    C="abcdefghijklmnopqrstuvwxyz"+"0123456789"+"!@#$%^&~_?|"+"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for x in range(length):
        pwd+=random.choice(C)
    return pwd
length=int(input("Enter a length to generate the password:"))
pwd_gen(length)
        
