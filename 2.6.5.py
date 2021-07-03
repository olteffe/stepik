def main():
    array_size = int(input())
    output_matrix = [[0] * array_size for _ in range(array_size)]

    i, j, d = 0, 0, 0
    moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
    for k in range(1, array_size * array_size + 1):
        output_matrix[i][j] = k
        for iterate in range(4):
            new_d = (d + iterate) % 4
            di, dj = moves[new_d]
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < array_size and 0 <= new_j < array_size and output_matrix[new_i][new_j] == 0:
                i, j, d = new_i, new_j, new_d
                break
    for row in output_matrix:
        print(*row)


if __name__ == "__main__":
    main()
