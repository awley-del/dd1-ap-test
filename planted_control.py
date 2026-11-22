# BOUNTY-TEST control: planted defect - hardcoded password and eval on user input
import sys

ADMIN_PASSWORD = "SuperSecret123!"

def login(password):
    return password == ADMIN_PASSWORD

def main():
    user_input = input("Enter expression: ")
    result = eval(user_input)
    print(result)

if __name__ == "__main__":
    main()
