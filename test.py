import sys
import random


def uswriter(input):
    output = ""
    for i in input:
        l = ",".join(map(str, i))
        output += l + "\n"
    return output


def usparser(input):  # 自作のアルティメットシンプルcsvパーサー
    cnt = 0
    val = ""
    output = [[]]
    chk = False
    for i in input:
        if i == ',':
            output[cnt].append(val)
            val = ""
            chk = False
        elif i == '\n':
            output[cnt].append(val)
            val = ""
            output.append([])
            cnt += 1
        else:
            val += i
    return output


f = open("test.csv")
kh = usparser(f.read())
f.close()
print(uswriter(kh))
