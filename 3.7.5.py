def main():
    with open('dataset_3380_5.txt', 'r') as f:
        l = list()
        for line in f:
            l.append(line.strip().split('\t'))

    avg = dict()
    for i in range(1, 12):
        avg[i] = 0

    for key in avg.keys():
        cnt = 0
        for pup in l:
            if int(pup[0]) == key:
                cnt += 1
                avg[key] += int(pup[2])

        if cnt == 0:
            avg[key] = '-'
        else:
            avg[key] /= cnt

    with open('step05.txt', 'w') as f:
        for i in range(1, 12):
            f.write(str(i) + ' ' + str(avg[i]) + '\n')


if __name__ == "__main__":
    main()
