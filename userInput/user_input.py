
def input_details():
    name = input("Enter your name: ")
    while True:
        age = input("Enter your age: ")
        if age.isdigit():
            age = int(age)
            break
        else:
            print("Please enter a valid age.")

    location = input("Enter your location: ")
    
    print("Hello, " + name + "!"+ " I guess you are " + str(age) + " year(s) old and you live in " + location + ".")
    
    
input_details()