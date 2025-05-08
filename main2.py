from random import randint
comp=randint(1,100)
guess=0
a=-2
while(a!=comp):
    a=int(input("enter a random number:"))
    guess+=1

    

    if (a>comp):
       print("lower number please")
    else:
       print("higher number please")

print(f"you have guessed the number {a} in {guess} guesse!! you won!!!")    
