def collatz(number):
    if number % 2 == 0: # number is even
        result = number // 2
        print(f'{number} ÷ 2 = {result}')
        return result
    else: # number % 2 == 1 meaning number is odd
        result = 3 * number + 1
        print(f'3 × {number} + 1 = {result}')
        return result


while True:
    try:
        num = float(input("Enter a positive integer: "))
        if num <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input! Please enter a positive integer.")

while num != 1:
    num = collatz(num)
