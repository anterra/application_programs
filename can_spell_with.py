def can_spell_with(target_word, letter_word):
    valid = True
    new_target_word = target_word.lower()
    new_target_list = list(new_target_word)
    new_letter_word = letter_word.lower()
    new_letter_list = list(new_letter_word)
    for c in new_target_list:
        if c in new_letter_list:
            new_letter_list.pop(new_letter_list.index(c))
            pass
        else:
            valid = False
    return valid


target_word = input("target word ")
letter_word = input("letter word ")
result = can_spell_with(target_word, letter_word)
print(result)