n = str(input())
last = n[len(n)-1]
number = int(n)
bad_range = [11, 12, 13, 14, 111, 112, 113, 114, 211, 212, 213, 214, 311, 312, 313, 314,
             411, 412, 413, 414, 511, 512, 513, 514, 611, 612, 613, 614, 711, 712, 713, 714,
             811, 812, 813, 814, 911, 912, 913, 914]
description = "программист"
if last == "2" or last == "3" or last == "4":
    if number not in bad_range:
        print(int(n), description + "а")
    else:
        print(int(n), description + "ов")
elif last == "1":
    if number not in bad_range:
        print(int(n), description)
    else:
        print(int(n), description + "ов")
else:
    print(int(n), description + "ов")
