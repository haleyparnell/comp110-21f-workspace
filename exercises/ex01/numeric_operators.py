left_input: str = input("Left-hand side: ")
right_input: str = input("Right-hand side: ")
a = int(left_input)
b = int(right_input)

exponent_1 = int(left_input) ** int(right_input)
exponent_2 = str(exponent_1)
print(left_input + " ** " + right_input + " is " + exponent_2)

division_1 = int(left_input) / int(right_input)
division_2 = str(division_1)
print(left_input + " / " + right_input + " is " + division_2)

intdiv_1 = int(left_input) // int(right_input)
intdiv_2 = str(intdiv_1)
print(left_input + " // " + right_input + " is " + intdiv_2)

remain_1 = int(left_input) % int(right_input)
remain_2 = str(remain_1)
print(left_input + " % " + right_input + " is " + remain_2)