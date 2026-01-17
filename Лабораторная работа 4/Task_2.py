# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode="r", encoding="utf-8") as cvs_file:
        reader = csv.DictReader(cvs_file)


        for row in reader:
             data.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4


    with open(OUTPUT_FILENAME, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
