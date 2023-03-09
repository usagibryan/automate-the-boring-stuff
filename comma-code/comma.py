def comma_code(list):
    if not list:
        return ''
    new_string = ''
    new_string += list[0] + ','
    for word in list[1:-1]:
        new_string += ' ' + word + ','
    new_string += ' and ' + list[-1]
    return new_string

while True:
    user_list = []
    while True:
        item = input("Enter an item to add to the list (or 'done' to finish): ")
        if item == 'done':
            break
        user_list.append(item)

    print(comma_code(user_list))

    again = input("Do you want to create another list? (y/n): ")
    if again.lower() != 'y':
        break
