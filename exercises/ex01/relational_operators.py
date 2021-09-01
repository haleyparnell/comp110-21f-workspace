"""ex01 relational_operators!"""

__author__ = "730514769"

left_input: str = input("Left-hand side: ")
right_input: str = input("Right-hand side: ")
a = int(left_input)
b = int(right_input)

lessthan_1 = int(left_input) < int(right_input)
lessthan_2 = str(lessthan_1)
print(left_input + " < " + right_input + " is " + lessthan_2)

atleast_1 = int(left_input) >= int(right_input)
atleast_2 = str(atleast_1)
print(left_input + " >= " + right_input + " is " + atleast_2)

equal_1 = int(left_input) == int(right_input)
equal_2 = str(equal_1)
print(left_input + " == " + right_input + " is " + equal_2)

notequal_1 = int(left_input) != int(right_input)
notequal_2 = str(notequal_1)
print(left_input + " != " + right_input + " is " + notequal_2)