def main():
    d = [input().lower() for _ in range(int(input()))]
    e = set()
    for i in range(int(input())):
        [e.add(j) for j in input().lower().split() if j not in d]
    print(*e, sep="\n")


if __name__ == "__main__":
    main()
