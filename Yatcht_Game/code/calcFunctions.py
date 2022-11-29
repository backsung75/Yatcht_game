import random
from datetime import datetime

def roll():
    a = random.randint(1, 6) 
    b = random.randint(1, 6)
    c = random.randint(1, 6)
    d = random.randint(1, 6)
    e = random.randint(1, 6)
    return [str(a), str(b), str(c), str(d), str(e)]

def reroll(checkList, diceList):
    for i in range(5):
        if checkList[i].isChecked():
            diceList[i] = str(random.randint(1, 6))
    return diceList

def aces(diceNumList):
    value = 0
    for i in diceNumList:
        if i == "1":
            value += 1
    return str(value)

def twos(diceNumList):
    value = 0
    for i in diceNumList:
        if i == "2":
            value += 2
    return str(value)

def threes(diceNumList):
    value = 0
    for i in diceNumList:
        if i == "3":
            value += 3
    return str(value)

def fours(diceNumList):
    value = 0
    for i in diceNumList:
        if i == "4":
            value += 4
    return str(value)

def fives(diceNumList):
    value = 0
    for i in diceNumList:
        if i == '5':
            value += 5
    return str(value)

def sixes(diceNumList):
    value = 0
    for i in diceNumList:
        if i == '6':
            value += 6
    return str(value)

def choice(diceNumList):
    value = int(diceNumList[0]) + int(diceNumList[1]) + int(diceNumList[2]) + int(diceNumList[3]) + int(diceNumList[4])
    return str(value)

def tcard(diceNumList):
    l_ = [int(i) for i in diceNumList]
    value = 0
    for i in l_:
        if l_.count(i) >= 3:
            value = sum(l_)
            break
    return str(value)

def fcard(diceNumList):
    l_ = [int(i) for i in diceNumList]
    value = 0
    for i in l_:
        if l_.count(i) >= 4:
            value = sum(l_)
            break
    return str(value)

def fhouse(diceNumList):
    l_ = [int(i) for i in diceNumList]
    ll_ = {}
    value = 0
    for i in sorted(l_):
        if i not in ll_:
            ll_[i] = 1
        else:
            ll_[i] += 1
    if len(ll_) == 2:
        for i in ll_.keys():
            if ll_[i] == 3 or ll_[i] == 2:
                value = 25
    
    return str(value)

def s_straight(diceNumList):
    l_ = [int(i) for i in diceNumList]
    l_ = sorted(l_)
    ll_ = []
    lll_ = {}
    value = 0
    for i in range(4):
        ll_.append(l_[i+1] - l_[i])
    for i in sorted(ll_):
        if i not in lll_:
            lll_[i] = 1
        else:
            lll_[i] += 1
    if len(lll_) == 2 or len(lll_) == 1:
        for i in lll_.keys():
            if lll_[i] == 3 or lll_[i] == 4:
                if i == 1:
                    value = 30
    return str(value)

def l_straight(diceNumList):
    l_ = [int(i) for i in diceNumList]
    l_ = sorted(l_)
    ll_ = []
    lll_ = {}
    value = 0
    for i in range(4):
        ll_.append(l_[i+1] - l_[i])
    for i in sorted(ll_):
        if i not in lll_:
            lll_[i] = 1
        else:
            lll_[i] += 1
    if len(lll_) == 1 and (l_[0] != l_[1]):
        value = 40
    return str(value)

def yatcht(diceNumList):
    l_ = [int(i) for i in diceNumList]
    value = 0
    if len(set(l_)) == 1:
        value = 50
    return str(value)

def upsum(a, b, c, d, e, f):
    l_ = [a, b, c, d, e, f]
    c = 0
    for i in l_:
        if i == '':
            l_[c] = 0
            c += 1
        else:
            l_[c] = int(i)
            c += 1
    return int(sum(l_))
def score(a, b, c, d, e, f, g, h, i ,j , k, l, m, n, o):
    l_ = [a, b, c, d, e, f, g, h, i ,j , k, l, m, n, o]
    c = 0
    for i in l_:
        if i == '':
            l_[c] = 0
            c += 1
        else:
            l_[c] = int(i)
            c += 1
    return str(sum(l_))

def save(score):
    if score == 0:
        pass
    else:
        save_t = open('score.txt', 'a', encoding='UTF8')
        line_ = datetime.today().strftime("%Y/%m/%d/%H:%M:%S ") + str(score) + '\n'
        save_t.write(line_)
        save_t.close()
    save_t = open('score.txt', 'r', encoding='UTF8')
    l_ = {}
    while True:
        line__ = save_t.readline()
        if line__ != "":
            a = line__.split(" ")
            l_[a[0]] = int(a[1][:-1])
        else:
            break
    if len(l_) != 0:
        return sorted(l_.items(), key = lambda x : x[1], reverse=True)
    else:
        return ''
    

if __name__ == '__main__':
    a = save(30)
    for i in range(len(a)):
        print(a[i])