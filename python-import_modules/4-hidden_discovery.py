#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    modules = dir(hidden_4)
    for module in modules:
        if module[0] != '_':
            print(module)
