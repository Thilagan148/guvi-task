import random
a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

c=random.choice(a)
for i in range(len(a)):
    b=input("Enter a letter")
    if(b==c):
        print("Correctly guessed")
        print(15-i)
    else:
        print("Incorrect Guess")
        print(15-i)
        
print("Game over")        
    
