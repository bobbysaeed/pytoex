# Write function find_code() that takes a list of integers and prints True if it contains 007 in order.

def find_code(int_list):
    for i in range(len(int_list)):
        if int_list[i:i+3] == [0, 0, 7]:
            print(True)
