def string_reverse_A(input_str):
    reversed_str = input_str[::-1]
    new_list= []
    for character in reversed_str:
        new_list.append(character)
        new_list.append("A")
    empty_str = ""
    new_str = empty_str.join(new_list)
    return new_str


input_str = input("what is your string? ")
result = string_reverse_A(input_str)
print(result)