# Write a program that pick  a number from the user and prints it back.
import sys

def define_even_odd():
    while True:
        try:
        
            user_number = input('Enter a number ')

            if user_number== "exit":
                sys.exit()
            num = float(user_number)
            return num
        except ValueError:
            print("Invalid input for a number")

if __name__ == "__main__" :
    unum = define_even_odd()

    if unum is not None:
        if unum%2 == 0:

            print("Your number is Even")
        else:
            print("Your number is Odd")
    else:
        print("Enter a valid number")
