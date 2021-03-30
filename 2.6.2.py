input_value = int(input())
out = []
for i in range(1, input_value + 1):
    for j in range(1, i + 1):
        out.append(i)
out = out[:input_value]
print(out)
