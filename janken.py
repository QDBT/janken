name = input("Enter your name:")
print("your name is " + name)

user = []
com = [1, 2, 1, 3, 1]
print("1--Rock ; 2--Paper ; 3--Sister")
for i in range(5):
    user_choice = int(input((str(i+1))+"回目:"))
    user.append(user_choice)
    print(user_choice)
    if (user_choice == com[i]):
        print("tie")
    elif ((user_choice == 1 and com[i] == 3) or (user_choice == 2 and com[i] == 1) or (user_choice == 3 and com[i] == 2)):
        print("user win")
    else:
        print("user lose")
