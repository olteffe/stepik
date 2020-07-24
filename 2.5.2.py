input_str = [int(i) for i in input().split()]
out_list = []
if len(input_str) == 1:
    print(input_str[0])
else:
    for i in range(len(input_str)):
        if i == 0:
            out_list.insert(i, input_str[i + 1] + input_str[len(input_str) - 1])
        elif 0 < i < (len(input_str) - 1):
            out_list.insert(i, input_str[i - 1] + input_str[i + 1])
        elif i == (len(input_str)) - 1:
            out_list.insert(i, input_str[i - 1] + input_str[0])
    for i in out_list:
        print(i, end=' ')