# Take to note: improve program and accept user input even if user entered
# "Five".
try:
    first_input = float(input("Enter a first number: "))
    second_input = float(input("Enter a second number: "))
except:
    print('You have entered an invalid input.')
else:
    add_them = first_input + second_input
    print('The sum of the two variables is: ',add_them)
finally:
    print('Program execution finished.')
