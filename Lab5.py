# Program Name: Lab5.py
# Course: IT1114/Section W02
# Student Name: Farzam Dizna
# Assignment Number: Lab5
# Due Date: 02/26/2023
# Purpose: This program will take the input of the users starting number and ending number. It will then display an output of only prime numbers from the starting number to the ending number.
# Source1: https://geekflare.com/prime-number-in-python/#:~:text=Python%20Function%20to%20Check%20for%20Prime%20Number&text=The%20above%20function%20is_prime(),loop%20without%20finding%20a%20factor.
# Source2: https://www.geeksforgeeks.org/program-to-print-first-n-prime-numbers/
# Source3: https://www.youtube.com/watch?v=yUaqdaZ_QJk
StartingNumber = int(input("Starting Number: "))    # collects the starting number
EndingNumber = int(input("Ending Number: "))        # collects the ending number

for i in range(StartingNumber, EndingNumber+1):     # defines the range
    flag = 0                                        # sets flag to equal 0
    for j in range(2, i):                           # function that checks if i is prime or not
        if (i % j == 0):                            # checks if i is divisible by 2, 3, 4, etc. if it is divisible by any of these numbers we set flag to 1, saying that the given number is not a prime number.
            flag = 1                                # sets flag to equal 1
            break
                                                    # if flag is equal to 0 then that means the number is a prime number
    if (flag == 0):                                 # if flag is equal to 0 then we print the number until it reaches the end in the range
        print (i, end = "\n")
