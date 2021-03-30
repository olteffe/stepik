inp_list = list(map(int, input().split()))
inp_value = int(input())
if inp_value not in inp_list:
    print("Отсутствует")
else:
    for i in range(len(inp_list)):
        if inp_value == inp_list[i]:
            print(i, sep=" ", end=" ")
