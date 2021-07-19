import sys
import os
import random
from queue import Queue
import threading
import datetime


def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True


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


def uswriter(input, path):  # 自作のアルティメットシンプルcsvライター
    output = ""
    for i in input:
        l = ",".join(map(str, i))
        output += l + "\n"
    try:
        with open(path, mode='w') as f:
            f.write(output)
        return 0
    except:
        return 1


def alpha2dec(input):  # Excel形式の行の名前のうっざいアルファベットを数字に変える魔法の関数（
    input = input.upper()
    cnt = 0
    output = 0
    if isint(input) == True:
        return int(input)
    for i in input[::-1]:
        output += ((ord(i) - 64) * (26 ** cnt))
        cnt += 1
    return output - 1


# 入力csvの二次元配列とデータベースと当選後下がる確率と何列目に希望クラスが入ってるかと何人まで当選できるかと何番目に学年、クラス、番号が入ってるか
def lottery(input, dbpath, per, col, col2, nums, c1, c2, c3, mushi, sec, secred, secwri, lt, wt):
    try:
        people = [[]]
        ll = []
        winners = {}
        writewinners = {}
        numdict = {"5A": nums[0], "5B": nums[1], "5C": nums[2], "5D": nums[3],
                   "6A": nums[4], "6B": nums[5], "6C": nums[6], "6D": nums[7]}
        if mushi == True:
            print("m")
            input = input[1:]
        for i in input:  # 希望クラスごとに振り分ける
            if len(i) > col:
                if i[col] in ll:
                    people[ll.index(i[col])].append(i)
                else:
                    ll.append(i[col])
                    people.append([])
                    people[ll.index(i[col])].append(i)
        for group in people:
            tickets = {}
            cnt = 0
            for person in group:
                try:
                    if os.path.exists(dbpath) == True:
                        with open(dbpath, mode='r') as f:
                            parsedcsv = usparser(f.read())
                    else:
                        parsedcsv = []
                except:
                    print("error when opening file!")
                    pass
                n = 100  # とりあえず100％にしといて
                for p in parsedcsv:
                    if p == []:
                        continue
                    if len(person) < c1 and len(person) < c2 and len(person) < c3:
                        continue
                    if p[0] == person[c1] and p[1] == person[c2] and p[2] == person[c3]:  # もし前にもう当選してたら
                        n = n - per  # n％減らす
                for c in range(0, n):
                    tickets[c+(cnt*n)] = person
                cnt += 1
            if len(group) == 0 or len(group[0]) == 0:
                continue
            for co in range(0, numdict[group[0][col]]):
                t2 = list(tickets.keys())
                if t2 == []:
                    print("there are no more people who has possibility to win")
                    continue
                w = random.choice(t2)
                input.remove(tickets[w])
                if tickets[w][col] not in winners:
                    winners[tickets[w][col]] = []
                temp = winners[tickets[w][col]]
                temp.append(tickets[w])
                winners[tickets[w][col]] = temp
                writewinners[tickets[w][col]] = temp
                wintickets = [k for k, v in tickets.items() if v == tickets[w]]
                for rem in wintickets:
                    tickets.pop(rem)
        if sec == True:  # パラメータによって2回目の抽選をする
            ll = []
            people = [[]]
            for i in input:  # 希望クラスごとに振り分ける
                if len(i) > col2:
                    if i[col2] in ll:
                        people[ll.index(i[col2])].append(i)
                    else:
                        ll.append(i[col2])
                        people.append([])
                        people[ll.index(i[col2])].append(i)
            for group in people:
                tickets = {}
                cnt = 0
                for person in group:
                    try:
                        if os.path.exists(dbpath) == True:
                            with open(dbpath, mode='r') as f:
                                parsedcsv = usparser(f.read())
                        else:
                            parsedcsv = []
                    except:
                        print("error when opening file!")
                        pass
                    n = 100  # とりあえず100％にしといて
                    for p in parsedcsv:
                        if p == []:
                            continue
                        # もし前にもう当選してたら
                        if p[0] == person[c1] and p[1] == person[c2] and p[2] == person[c3] and secred == True:
                            n = n - per  # n％減らす
                    for c in range(0, n):
                        tickets[c+(cnt*n)] = person
                    cnt += 1
                if group == []:
                    continue
                if group[0][col2] not in winners:
                    print("test")
                    winners[group[0][col2]] = [[]]
                print(numdict[group[0][col2]])
                print(group[0][col2] in winners)
                if len(group) == 0:
                    continue
                for co in range(0, numdict[group[0][col2]] - len(winners[group[0][col2]])):
                    print("second lottery")
                    t2 = list(tickets.keys())
                    if t2 == []:
                        print("there are no more people who has possibility to win")
                        continue
                    w = random.choice(t2)
                    if tickets[w][col2] not in winners:
                        winners[tickets[w][col2]] = [[]]
                    temp = winners[tickets[w][col2]]
                    temp.append(tickets[w])
                    winners[tickets[w][col2]] = temp
                    if secwri == True:
                        writewinners[tickets[w][col2]] = temp
                    wintickets = [k for k, v in tickets.items()
                                  if v == tickets[w]]
                    for rem in wintickets:
                        tickets.pop(rem)
        lt.put(winners)
        wt.put(writewinners)
    except:
        pass
    return winners, writewinners


