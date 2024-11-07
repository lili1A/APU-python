# part a
# how to use the Selection control statements (if, if..else, if..elif..else) 

# i: checks if x is greater than y.
x = 6
y = 9 
if (x > y):
    print("x is greater than y")
else: 
    print("y is greater than x")
# checks if x is equal to y.
x = 7 
y = -8
if (x == y):
    print("x is equal y")
else: 
    print("y is not equal to x")
# checks if x  and y is both greater than 10 and less than 20.
x = 30
y = 23
if (x > 10) and (y > 10) and (x < 20) and (x < 20):
    print("x and y are both greater than 10 and less than 20")
else: 
    print("x and y are both not greater than 10 and less than 20.")
# checks if x is either greater than 0 or not having the same value as y
x = 67
y = 8
if not ((x < 0) or (x == y)):
    print("x is > 0 or is not equal to y")
else: 
    print("x is not > 0 or is not equal to y")
# calculate the sum of x and y
x = 67
y = 8
if not (isinstance(x, int) and isinstance(y, int)):
    print("sum unavailable")
else: 
    res = x + y
    print(f"sum: {res}")
# checks if x is divisible by
x = 67
y = 0
if not (isinstance(x, int) and isinstance(y, int)) or (y == 0):
    print("sum unavailable")
else: 
    res = x / y
    print(f"sum: {res}")
    
""" 2. What is the output of the following Python expression?
(5 > 3) and (7 < 10)
(10 == 5) or (3 != 3)
not(6 >= 8)
(2 + 2== 5) and (8 < 9)
(7 >= 9) or (4 == 4)
 """
one = 5 > 3 # This is True because 5 is indeed greater than 3.
two = 7 < 10 # This is True because 7 is less than 10.
three =  not 6 >= 8 #6 >= 8 is False, and not False is True.
four = 2 + 2 == 5 and 8 < 9 # The and operator requires both sides to be True to return True. Since one part is False, the whole expression is False.
five = 7 >= 9 or 4 == 4 # The or operator requires only one side to be True to return True. Since one part is True, the whole expression is True.
print(f"one: {one} \n two: {two} \n three: {three} \n four: {four} \n five: {five}")

# Write a program to check if the given number is even or odd.
num = 33
if (num %2 == 0):
    print(f"Number {num} is even")
else: 
    print(f"Number {num} is not even")
    
# Write a program to display profit or loss in trading of an item.
""" Sample input/output:
Enter selling price: 20
Enter buying price:19
You have profit in trading of this item """
while True:
    try:
        input1 = float(input(" Enter selling price: "))
        input2 = float(input(" Enter buying price: "))
        
        if input1 < 0 and input < 0:
            print("Price must not be a negative number")
            continue
        break
    except ValueError:
        print("Invalid input, NaN")
        
if (input1 > input2):
    print("You have profit in trading of this item")
else: 
    print("You don't have profit in trading of this item")
    
# part B 
""" Create a Python program that presents a menu to the user and allows them to make selections. The menu should display the following options:
i. Calculate the area of rectangle
ii. Check entered character is vowel or consonant. 
iii. Find smallest of three numbers. 
iv. Exit """

menu = "Choose one option: \n i. Calculate the area of rectangle \n ii. Check entered character is vowel or consonant \n iii. Find smallest of three numbers \n iv. Exit\n "
print(menu)
while True:
    try:
        user_input = input("Choose i/ii/iii/iv: ").strip().lower()
        
        if user_input == "i":
            # Loop until valid numeric input is provided for length and width
            while True:
                try:
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    
                    # Check if length and width are positive values
                    if length <= 0 or width <= 0 :
                        print("Length and width must be positive numbers. Please enter valid values.")
                        continue  # Restart the loop to re-enter values if they are negative

                    area = length * width
                    print(f"The area is: {area}")
                    break  # Exit the loop when valid inputs are entered
                except ValueError:
                    print("Invalid input. Please enter numeric values for length and width.")  # Error message if input is not a number

        elif user_input == "ii":
            while True:  # Loop to keep asking for valid input
                char = input("Enter a single English character: ").strip().lower()
                
                # Check if input is a single alphabetic character in the English language
                if len(char) == 1 and char.isalpha() and 'a' <= char <= 'z':
                    vowels = 'aeiou'
                    
                    if char in vowels:
                        print(f"The character '{char}' is a vowel.")
                    else:
                        print(f"The character '{char}' is a consonant.")
                    break  # Exit the loop if valid input is provided
                else:
                    print("Invalid input. Please enter a single English letter (A-Z).")

        elif user_input == "iii":
            # Prompt the user to enter three numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            num3 = float(input("Enter the third number: "))

            # Find and print the smallest of the three numbers
            smallest = min(num1, num2, num3)
            print(f"The smallest number is: {smallest}")

        elif user_input == "iv":
            print("Exiting the program.")
            break  # Exit the while loop to terminate the program

        else:
            print("Invalid option. Please choose i, ii, iii, or iv.")
            continue  # Restart loop to re-prompt for valid option

    except ValueError:
        print("Invalid input. Please enter numeric values for length, width, and numbers in option iii.")


# Write a Python program to check a year is a leap year or not a leap year.

def isyearleap(x):
    if x%4 == 0:
        print(f"{x} is a leap year")
    else:
        print(f"{x} is not a leap year")
year1 = 2016
year2 = 2023
isyearleap(year1)
isyearleap(year2)

""" Problem: A company insures its drivers based on the following cases:
i. If the driver is married.
ii. If the driver is unmarried, male, and above 30 years of age.
111. If the driver is unmarried, female and above 25 years of age. 
iv. In all the other cases, the driver is not insured.
Let's the marital status, gender, and age of the driver are the inputs, write a Python program to determine whether the driver is insured or not.
 """
 
