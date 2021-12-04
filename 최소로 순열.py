# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
pr = [random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100),random.randrange(100)]
print(pr)
min_value = pr[0]
for t in range(len(pr)):
    min = t
    for i in range(len(pr)):
        if min_value > pr[i]:
            min_value = pr[i]

