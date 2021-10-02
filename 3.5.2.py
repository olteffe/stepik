import sys


def main():
    if len(sys.argv) == 1:
        print("Need 1 or more arguments!")
    elif len(sys.argv) >= 2:
        print(*sys.argv[1:])


if __name__ == '__main__':
    main()
