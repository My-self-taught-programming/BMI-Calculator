import pyfiglet
banner = pyfiglet.figlet_format("BMI.PY")

print(banner)
print("Welcome to Body Mass Index calculator")

while True:
    # The below code will run and if you wish the program to stop enter 'N'.
    quit = input("Would you like to determine your BMI?: Y/N \n")
    if quit == "N":
        break

    # Name of user 
    name = input("What is you name?\n ")
    
    

    # Below is the users height and weight as the result of the input function and are then saved as a float variable.
    height_input = input("What is you height in centimeters? ")
    float_height = float(height_input)

    weight_input = input("What is your weight in kilograms? ")
    float_weight = float(weight_input)

    # A Class function which will take the above input
    class Person():
        def __init__(self, name, float_weight,float_height):
            self.name = name
            self.float_weight = float_weight
            self.float_height = float_height
            self.bmi = (float_weight/(float_height*float_height))*10000


    user = Person(name, float_weight, float_height)

    # The below message  will run for every BMI categories.
    message = "\nUnder the BMI categories for adults 20 years old or over you are classed as "
    
    # Below if statement for BMI classed as Underweight
    if user.bmi <= 18.5:
        print(message, "underweight")
        print(f"\nSpeak with your health care provider {user.name}.")

    # Below if statement for BMI classed as Healthy
    elif user.bmi >= 18.5 and user.bmi <= 24.9:
            print(message, "having a healthy weight")
            print(f"\nSpeak with your health care provider {user.name} if you have further questions.")

    # Below if statement for BMI classed as Overweight
    elif user.bmi >= 25.0 and user.bmi <= 29.9:
            print(message, "being overweight")
            print(f"\nSpeak with your health care provider {user.name}")

    # Below if statement for BMI classed as Obese
    elif user.bmi >= 30.0:
            print(message, "Obese")
            print(f"\nSpeak with your health care provider {user.name}")


