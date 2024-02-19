# import modules to use pre-build code
import random
import time

# constant variables
OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10


input('press enter to start! ')
print("-------------------")
wrong = 0
# start time 
start_time = time.time()

# functions to generate random basic math questions
def generate_problems():
    left_value = random.randint(MIN_OPERAND, MAX_OPERAND)
    right_value = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = str(left_value)+ " " + operator+ " " + str(right_value)
    answer = eval(expression)
    return expression, answer

# loop through all problems and get answer
for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problems()
    while True:
        guess = input("Problem #"+ str(i+1) + ": " + expression + " = ")
        if guess == str(answer):
            break
        wrong += 1

# end time
end_time = time.time()
# calculate time to finish program
total_time = round(end_time - start_time)

print("-------------------")
print("Nice Work! You finished in", total_time, "seconds!")




