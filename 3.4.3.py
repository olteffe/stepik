DATASET_FILE_NAME = "dataset_3363_4.txt"
OUTPUT_FILE_NAME = "out_dataset_3363_4.txt"


def get_dataset(f_name: str) -> list:
    data_array = []
    with open(f'{f_name}') as file:
        for line in file:
            data_array.append(line.strip().split(";"))
    return data_array


def write_data(f_name: str, persons_average_value: list, average_value: list):
    with open(f'{f_name}', "w") as file:
        for value in persons_average_value:
            file.write(str(value) + '\n')
        file.write(" ".join(str(item) for item in average_value))


def main():
    dataset = get_dataset(DATASET_FILE_NAME)
    persons = [((int(mathematics) + int(physics) + int(russian)) / 3) for name, mathematics, physics, russian in dataset]
    average_mathematics = sum([int(mathematics) for name, mathematics, physics, russian in dataset]) / len(dataset)
    average_physics = sum([int(physics) for name, mathematics, physics, russian in dataset]) / len(dataset)
    average_russian = sum([int(russian) for name, mathematics, physics, russian in dataset]) / len(dataset)
    average = [average_mathematics, average_physics, average_russian]
    write_data(OUTPUT_FILE_NAME, persons, average)


if __name__ == '__main__':
    main()
