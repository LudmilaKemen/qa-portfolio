import sys

# проверка аргументов
if len(sys.argv) != 3:
    print("Usage: python main.py ellipse.txt points.txt")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

try:
    # читаем эллипс
    with open(file1) as f:
        x0, y0 = map(float, f.readline().split())
        a, b = map(float, f.readline().split())

    # читаем точки
    with open(file2) as f:
        points = [list(map(float, line.split())) for line in f]

except Exception as e:
    print("Error reading files:", e)
    sys.exit(1)

# проверка радиусов
if a == 0 or b == 0:
    print("Ellipse radii must be non-zero")
    sys.exit(1)

EPS = 1e-6

# проверяем точки
for x, y in points:
    S = ((x - x0)**2) / (a**2) + ((y - y0)**2) / (b**2)

    if abs(S - 1) < EPS:
        print(0)
    elif S < 1:
        print(1)
    else:
        print(2)
