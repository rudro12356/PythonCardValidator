# Author: Rudro
# Date : 12/18/2020
# Brief:This is a project to check if a given credit card number is valid.We will be using our fundamental knowledge of Python to execute this project
# and also the Luhn Algorithm

"""
@https://blog.tecladocode.com/python-30-day-9-project/
1)Remove the rightmost digit from the card number. This number is called the checking digit, and it will be excluded from most of our calculations.
2)Reverse the order of the remaining digits.
3)For this sequence of reversed digits, take the digits at each of the even indices (0, 2, 4, 6, etc.) and double them. If any of the results are greater than 9, subtract 9 from those numbers.
4)Add together all of the results and add the checking digit.
5)If the result is divisible by 10, the number is a valid card number. If it's not, the card number is not valid.

"""
# declare a variable for credit card number and store it in a list
# we have to deal with whitespaces so we will apply the predefined Py function Strip()
user_card_num = list(input("Please enter your card number: ").strip())

# remove the last digit from the card number using pop method
check_digit = user_card_num.pop()

# reverse the card number using the reverse function
user_card_num.reverse()

# create a new empty list to store the modified digits
modified_digit = []

# its time to double the number at even index and subtracting 9 from the result if it is above 9
# we will use for loop to loop through the number and incrementing a counter value

# index = 0

# we will be using the enumerate function to get rid of the stress to track the counter
for index, digit in enumerate(user_card_num):
    if index % 2 == 0:
        #print("Even index.")
        double_digit = int(digit) * 2

        if double_digit > 9:
            double_digit = double_digit - 9

        modified_digit.append(double_digit)
    else:
        #print("Odd index.")
        modified_digit.append(int(digit))

# increment the index variable
# index+=1


#check total and see if it is divisible by 10
"""
total = int(check_digit)

for digit in modified_digit:
    #total = total + digit
"""
total = int(check_digit) + sum(modified_digit)

if total % 10 == 0:
    print("Valid!")
else:
    print("Invalid!")

