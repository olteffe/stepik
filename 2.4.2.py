input_str = input()
current_ch = input_str[:1]
current_count = 1
result = ""
for i in input_str[1:]:
    if i != current_ch:
        result += (current_ch + str(current_count))
        current_ch = i
        current_count = 1
    else:
        current_count += 1
result += (current_ch + str(current_count))
print(result)