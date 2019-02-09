def main():
    expressionNums = []
    #Greedy Strategy 1:
    print("Masukkan empat angka yang Anda mau!")
    nums = [int(msk) for msk in input().split()]
    #https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
    nums.sort(reverse = True)
    expression = ''
    operatorList = ['+', '-', '*', '/']
    #Cari dua angka dari HIMPUNAN KANDIDAT yang jika dioperasikan dengan operatorList mendekati 24
    nextTempStep1 = eval(''.join([str(nums[0]),operatorList[0],str(nums[1])]))
    itemp1 = 0; jtemp1 = 1; ktemp1 = 0
    for i in range (0,4):
        for j in range (0,4) :
            if (i != j):
                for k in range (0,4) :
                    temp1 = eval(''.join([str(nums[i]),operatorList[k],str(nums[j])]))
                    if ((abs(temp1 - 24) < abs(nextTempStep1 - 24))):
                        indexestemp = [0,1,2,3]
                        #Cek dua angka yang lain
                        if (j > i):
                            del indexestemp[j]; del indexestemp[i]
                        else:
                            del indexestemp[i]; del indexestemp[j]
                        #Fungsi Seleksi, yaitu yang paling dekat dengan 24

                        if (temp1 == 24 and nums[indexestemp[0]] == nums[indexestemp[1]] or (abs(nums[indexestemp[0]]-nums[indexestemp[1]]) == 1)):
                            nextTempStep1 = temp1; itemp1 = i; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '+' or operatorList[k] == '-') and abs (temp1-24) <6 and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k
                        elif (operatorList[k] == '*' or operatorList[k] == '/' and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k

    #Masukkan dua angka tersebut dalam himpunan solusi
    expressionNums.append(nums[itemp1]); expressionNums.append(nums[jtemp1])
    expression = ''.join([str(expressionNums[0]),operatorList[ktemp1],str(expressionNums[1])])
    print(expression)

    #Buang dua angka tersebut dari himpunan kandidat
    indexes = [itemp1, jtemp1]
    for i in sorted (indexes, reverse = True):
        del nums[i]
    #https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time

    #Cari angka berikutnya yang jika dioperasikan dengan operator dalam operatorList tetap mendekati 24
    nextTempStep2 = eval(''.join([str(nextTempStep1),'+',str(nums[0])])) #Awal
    itemp2 = 0; ktemp2 = 0
    for i in range (0,2):
        for k in range (0,4):
            temp2 = eval(''.join([str(nextTempStep1),operatorList[k],str(nums[i])]))
            if (abs(24 - temp2)  < abs (24 - nextTempStep2) and temp2 != 24):
                nextTempStep2 = temp2; itemp2 = i; ktemp2 = k
            elif (abs(24 - temp2) < abs (24 - nextTempStep2) and (temp2 == 24) and (nums[1-i] == 1)):
                nextTempStep2 = temp2; itemp2 = i;
                ktemp2 = k

    #Masukkan angka tersebut dalam himpunan solusi
    expressionNums.append(nums[itemp2])
    if ((ktemp2 == 2 or ktemp2 == 3)): # * atau /
        if (ktemp1 == 0 or ktemp1 == 1):
            expression = '(' + expression + ')' + (operatorList[ktemp2] + str(expressionNums[2]))
        else:
            expression = expression + (operatorList[ktemp2] + str(expressionNums[2]))
    else:
        expression = expression + (operatorList[ktemp2] + str(expressionNums[2]))
    #Buang angka tersebut dari himpunan kandidat
    nums.remove(nums[itemp2])
    #Cari angka berikutnya (terakhir) yang jika dioperasikan dengan operator dalam operatorList tetap mendekati 24
    nextTempStep3 = eval(''.join([str(nextTempStep2),'+',str(nums[0])])); ktemp3 = 0 #Awal
    for k in range (0,4):
        temp3 = eval(''.join([str(nextTempStep2),operatorList[k],str(nums[0])]))
        if (abs(24 - temp3)  < abs (24 - nextTempStep3)):
            nextTempStep3 = temp3;  ktemp3 = k

    #Masukkan angka terakhir dalam himpunan solusi
    expressionNums.append(nums[0])
    expression = expression + operatorList[ktemp3] + str(expressionNums[3])
    #Buang angka terakhir dari himpunan kandidat
    nums.remove(nums[0])

    print((expression))
    print('Hasil : ' + str(eval(expression)))


    '''

    scores = [0, 0, 0, 0]
    currentScore = 0
    print(''.join(['Score: ', str(currentScore)]))
    currentNumber = nums[0] #Ambil angka terbesar

    expressionNums.append(nums[0])
    nums.remove(nums[0])
    print(nums)



    scores = [
        currentScore + 4 - (abs(24 - (currentNumber + nums[2]))),
        currentScore + 3 - (abs(24 - (currentNumber - nums[0]))),
        currentScore + 3 - (abs(24 - (currentNumber * nums[2]))),
        currentScore + 2 - (abs(24 - (currentNumber - nums[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    currentScore = scores[id]
    print(''.join(['Score', str(currentScore)]))

    chosen = 0

    if (id == 0 or id == 2):
        chosen = nums[2]
    else:
        chosen = nums[0]

    nums.remove(chosen)
    print(nums)
    expressionNums.append(chosen)

    if (id == 0 or id == 1):
        expression = ''.join([expression, '(', str(expressionNums[0]), operatorList[id], str(expressionNums[1]), ')'])
    else:
        expression = ''.join([expression, str(expressionNums[0]), operatorList[id], str(expressionNums[1])])

    currentNumber = eval(expression)

    print(expression)
    print(currentNumber)

    scores = [
        currentScore + 4 - (abs(24 - (currentNumber + nums[1]))),
        currentScore + 3 - (abs(24 - (currentNumber - nums[0]))),
        currentScore + 3 - (abs(24 - (currentNumber * nums[1]))),
        currentScore + 2 - (abs(24 - (currentNumber - nums[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    currentScore = scores[id]
    print(''.join(['Score', str(currentScore)]))

    chosen = 0

    if (id == 0 or id == 2):
        chosen = nums[1]
    else:
        chosen = nums[0]

    nums.remove(chosen)
    print(nums)
    expressionNums.append(chosen)

    if (id == 0 or id == 1):
        expression = ''.join(['(', expression, operatorList[id], str(expressionNums[2]), ')'])
    else:
        expression = ''.join([expression, operatorList[id], str(expressionNums[2])])
    currentNumber = eval(expression)

    print(expression)
    print(currentNumber)

    scores = [
        currentScore + 4 - (abs(24 - (currentNumber + nums[0]))),
        currentScore + 3 - (abs(24 - (currentNumber - nums[0]))),
        currentScore + 3 - (abs(24 - (currentNumber * nums[0]))),
        currentScore + 2 - (abs(24 - (currentNumber - nums[0]))),
    ]

    print(scores)

    id = 0
    max = scores[id]

    for (i, score) in enumerate(scores):
        if (max < score):
            id = i
            max = scores[id]

    currentScore = scores[id]
    print(''.join(['Score', str(currentScore)]))

    chosen = nums[0]

    nums.remove(chosen)
    print(nums)
    expressionNums.append(chosen)

    expression = ''.join([expression, operatorList[id], str(expressionNums[3])])
    currentNumber = eval(expression)

    print(expression)
    print(currentNumber)

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

    s -= abs(currentNumber - 24)

    print(''.join(['Final', str(s)]))

    '''
main()
