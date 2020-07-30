input_list = input().lower().split()
output_dict = {}.fromkeys(input_list, 0)
for i in input_list:
    output_dict[i] += 1
for key in output_dict:
    print(key, output_dict[key])

