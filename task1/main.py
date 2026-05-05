import sys

def get_path(n, m):
    path = []
    current = 1

    while True:
        path.append(str(current))
        current = (current + m - 1) % n

        if current == 0:
            current = n

        if current == 1:
            break

    return ''.join(path)


# проверка количества аргументов
if len(sys.argv) != 5:
    print("Usage: python main.py n1 m1 n2 m2")
    sys.exit(1)

try:
    n1, m1, n2, m2 = map(int, sys.argv[1:])
except ValueError:
    print("All arguments must be integers")
    sys.exit(1)

# проверка значений
if n1 <= 0 or n2 <= 0 or m1 <= 0 or m2 <= 0:
    print("All values must be positive integers")
    sys.exit(1)

# вычисление
result1 = get_path(n1, m1)
result2 = get_path(n2, m2)

# вывод
print(result1 + result2)
