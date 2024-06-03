# On many websites, there are restrictions on usernames and passwords for more security.

# We want to write a function check_validation()
# that receives a number of usernames and passwords
# and checks their validity based on rules
# and finally returns the list of usernames allowed to join. the followings are the rules:

# Username less than 4 characters is too short and is not allowed.
# for the security of users, the use of a password that is less than 6 characters
# or consists of only numbers is also not allowed.
# password must have at least one Uppercase character.



def check_validation(info_dict):
    users = []
    for key, value in info_dict.items():
        if len(key) < 4:
            # print('username must be atleast 4 characters')
            continue
        elif value.islower():
            # print(f'The pass must contain at least one Uppercase char')
            continue
        elif value.isdigit():
            # print('pass can Not be all numbers')
            continue
        elif len(value) < 6:
            # print('pass must be atleast 6 characters')
            continue
        else:
            users.append(key)
    return users

check_validation({
    'mahtab': "1235678",
    'Ali': "He3@lsa",
    'Amir': "kLS45@l$",
    'Sina': 'Pass',
    'Hamid': '1458jE',
})