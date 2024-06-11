# Write a program that computes the net amount of a bank account
#  based on a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.

def transaction(trans_type):
    net_amount = sum(trans_type)
    print(net_amount)

transaction_list = []
while True:
    trans_inp = input('enter your transaction (or "end" to quit): ')
    if trans_inp.lower() == 'end':
        transaction(transaction_list)
        break
    trans_type, amount = trans_inp.split()
    amount = int(amount)
    if trans_type.upper() == 'D':
        transaction_list.append(amount)
    elif trans_type.upper() == 'W':
        transaction_list.append(-amount)
