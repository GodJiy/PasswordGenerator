import random

password_list = []
def start_prog():
    print("Welcome to Password Generator")
    choice = input("Would you like continue?(Enter Yes/No): ")

    while choice.lower() == "yes":
        length = int(input("\n What is the password length?: "))
        password = ''


        for i in range(length):
            password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
        print("\n Your password: ", password)

        choice = input("\n Would you like continue?(Enter Yes/No): ")

        if choice.lower() != "yes":
            print("\n Okay,goodbye!")
        else:
            password_list.append(password)
            show_list = input("\n Would you like see your passwords?(Enter Yes/No): ")
            if show_list.lower() != "yes":
                print("\n Okay")
                continue
            else:
                print("\n",password_list)
                continue

start_prog()