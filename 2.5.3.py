input_list = [int(i) for i in input().split()]
input_list.sort()
if len(input_list) > 1:
    for i in range(len(input_list) - 2):
        if input_list[i] == input_list[i + 1] and input_list[i + 1] != input_list[i + 2]:
            print(input_list[i], end=' ')
    if input_list[-1] == input_list[-2]:
        print(input_list[-1])