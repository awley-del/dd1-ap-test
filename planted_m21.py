# BOUNTY-TEST M-21: planted defect - hardcoded password and eval on user input
ADMIN_PASSWORD = "SuperSecret123!"

def main():
    user_input = input("Enter expression: ")
    print(eval(user_input))

if __name__ == "__main__":
    main()





