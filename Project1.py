while True:
    # created a prompt for the terminal/user
    choice = input("Hello, user, please enter a number relating to: 1 temp, 2 weight, 3 distance, 4 inches to centimeters, 5 gallons to liters (0 for quit): ")
    
    # lets the user exit neatly by typing 0
    if choice == "0":
        print("See you next time")
        break
    
    # each conversion option for individual sequences
    if choice == "1":
        print("Ok, now let's convert temperature in Fahrenheit to Celsius")
        f_temp = float(input("Enter temperature in F: "))
        c_temp = (f_temp - 32) * (5 / 9)
        print(f"Result: {f_temp} F is {c_temp} C")
        
    elif choice == "2":
        print("Ok, now let's convert weight in pound to kg")
        pounds = float(input("Enter weight in pound: "))
        kilograms = pounds * 0.453592
        print(f"Result: {pounds} pound is {kilograms} kg")
        
    elif choice == "3":
        print("Ok, now let's convert distance in feet to meter")
        feet = float(input("Enter distance in feet: "))
        meters = feet * 0.3048
        print(f"Result: {feet} feet is {meters} meter")
        
    elif choice == "4":
        print("Ok, now let's convert length in inches to centimeters")
        inches = float(input("Enter length in inches: "))
        centimeters = inches * 2.54
        print(f"Result: {inches} inches is {centimeters} centimeters")
        
    elif choice == "5":
        print("Ok, now let's convert volume in gallons to liters")
        gallons = float(input("Enter volume in gallons: "))
        liters = gallons * 3.78541
        print(f"Result: {gallons} gallons is {liters} liters")
        
    else:
        # error message for the user if wrong call
        print("Please try again with valid option")