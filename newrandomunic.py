import random

list_unic_random = []
start_number = 0
end_number = 20
random_number = random.randint(start_number,end_number)
print(random_number)
while len(list_unic_random) != (end_number - start_number) or len(list_unic_random) != end_number:
    print(random_number)
    if random_number in list_unic_random:
        random_number = random.randint(start_number, end_number)
    else:
        list_unic_random.append(random_number)
#     if start_number > 1 or start_number > 0:
#         if len(list_unic_random) == (end_number - start_number):
#             break
#     else:
#         if len(list_unic_random) == end_number:
#             break
print(list_unic_random)

