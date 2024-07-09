import string
import random
uppercase = random.sample(string.ascii_uppercase, 2)
lowercase = random.sample(string.ascii_lowercase, 2)
number = random.sample(string.digits, 3)

selected_xters = uppercase + number + lowercase

remaining_length = 10 - len(selected_xters)

all_xters = set(string.ascii_uppercase + string.ascii_lowercase + string.digits)
used_xters = set(selected_xters)
available_xters = list(all_xters - used_xters)

all_xters = ''.join(all_xters)
used_xters = ''.join(used_xters)
available_xters = ''.join(available_xters)

if remaining_length > 0:
    additional_xters = random.sample(available_xters, remaining_length)
else:
    additional_xters = []

my_uid = selected_xters + additional_xters
random.shuffle(my_uid)

my_uid = ''.join(my_uid)

print(all_xters)
print(used_xters)
print(available_xters)

upcount = sum(1 for x in all_xters if x in string.ascii_uppercase)
print(upcount)


for x in my_uid if x in all_xters print("Valid")
