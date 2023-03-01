spam = ['apples', 'bananas', 'tofu', 'cats']

def comma_code(list):
    if not list:
        return ''
    new_string = ''
    new_string += list[0] + ','
    for word in list[1:-1]:
        new_string += ' ' + word + ','
    new_string += ' and ' + list[-1]
    return (new_string)

print(comma_code(spam))