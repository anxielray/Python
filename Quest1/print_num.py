# Write a program that pick  a number from the user and prints it back.

def get_user_credentials():
    while True:
        try:
        
            user_number = input('Enter a number')
            num = float(user_number)
            return num
        except ValueError:
            print("Invalid input for a number")

if __name__ == "__main__" :
    unum = get_user_credentials()
    if unum is not None:
        print(f"Your number is {unum}")
    else:
        print("Enter a valid number")
