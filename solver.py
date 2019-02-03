def main():
    print("Masukkan empat angka yang Anda mau!")
    num = [int(msk) for msk in input().split()]
    #https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
    num.sort(reverse = True)
    expression = ''
    scores = [0, 0, 0, 0]
    curScore = 0
    print(''.join(['Score ', str(curScore)]))
    curNum = num[0]
    exprNum = []

    solusi = 24 - num[0] #Pilih angka terbesar
    #Initial : Jumlahkan semua angka
    if (num[1] + num[2] + num[3] == solusi):
        exprNum.append(num[0]); exprNum.append(num[1]); exprNum.append(num[2]); exprNum.append(num[3])
        idx = 1
        while (idx <= 4) :
            num.remove(num[0])
            idx = idx + 1
        print(str(exprNum[0]),'+',str(exprNum[1]),'+',str(exprNum[2]),'+',str(exprNum[3]))
    else:
        #Kurangkan dengan angka terkecil atau dua angka terkecil
        solusi = solusi - num[1]
        if (abs(num[2] - num[3]) == solusi):
            exprNum.append(num[0]); exprNum.append(num[1]); exprNum.append(num[2]); exprNum.append(num[3])
            idx = 1
            while (idx <= 4) :
                num.remove(num[0])
                idx = idx + 1

            if (num[2] >= num[3]):
                print(str(exprNum[0]),'+',str(exprNum[1]),'+',str(exprNum[2]),'-',str(exprNum[3]))
            else:
                print(str(exprNum[0]),'+',str(exprNum[1]),'+',str(exprNum[3]),'-',str(exprNum[2]))
        else:
            #Cari faktor dari 24
            solusi = 24
            idx = 0; Check = False
            while (idx < 4) and (Check == False):
                if (solusi % num[idx] == 0):
                    exprNum.append(num[idx]); num.remove(num[idx])
                    #print(str(num[0]),' ',str(num[1]),' ',str(num[2]))
                    #print(str(solusi))
                    if ((num[0] + num[1] + num[2]) * exprNum[0] == solusi):
                        #print("Tes")
                        Check = True
                        exprNum.append(num[0]); exprNum.append(num[1]); exprNum.append(num[2])
                        i = 1
                        while (i <= 3) :
                            num.remove(num[0])
                            i = i + 1
                        print(str(exprNum[0]),'*','(',str(exprNum[1]),'+',str(exprNum[2]),'+',str(exprNum[3]),')')
                    else:
                        print("Tes")
                        exprNum.remove(exprNum[0])
                        num.append(num[idx])
                        num.sort(reverse = True)
                        idx = idx + 1
                else:
                    idx = idx+1

    '''
    print(num)

    operatorList = ['+','-', '*','/']

    scores = [
        curScore + 4 - (abs(24 - (curNum + num[2]))),
        curScore + 3 - (abs(24 - (curNum - num[0]))),
        curScore + 3 - (abs(24 - (curNum * num[2]))),
        curScore + 2 - (abs(24 - (curNum - num[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    curScore = scores[id]
    print(''.join(['Score ', str(curScore)]))

    chosen = 0

    if (id == 0 or id == 2):
        chosen = num[2]
    else:
        chosen = num[0]

    num.remove(chosen)
    print(num)
    exprNum.append(chosen)

    if (id == 0 or id == 1):
        expression = ''.join([expression, '(', str(exprNum[0]), operatorList[id], str(exprNum[1]), ')'])
    else:
        expression = ''.join([expression, str(exprNum[0]), operatorList[id], str(exprNum[1])])

    curNum = eval(expression)

    print(expression)
    print(curNum)

    scores = [
        curScore + 4 - (abs(24 - (curNum + num[1]))),
        curScore + 3 - (abs(24 - (curNum - num[0]))),
        curScore + 3 - (abs(24 - (curNum * num[1]))),
        curScore + 2 - (abs(24 - (curNum - num[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    curScore = scores[id]
    print(''.join(['Score ', str(curScore)]))

    chosen = 0

    if (id == 0 or id == 2):
        chosen = num[1]
    else:
        chosen = num[0]

    num.remove(chosen)
    print(num)
    exprNum.append(chosen)

    if (id == 0 or id == 1):
        expression = ''.join(['(', expression, operatorList[id], str(exprNum[2]), ')'])
    else:
        expression = ''.join([expression, operatorList[id], str(exprNum[2])])
    curNum = eval(expression)

    print(expression)
    print(curNum)

    scores = [
        curScore + 4 - (abs(24 - (curNum + num[0]))),
        curScore + 3 - (abs(24 - (curNum - num[0]))),
        curScore + 3 - (abs(24 - (curNum * num[0]))),
        curScore + 2 - (abs(24 - (curNum - num[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    curScore = scores[id]
    print(''.join(['Score ', str(curScore)]))

    chosen = num[0]

    num.remove(chosen)
    print(num)
    exprNum.append(chosen)

    expression = ''.join([expression, operatorList[id], str(exprNum[3])])
    curNum = eval(expression)

    print(expression)
    print(curNum)

    s = 0

    for c in expression:
        if (c == '('):
            s -= 1
        elif (c == '+'):
            s += 5
        elif (c == '-'):
            s += 4
        elif (c == '*'):
            s += 3
        elif (c == '/'):
            s += 2

    s -= abs(curNum - 24)

    print(''.join(['Final: ', str(s)]))
    '''
main()