def insurance(name, sex, age, status):
    if status == "married":
        print(f"Driver {name} is insured")
    elif sex == "male" and age >= 30 and status == "unmarried":
        print(f"Driver {name} is insured")
    elif sex == "female" and age >= 25 and status == "unmarried":
        print(f"Driver {name} is insured")
    else:
        print(f"Driver {name} is not insured")
# Example usage with a driver
driver1_name = "James"
driver1_sex = "male"
driver1_age = 32
driver1_status= "unmarried"
# Calling the function for driver1
insurance(driver1_name, driver1_sex, driver1_age, driver1_status)
driver1_name = "Marie"
driver2_sex = "female"
driver2_age = 23
driver2_status = "unmarried"

# Calling the function for driver2
insurance(driver1_name, driver2_sex, driver2_age, driver2_status)

""" The program will accept two numbers from the operator, then compare it and prints either the message identifying the greater number or the message stating that both numbers are equal.
Sample input - output
Enter Number 1: 5
Enter Number 2: 10
10 is greater than 5. """

while True:
    try:
        num1 = float(input("Enter Number 1: "))
        num2 = float(input("Enter Number 2: "))
    
        if num1 > num2:
            print(f"{num1} is greater than {num2}.")
        elif num1 < num2 :
            print(f"{num2} is greater than {num1}.")
        else:
            print(f"Both numbers {num1} and {num2} are equal.")
        continue_choice = input("Do you wish to continue comparing numbers? Yes/no: ").strip().lower()
        if continue_choice!= "yes":
            print("Exiting the program.")
            break
    except ValueError:
        print("Invalid input. Enter numbers")
        
# Write a Python program to handle ZeroDivisionError Exception with Try Except statements
while True:
    try:
        num1 = float(input("Enter Number 1: "))
        num2 = float(input("Enter Number 2: "))
        division = num1 / num2
        print(f"Result: {division}")
        break
    except ZeroDivisionError:
        print("Invalid input. Cannot divide by 0")
    except ValueError:
        print("Invalid input. Enter numbers")
        
# part c
print("PART C.1")
""" 1. Calculate employee weekly pay. The program will read the employee's name, 
his total number of hours worked 
and hourly wage rate. 
Weekly pay is calculated as payment for regular hours (first 40 hours), 
plus payment for overtime hours worked. 
Payment for regular hours worked is calculated as (wage rate times regular hours worked);
payment for overtime hours worked is calculated as (wage rate times overtime hours worked times 1.5).
Display the employee's name and his weekly pay to the screen.
Sample input - output
Enter name: John
Enter total number of hours worked: 50
Enter hourly rate RM: 10
John received RM 550.00.
         """
def employee_weekly_pay(name, worked_hours, hourly_wage_rate):
    if worked_hours <= 40:
        weekly_pay = worked_hours * hourly_wage_rate
        print(f"{name}'s weekly pay is {weekly_pay} $")
    else:
        overtime_difference = worked_hours - 40
        weekly_pay = overtime_difference * hourly_wage_rate * 1.5
        print(f"{name}'s weekly pay is {weekly_pay} $")

employee1_name = "Vannesa"
employee1_worked_hours = 39
employee1_hourly_wage_rate = 16
employee_weekly_pay(employee1_name, employee1_worked_hours, employee1_hourly_wage_rate)
employee2_name = "Jane"
employee2_worked_hours = 40
employee2_hourly_wage_rate = 13
employee_weekly_pay(employee2_name, employee2_worked_hours, employee2_hourly_wage_rate)

""" PCK Limited wishes to employ a systems analyst to undertake a major project. The decision will be based on the following:
If a person is suitably qualified, has experience of more than 5 years and is aged over 30, he will be called for an interview.
If he is less than 30 years old but qualified and has the necessary experience, he will also be called for an interview. 
If the candidate is qualified and is aged over 30 but lack of experience, he will be rejected. 
If the person is qualified but is neither experienced nor over 30 years old, his record will be kept on file.
If he does not have the necessary qualification but the candidate is experienced and is over 30 years old, he will be called for an interview. If he has the relevant experience but not the qualification and is under-aged, his record will be kept on file. 
If he does not have the necessary qualification or experience but is aged over 30 his application will be rejected. 
He will also be rejected if he does not meet all conditions.
Sample input - output
Enter number of years of experience: 5
Enter age: 28
Qualified (1- Yes, 0 - No) :1
Decision: Call for interview
 """
print("PART C.2")
# arguments:
# name, age, experience, qualification
def interview(name, age, experience, qualification):
    if age <30 and qualification == "yes" and experience == "yes":
        print(f" Call {name} for interview")
    elif age > 30 and qualification == "yes" and experience == "no":
        print(f" Reject {name}'s application for interview")
    elif age <30 and qualification == "yes" and experience == "no":
         print(f" Keep {name}'s application for interview in the file")
    elif age > 30 and qualification == "no" and experience == "yes":
        print(f" Call {name} for interview")
    elif age > 30 and qualification == "no" and experience == "no":
        print(f" Reject {name}'s application for interview")
    else:
        print(f" Reject {name}'s application for interview")
    
interview("Alice", 28, "yes", "yes")
interview("Bob", 35, "no", "yes")
interview("Charlie", 25, "no", "yes")
interview("David", 32, "yes", "no")
interview("Eva", 29, "yes", "no")
interview("Frank", 40, "yes", "no")
interview("Grace", 22, "yes", "yes")
interview("Hannah", 33, "yes", "yes")
interview("Ian", 30, "no", "yes")
interview("Jack", 27, "no", "no")
