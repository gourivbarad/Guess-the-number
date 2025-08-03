import random
start=input("Shall we Start the Game : ")
while(start!="No"):
    computer=random.randint(1,10)
    user=int(input("Guess the number: "))
    score=1 if user==computer else 0
    
    if(user==computer):
        print("You won!")
    else:
        print("You Lose")
        
    start=input("Shall we Start the Game : ")
        
    with open("new1.txt","a") as f:
        f.write(str(score)+"\n")
    with open("new1.txt","r") as f:
        lines = f.readlines()
        total_score=sum(int(line.strip()) for line in lines)
        
print("Total Score:", total_score)