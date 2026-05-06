import sys

# проверка аргументов
if len(sys.argv) != 2:
    print("Usage: python main.py nums.txt")
    sys.exit(1)

file_path = sys.argv[1]

try:
    # читаем массив
    with open(file_path) as f:
        nums = [int(line.strip()) for line in f if line.strip()]

except Exception as e:
    print("Error reading file:", e)
    sys.exit(1)

# проверка, что есть данные
if not nums:
    print("File is empty")
    sys.exit(1)

# сортировка
nums.sort()

# медиана
n = len(nums)
median = nums[n // 2]

# считаем ходы
moves = sum(abs(x - median) for x in nums)

# проверка ограничения
if moves > 20:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
else:
    print(moves)
