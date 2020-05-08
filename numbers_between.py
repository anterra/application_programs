def numbers_between(lower, upper):
    the_list = []
    for i in range(lower, upper+1):
        if i % 2 == 0:
            the_list.append(i)
        elif i % 7 == 0:
            the_list.append(i)
    the_list.sort()
    return the_list


lower = int(input("what is lower num "))
upper = int(input("what is upper num "))
result = numbers_between(lower, upper)
print(result)