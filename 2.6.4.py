def get_input_matrix() -> list:
    input_matrix = []
    while True:
        input_value = input()
        if input_value == "end":
            break
        input_matrix.append([int(i) for i in input_value.split()])
    return input_matrix


def sum_matrix_elements(input_matrix: list) -> list:
    height = len(input_matrix)
    length = len(input_matrix[0])
    output_matrix = [[0 for j in range(length)] for i in range(height)]
    for i in range(height):
        for j in range(length):
            output_matrix[i][j] = sum((
                input_matrix[(i + 1) % height][j],
                input_matrix[(i - 1) % height][j],
                input_matrix[i][(j + 1) % length],
                input_matrix[i][(j - 1) % length]
            ))
    return output_matrix


def print_matrix(output_matrix: list):
    for element in output_matrix:
        print(*element)


if __name__ == '__main__':
    print_matrix(sum_matrix_elements(get_input_matrix()))
