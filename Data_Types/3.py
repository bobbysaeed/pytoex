inp_1 = int(input("please enter the first number:"))
inp_2 = int(input("please enter the second number:"))
temp_var = inp_1
inp_1 = inp_2
inp_2 = temp_var
del temp_var
print("first number is: ", inp_1, "second number is: ", inp_2)