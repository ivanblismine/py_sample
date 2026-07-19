def calculate(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b
    raise ValueError('Unsupported operator')


def main():
    print('Simple Calculator')
    print('Enter expressions like 3 + 4 or type q to quit')

    while True:
        text = input('> ').strip()
        if text.lower() in ('q', 'quit', 'exit'):
            print('Goodbye!')
            break

        parts = text.split()
        if len(parts) != 3:
            print('Invalid format. Use: number operator number')
            continue

        try:
            a = float(parts[0])
            op = parts[1]
            b = float(parts[2])
            result = calculate(a, b, op)
            if result.is_integer():
                result = int(result)
            print('Result:', result)
        except ValueError as err:
            print('Error:', err)
        except Exception:
            print('Error: invalid input')


if __name__ == '__main__':
    main()
