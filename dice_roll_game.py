from random import*
print("....Welcome to dice Rolling Game....")
count=0
while True:

    k = input("Enter your choice (y or n): ")
    if k.lower()=="y":
        while True:
            try:
                choice= int(input("Choose how many dice you want to roll: "))
                if(choice<=0):
                    print("Enter the positive number.")
                    continue
                else:
                    rolls=[]
                    for i in range(1,choice+1):
                        t=(randint(1,6))
                        rolls.append(t)
                print(tuple(rolls))
                count+=1
                print()
                break
            except Exception:
                print("Invalid input! Please enter a valid number.\n")
    elif k.lower()== "n" :
        print("Thanks for Playing!")
        break
    else:
        print("Invalid Choice, write a valid choice.")
    print(f"User has rolled the dices {count} times.")