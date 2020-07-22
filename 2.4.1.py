input_gc = input()
count_gc = input_gc.upper().count('G') + input_gc.upper().count('C')
print((count_gc / len(input_gc)) * 100)