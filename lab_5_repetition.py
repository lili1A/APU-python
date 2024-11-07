# part a
""" Extend your solution from the question B1 from previous week (selection tutorial)
using while loop to repeat the program until user entered - 1. """
menu = "Choose one option: \n i. Calculate the area of rectangle \n ii. Check entered character is vowel or consonant \n iii. Find smallest of three numbers \n iv. Exit\n "
print(menu)
print("ALREADY USED WHILE TRUE")
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

# Write a program that able to print the even number that in the between of 2 to 50.

count = 0 # counter for numbers 
width = 4 # Field width for each number
for i in range(2, 50):
    if i % 2 == 0:
        print(f"{i:>{width}}", end=" ")
        count += 1
        if count == 4:
            print()
            count = 0
# Formatting f"{i:>{width}}" in an f-string is a way to control the output of values

# ​​with a specific alignment and width

# i: This is the variable whose value we want to format and output.

# :: This symbol indicates that a formatting specification follows.

# >: This specifies the alignment of the value in the field. In this case, 
# > means that the value will be right-aligned. That is, 
# if the number or string is smaller than the specified field size, 
# a space will be added on the left to align the value to the right.

# {width}: This is a variable that specifies the width of the field where the value of i will be placed.

# part b
print("PART B")
# 1. Write a Python program to display numbers from 1 to 20. Note: use all types of repetitive structures
count = 0 
width = 10
for i in range(1, 21):
    print(f"{i:>{width}}", end=" ")
    count += 1
    if count == 4:
        print()
        count = 0
# 2. Write a Python program to create a multiplication table of 7.
print("    ")
count = 0 
width = 10
for i in range(1, 13): # Looping over 1 to 12 (multiples of 7)
    mult = i * 7
    print(f"{mult:>{width}}", end=" ")
    count += 1
    if count == 4:
        print()
        count = 0
        
""" 3. Create a guessing game in Python.
The Game Logic
a. The Number Guessing Game revolves around a few key elements:
i. Generating a Random Number: The game will randomly generate a number between 1 and 10, which you will have to guess.
ii. Limited Attempts: You will have a maximum of 5 attempts to guess the correct number. Can you solve the mystery within these attempts? 
iii. Feedback Loop: After each guess, the game will provide feedback on whether your guess is too low or too high. This will guide you in making your subsequent guesses.
iv. Victory or Defeat: If you successfully guess the number within the given attempts, you will be celebrated for your guessing prowess. If not, the game will reveal the correct number.
     """
     
# i will use triangular() method 
import random
low = 1
high = 10


random_number = random.triangular(low, high)
rounded_number = round(random_number)
print(f"Rounded: {rounded_number}")
print("You have 5 attempts to guess a number in the ranhe from 1 to 10")

# initialization of the attempts counter 
attempts = 0 
max_attempts = 5 
# game 

while attempts < max_attempts:
    try:
        guess = float(input("Enter a number: "))
        attempts +=1
        if guess == rounded_number:
            print("You won!")
            break
        else:
            remaining_attempts = max_attempts - attempts
            if guess > 10 or guess <= 0:
                print("The number is out of range! Please enter a number between 1 and 10.")
            elif remaining_attempts > 0:
                if guess > random_number:
                    print(f"Wrong guess! You have {remaining_attempts} attempts left. Hint: {guess} is a bigger number than the answer")
                if guess < random_number:
                    print(f"Wrong guess! You have {remaining_attempts} attempts left. Hint: {guess} is smaller number than the answer")
            else: 
                print("Sorry, you've used all your attempts! The correct number was", rounded_number)
                break
    except ValueError:
        print("Entered number is not a number")