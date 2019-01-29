import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    y = np.sum([x*w])

    if y+b > 0:
        return 1
    else:
        return 0


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3

    y = np.sum([x * w])

    if y + b > 0:
        return 1
    else:
        return 0


def NAND(x1, x2):
    s = AND(x1, x2)

    if s == 1:
        return 0
    else:
        return 1


def XOR(x1, x2):
    nand_gate = NAND(x1, x2)
    or_gate = OR(x1, x2)
    xor = AND(nand_gate, or_gate)

    return xor


if __name__ == "__main__":
    while(True):
        print("0. 종료")
        print("1. AND")
        print("2. OR")
        print("3. NAND")
        print("4. XOR")

        cmd = input()

        if cmd == '0':
            break

        [x1, x2] = input().split(' ')
        x1 = int(x1)
        x2 = int(x2)

        if cmd == '1':
            print('AND  =>' + str(AND(x1, x2)))
        elif cmd == '2':
            print('OR   =>' + str(OR(x1, x2)))
        elif cmd == '3':
            print('NAND =>' + str(NAND(x1, x2)))
        elif cmd == '4':
            print('XOR  =>' + str(XOR(x1, x2)))

