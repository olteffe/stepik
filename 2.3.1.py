a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c, d + 1): #ось c-d горизонтали
    print('\t', i, sep='\t', end='')
print()
for j in range(a, b + 1): #ось a-b вертикали
    print(j, sep='', end='')
    for i in range(c, d + 1): #внутренний квадарат умножения
        print('\t', i * j, end='', sep='\t')
    print()
