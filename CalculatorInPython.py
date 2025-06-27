import math

# add function
def add(first,second):
    return first + second

# subtract function 
def sub(first,second):
    return first - second

# divide fiunction
def div(first,seccond):
    # add if for divide
    try:
        return first / seccond
    
    except ZeroDivisionError:
        print("You can not divide by zero \n Try again Math Error")

# multiply function
def multiply(first,second):
    return first * second

# # soon
# # function for power
# def power(first,second):
#     return math.pow()
    


# user input
print('---------------------------------')
print('-------Python Calculator---------')
print('---------------------------------')

print()

user_name = input('👋 Provide your name: ')

print("--------------------------------")
print()

is_running = True
# iterating the user experience

while is_running :
    
    try:
        user_first = int(input('Enter first number: '))
        user_secon = int(input('Enter second number: '))
        user_operators = input('Choose operator 👉(+ , - , / , *) : ')
            
        if user_operators == '+':
            # envoking function
            print()
            print(f"Answer ✅  : {add(user_first,user_secon)}")

        elif user_operators == '-':
            print()
            print(f"Answer ✅ : {sub(user_first,user_secon)}")
            
        elif user_operators == '/':

            if user_secon == 0:
                print()
                print(" ❎ ---")
                print(" ❗❗ You can not divide by zero \n Try again Math Error")
            else:
                print()
                print(f"Answer ✅  : {div(user_first,user_secon):.2f}")

        elif user_operators == '*':
            print()
            print(f"Answer ✅ : {multiply(user_first, user_secon)}")

        else:
            print()
            print("❗ No operator chosen")
    except ValueError:
        print()
        print('only numbers are allowed 😊')
      
    # User to decide 
    to_continue = input('Do you want to continue(y/n)?: ').upper()

    if to_continue =="N":

        is_running = False
    else:
        is_running
    # while is_running:

    #     if to_continue == 'N':
    #         # breaking the while loop
    #         is_running == False    

    #     is_running == False

print()
print(f"😊 Thank you for using our Calculator {user_name}.")
print()
print("--------------------------------")
#Program Done 

# Developed by :Frans Chokoe
# Date : 27 June 2025 (22:45)
