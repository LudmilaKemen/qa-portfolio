
import json
import sys

# проверка аргументов
if len(sys.argv) != 4:
    print("Usage: python main.py tests.json values.json report.json")
    sys.exit(1)

tests_file = sys.argv[1]
values_file = sys.argv[2]
report_file = sys.argv[3]

try:
    # читаем файлы
    with open(tests_file) as f:
        tests = json.load(f)

    with open(values_file) as f:
        values = json.load(f)

except Exception as e:
    print("Error reading files:", e)
    sys.exit(1)

# создаём словарь id → value
values_dict = {item["id"]: item["value"] for item in values.get("values", [])}

# рекурсивная функция
def fill_values(tests_list):
    for test in tests_list:
        test_id = test.get("id")

        if test_id in values_dict:
            test["value"] = values_dict[test_id]

        if "values" in test:
            fill_values(test["values"])

# запуск
fill_values(tests.get("tests", []))

# запись результата
with open(report_file, "w") as f:
    json.dump(tests, f, indent=2)
