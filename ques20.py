user_input = input("Enter numbers separated by spaces: ")
number_strings = user_input.split()
total = 0
for number_string in number_strings:
    total += int(number_string)
print("The sum of the numbers is:", total)
