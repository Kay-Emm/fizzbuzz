# FizzBuzz is a program that prints:
# Fizz for every factor of 3,
# Buzz for every factor of 5,
# FizzBzuzz for both factors of 3 and 5
# and a number for numbers that are neither factors of 3 nor 5. 


def fizz_buzz():

    for num in range(1, 101):

        if (num % 3 == 0 and num % 5 == 0):
            print("FizzBuzz")
        elif (num % 3  == 0):
            print("Fizz")

        elif (num % 5 == 0):
            print("Buzz")

        else:
            print(num) 

# Using a string to print fizzbuzz
def fizz_buzz_1():
    for num in range(1, 101):
        # this if conditional checks for the case of multiples of 3 

        if num % 3 == 0:
            answer = "Fizz"

        # this second if statement checks for the case
        # where a number is a multiple of both 3 and 5
        # 2 consecutive if statements will simultaneously check for both if constructs
        # if both are true FizzBuzz will be printed, otherwise Buzz for multiples of 5

        if num % 5 == 0:
            answer += "Buzz"

        # the print statement will print the value contained in answer if the conditionals are met
        # otherwise a number is printed
        
        print(answer or num) 

# Making use of tenary operators
def fizz_buzz_2():
    for num in range(1, 101):
        answer = "Fizz" if num % 3 == 0 else ""
        answer += "Buzz" if num % 5 == 0 else ""

        print(num) if answer == "" else print(answer)

if __name__ == '__main__':
        fizz_buzz()
        fizz_buzz_1()
        fizz_buzz_2()

 
