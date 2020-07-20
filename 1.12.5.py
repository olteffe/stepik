first = int(input())
second = int(input())
third = int(input())
if first >= second and first >= third:
    if second > third:
        print(first, third, second, sep="\n")
    elif second < third:
        print(first, second, third, sep="\n")
elif second >= first and second >= third:
    if first > third:
        print(second, third, first, sep="\n")
    elif first < third:
        print(second, first, third, sep="\n")
elif third >= first and third >= second:
    if first > second:
        print(third, second, first, sep="\n")
    elif first < second:
        print(third, first, second, sep="\n")
