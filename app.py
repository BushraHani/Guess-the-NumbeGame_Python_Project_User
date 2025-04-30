import random

print(" 🤔 Guess the Number between 1 and 30!")

number = random.randint(1,30)

while True:
    
    guess = int(input("💭 Enter Your guess number:"))
    if guess < number:
        print(" 🔅 Too low Number")
    elif guess > number:
        print("⚡ Too High Number")  
    else:
        print(" 👏 Congratulations! You have got Right Number") 
        break     
        