def dbupdate(input, path, c1, c2, c3):  # 入力データとデータのパスと何列目に学年、クラス、番号が入ってるか
    print("updating database")
    if os.path.exists(path) == False:
        print("there are no database file, so we'll make it")
        wincontainer = []
        for i in input.values():
            for val in i:
                v2 = []
                v2 += [val[c1], val[c2], val[c3], 1]
                wincontainer.append(v2)
        return uswriter(wincontainer, path)
    else:
        print("found database file")
        parsedcsv = [[]]
        wincontainer = []
        try:
            with open(path, mode='r') as f:
                parsedcsv = usparser(f.read())
            for i in input.values():
                for val in i:
                    v2 = []
                    chk = False
                    for p in parsedcsv:
                        if p == []:
                            break
                        if val[c1] == p[0] and val[c2] == p[1] and val[c3] == p[2]:
                            chk = True
                            v2 += [val[c1], val[c2], val[c3], int(p[3]) + 1]
                            break
                    if chk == False:
                        v2 += [val[c1], val[c2], val[c3], 1]
                    wincontainer.append(v2)
            for p in parsedcsv:
                chk = False
                if p == []:
                    break
                for i in wincontainer:
                    if p[0] == i[0] and p[1] == i[1] and p[2] == i[2]:
                        chk = True
                        break
                if chk == False:
                    wincontainer.append(p)
            return uswriter(wincontainer, path)
        except:
            return 1


def postprocess(winners, n, men, sw, year):  # テキスト整形
    t = ["5A", "5B", "5C", "5D", "6A", "6B", "6C", "6D"]
    temp = {}
    for i in t:
        temp[i] = winners[i]
    output = ""
    if men != "":
        output = men + "\n"
    for k in temp:
        output += k[0] + "年" + k[1] + "組" + "の劇の当選者：\n"
        cnt = 0
        for val in winners[k]:
            if val == []:
                continue
            output += val[0] + "年" + val[1] + "組" + val[2] + "番"
            cnt += 1
            if sw == True:
                output += " @" + val[0] + val[1] + val[2] + \
                    "KSS" + str(((year - 2004) - int(val[0]))) + "、"
            else:
                output += "、"
            if cnt == n and n != 0:
                output += "\n"
                cnt = 0
        if cnt != 0:
            output += "\n\n"
        else:
            output += "\n"
    return output[: -2]


if __name__ == '__main__':
    f = open("test.csv")
    kh = usparser(f.read())
    f.close()
    lt = [[]]
    wt = [[]]
    lt, wt = lottery(kh, "db.csv", 20, 3, 4, [
        10, 10, 10, 10, 10, 10, 10, 10], 0, 1, 2, False, True, True, True, lt, wt)
    dbupdate(wt, "db.csv", 0, 1, 2)
    today = datetime.date.today()
    print(postprocess(lt, 5, "", False, today.year))
