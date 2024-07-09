import string
import random

'''
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
'''

all_xters = set(string.ascii_uppercase + string.ascii_lowercase + string.digits)


def generate_uid():
    global all_xters
    #  to select unique characters without repeats:
    uppercase = random.sample(string.ascii_uppercase, 2)
    lowercase = random.sample(string.ascii_lowercase, 2)
    number = random.sample(string.digits, 3)

    # combining the selected xters
    selected_xters = uppercase + number + lowercase

    # Determine how many more xters are needed to reach the minimum length of 10.
    remaining_length = 10 - len(selected_xters)

    # Find available characters by subtracting the used characters from all possible characters

    used_xters = set(selected_xters)
    available_xters = list(all_xters - used_xters)

    # If additional characters are needed, select them from the available xters
    if remaining_length > 0:
        additional_xters = random.sample(available_xters, remaining_length)
    else:
        additional_xters = []

    my_uid = selected_xters + additional_xters
    random.shuffle(my_uid)

    # concatenate elements  into a single string.
    my_uid = ''.join(my_uid)

    return my_uid


def validate_uid(user_id):
    global all_xters
    upcount = sum(1 for x in user_id if x in string.ascii_uppercase)  # produce 1 for each x that meets the condition.
    # lowcount = sum(1 for x in user_id if x in string.ascii_lowercase)
    digitcount = sum(1 for x in user_id if x in string.digits)

    # check length
    if len(user_id) < 10:
        print("Invalid. Password is less than 10 characters!")

    # check at least 2 uppercase letters
        if upcount < 2:
            print("Invalid. Password exceeds 2 uppercase characters!")

    # check at least 3 digits
            if digitcount < 3:
                print("Invalid. Password has less than 3 digits")

    # check for alphanumeric xters only
                if any(x not in all_xters for x in user_id):
                    print("Invalid. Enter alphanumeric text only!")

    # check for uniqueness
                    if len(set(user_id)) != len(user_id):
                        print("Invalid. Enter unique characters!")

    else:
        print("Valid")


user_id = input("Enter id: ")
validate_uid(user_id)
