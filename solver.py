def Solve(nums):
    #CARA PAKAI
    #Parameter nums berisi empat buah angka.
    #Tinggal panggil.
    #Fungsi me-return ekspresi dalam string.
    #Greedy Strategy 1:
    expressionNums = []
    nums.sort(reverse = True)
    expression = ''
    operatorList = ['+', '-', '*', '/']
    #Cari dua angka dari HIMPUNAN KANDIDAT yang jika dioperasikan dengan operatorList mendekati 24
    nextTempStep1 = 0
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
                        if (temp1 == 24 and (abs(nums[indexestemp[0]]-nums[indexestemp[1]]) <= 1)):
                            nextTempStep1 = temp1; itemp1 = i; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '+' or operatorList[k] == '-') and abs (temp1-24) <8 and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '*' or operatorList[k] == '/') and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k

    #Masukkan dua angka tersebut dalam himpunan solusi
    expressionNums.append(nums[itemp1]); expressionNums.append(nums[jtemp1])
    expression = ''.join([str(expressionNums[0]),operatorList[ktemp1],str(expressionNums[1])])
    #print(expression)
    expressionv2 = expression #SIMPAN untuk STRATEGI GREEDY 2
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
                nextTempStep2 = temp2; itemp2 = i
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
    for k in range (0 ,4):
        temp3 = eval(''.join([str(nextTempStep2),operatorList[k],str(nums[0])]))
        if (abs(24 - temp3)  < abs (24 - nextTempStep3)):
            nextTempStep3 = temp3;  ktemp3 = k

    #Masukkan angka terakhir dalam himpunan solusi
    expressionNums.append(nums[0])
    expression = expression + operatorList[ktemp3] + str(expressionNums[3])
    #Buang angka terakhir dari himpunan kandidat
    nums.remove(nums[0])

    #Greedy Strategy 2:
    nextTempStep3v2 = 100000; itemp3v2 = 0; ktemp3v2 = 0; selisih = 100000
    nextTempStep3v2 = 100000; itemp3v2 = 0; ktemp3v2 = 0; selisih = 100000
    for k in range (0,4):
        for i in range (2,4) :
            if (i == 2):
                temp1 = eval(''.join([str(expressionNums[i]),operatorList[k],str(expressionNums[3])]))
                print(str(expressionNums[i]) + operatorList[k] + str(expressionNums[3]))
            else:
                temp1 = eval(''.join([str(expressionNums[i]),operatorList[k],str(expressionNums[2])]))
                print(str(expressionNums[i]) + operatorList[k] + str(expressionNums[2]))
            try:
                if (abs(eval(str(expressionv2) + '+' + str(temp1)) - 24) < abs(eval(str(expressionv2) + '+' + str(selisih)) - 24)):
                    tempeval1 = abs(eval(str(expressionv2) + '+' + str(temp1)) - 24)
                    tempeval2 = abs(eval(str(expressionv2) + '+' + str(selisih)) - 24)
                    if (operatorList[k] == "/"):
                        if ((tempeval2 > 2) or (abs(eval(str(expressionv2) + '+' + str(temp1)) - 24) == 0)):
                            selisih = temp1
                            if (i == 2):
                                itemp3v2 = 2
                            else:
                                itemp3v2 = 3
                            ktemp3v2 = k
                    else:
                        selisih = temp1
                        if (i == 2):
                            itemp3v2 = 2
                        else:
                            itemp3v2 = 3
                        ktemp3v2 = k
            except ZeroDivisionError:
                pass

    if (itemp3v2 == 2):
        expressionv2 = expressionv2 + '+' + str(expressionNums[2]) + operatorList[ktemp3v2] + str(expressionNums[3])
    else:
        expressionv2 = expressionv2 + '+' + str(expressionNums[3]) + operatorList[ktemp3v2] + str(expressionNums[2])

    if (abs(24 - eval(expressionv2)) < abs(24 - eval (expression))):
        expressionv2 = expressionv2 + " = " + str(eval(expressionv2))
        print(expressionv2)
        return expressionv2
    else:
        expression = expression + " = " + str(eval(expression))
        return expression


def SolveComp(nums):
    expressionNums = []
    nums.sort(reverse = True)
    expression = ''
    operatorList = ['+', '-', '*', '/']
    #Cari dua angka dari HIMPUNAN KANDIDAT yang jika dioperasikan dengan operatorList mendekati 24
    nextTempStep1 = 0
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
                        if (temp1 == 24 and (abs(nums[indexestemp[0]]-nums[indexestemp[1]]) <= 1)):
                            nextTempStep1 = temp1; itemp1 = i; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '+' or operatorList[k] == '-') and abs (temp1-24) <8 and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '*' or operatorList[k] == '/') and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k

    #Masukkan dua angka tersebut dalam himpunan solusi
    expressionNums.append(nums[itemp1]); expressionNums.append(nums[jtemp1])
    expression = ''.join([str(expressionNums[0]),operatorList[ktemp1],str(expressionNums[1])])
    #print(expression)
    expressionv2 = expression #SIMPAN untuk STRATEGI GREEDY 2
    #Buang dua angka tersebut dari himpunan kandidat
    indexes = [itemp1, jtemp1]
    for i in sorted (indexes, reverse = True):
        del nums[i]
    #https://stackoverflow.com/questions/11303225/how-to-remove-multiple-indexes-from-a-list-at-the-same-time

    #Greedy Strategy 2:
    nextTempStep3v2 = 100000; itemp3v2 = 0; ktemp3v2 = 0; selisih = 100000
    nextTempStep3v2 = 100000; itemp3v2 = 0; ktemp3v2 = 0; selisih = 100000
    for k in range (0,4):
        for i in range (0,2) :
            if (i == 0):
                temp1 = eval(''.join([str(nums[i]),operatorList[k],str(nums[1])]))
            else:
                temp1 = eval(''.join([str(nums[i]),operatorList[k],str(nums[0])]))
            try:
                if (abs(eval(str(expressionv2) + '+' + str(temp1)) - 24) < abs(eval(str(expressionv2) + '+' + str(selisih)) - 24)):
                    tempeval1 = abs(eval(str(expressionv2) + '+' + str(temp1)) - 24)
                    tempeval2 = abs(eval(str(expressionv2) + '+' + str(selisih)) - 24)
                    if (operatorList[k] == "/"):
                        if ((tempeval2 > 2) or (abs(eval(str(expressionv2) + '+' + str(temp1)) - 24) == 0)):
                            selisih = temp1
                            if (i == 0):
                                itemp3v2 = 0
                            else:
                                itemp3v2 = 1
                            ktemp3v2 = k
                    else:
                        selisih = temp1
                        if (i == 0):
                            itemp3v2 = 0
                        else:
                            itemp3v2 = 1
                        ktemp3v2 = k
            except ZeroDivisionError:
                pass

    if (itemp3v2 == 0):
        expressionv2 = expressionv2 + '+' + str(nums[0]) + operatorList[ktemp3v2] + str(nums[1])
    else:
        expressionv2 = expressionv2 + '+' + str(nums[1]) + operatorList[ktemp3v2] + str(nums[0])

    return expressionv2
