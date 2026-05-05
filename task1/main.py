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


# проверка аргументов
if len(sys.argv) != 5:
    print("Введите 4 аргумента: n1 m1 n2 m2")
    sys.exit(1)

# читаем аргументы
n1, m1, n2, m2 = map(int, sys.argv[1:])

# считаем пути
result1 = get_path(n1, m1)
result2 = get_path(n2, m2)

# вывод результата
print(result1 + result2)
