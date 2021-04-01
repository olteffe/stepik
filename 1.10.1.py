A = int(input())  # рекомендуется спать хотя бы
B = int(input())  # не стоит спать более
H = int(input())  # спит сейчас

if A <= H <= B:
    print("Это нормально")
elif H > B:
    print("Пересып")
else:
    print("Недосып")
