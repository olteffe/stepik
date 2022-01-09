steps = {"север": 0, "юг": 0, "запад": 0, "восток": 0}

for _ in range(int(input())):
    step = input().split()
    steps[step[0]] += int(step[1])

print(steps["восток"] - steps["запад"], steps["север"] - steps["юг"], end=" ")
