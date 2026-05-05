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

n1, m1, n2, m2 = map(int, sys.argv[1:])

result = get_path(n1, m1) + get_path(n2, m2)

print(result)
