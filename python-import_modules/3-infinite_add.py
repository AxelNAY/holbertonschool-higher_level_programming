#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    number = argv[1:]
    result = sum(int(number) for number in args)
    print(result)
