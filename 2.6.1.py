a = int(input())
summa = a
list_new = []
list_new.append(a)
s = 0
while summa != 0:
    a = int(input())
    summa = summa + a
    list_new.append(a)
for i in list_new:
    s = s + i**2
print(s)