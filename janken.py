def result(user_choice, com):
    if (user_choice == com):
        print("tie")
        count["tie"] += 1
    elif ((user_choice == 1 and com == 3) or (user_choice == 2 and com == 1) or (user_choice == 3 and com == 2)):
        print(name + " win")
        count["win"] += 1
    else:
        print(name + " lose")
        count["lose"] += 1


count = {"win": 0, "lose": 0, "tie": 0}

name = input("Enter your name:")
print("your name is " + name)
user = []
com = [1, 2, 1, 3, 1]
print("1--Rock ; 2--Paper ; 3--Sister")
for i in range(5):
    user_choice = int(input((str(i+1))+"回目:"))
    user.append(user_choice)
    print(user_choice)
    result(user[i], com[i])
print("win = " + str(count["win"]) + ", lose = " +
      str(count["lose"]) + ", tie = " + str(count["tie"]))
