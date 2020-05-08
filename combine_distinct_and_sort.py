def combine_distinct_and_sort(list1, list2):
    result_list = []
    for entry in list1:
        if entry not in list2:
            result_list.append(entry)
    for entry in list2:
        if entry not in list1:
            result_list.append(entry)
    result_list.sort()
    return result_list


list1 = [3, 3, 5]
list2 = [1, 4, 5]

result = combine_distinct_and_sort(list1, list2)
print(result)