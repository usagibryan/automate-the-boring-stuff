def collatz(number):
    if number % 2 == 0: # number is even
        result = number // 2
        print(f'{number} ÷ 2 = {result}')
        return result
    else: # number % 2 == 1 meaning number is odd
        result = 3 * number + 1
        print(f'3 × {number} + 1 = {result}')
        return result

def get_positive_integer(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError
            return num
        except ValueError:
            print("Invalid input! Please enter a positive integer.")

num = get_positive_integer("Enter a positive integer: ")
while True:
    while num != 1:
        num = collatz(num)

    print("The sequence has reached 1.")
    choice = input("Would you like to enter another number? (y/n): ")
    while choice.lower() not in ['y', 'n']:
        choice = input("Invalid input! Please enter 'y' or 'n': ")
    if choice.lower() == 'n':
        break

    num = get_positive_integer("Enter a positive integer: ")

print("Goodbye!")