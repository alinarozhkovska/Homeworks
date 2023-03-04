my_list = [50, 120, 80, 200, 30, 150]

for value in my_list:
    if value > 100:
        print(value)

########################################################

my_list = [50, 120, 80, 200, 30, 150]
my_results = []

for value in my_list:
    if value > 100:
        my_results.append(value)

print(my_results)

########################################################

my_list = [5, 10]

if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])

print(my_list)
