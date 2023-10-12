# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as inp:
        with open(OUTPUT_FILENAME, 'w') as out:
            j_d = []
            lines = inp.readlines()
            data_name = lines[0].split(',')
            data = lines[1:]
            for d in data:
                d = d.split(',')
                j = {}
                for i in range(len(d)):
                    j[data_name[i].replace('\n', '')] = d[i].replace('\n', '')
                j_d.append(j)
            json.dump(j_d, out, indent=4)
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
