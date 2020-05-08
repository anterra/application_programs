def create_divisors_dict(divisors, lower, upper):
    my_dict = dict()
    for element in divisors:
        my_list = []
        for entry in range(lower, upper+1):
            if entry % element == 0:
                my_list.append(entry)
        my_dict[element] = my_list
    return my_dict


divisors = [1, 2, 5]
lower = 2
upper = 4
result = create_divisors_dict(divisors, lower, upper)
print(result)
