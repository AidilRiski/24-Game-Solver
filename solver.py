def Solve(nums):
#def main():
    #CARA PAKAI
    #Parameter nums berisi empat buah angka.
    #Tinggal panggil.
    #Fungsi me-return ekspresi dalam string.

    #Greedy Strategy 1:
    #https://stackoverflow.com/questions/4663306/get-a-list-of-numbers-as-input-from-the-user
    #nums = [int(i) for i in input().split()]
    expressionNums = []
    nums.sort(reverse = True)
    expression = ''
    operatorList = ['+', '-', '*', '/']
    #Cari dua angka dari HIMPUNAN KANDIDAT yang jika dioperasikan dengan operatorList mendekati 24
    nextTempStep1 = 0 #eval(''.join([str(nums[0]),operatorList[0],str(nums[1])]))
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
                        print(nums[indexestemp[0]]); print(nums[indexestemp[1]])
                        if (temp1 == 24 and (abs(nums[indexestemp[0]]-nums[indexestemp[1]]) <= 1)):
                            nextTempStep1 = temp1; itemp1 = i; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '+' or operatorList[k] == '-') and abs (temp1-24) <8 and temp1 != 24):
                            nextTempStep1 = temp1; itemp1 = i ; jtemp1 = j; ktemp1 = k
                        elif ((operatorList[k] == '*' or operatorList[k] == '/') and temp1 != 24):
                            print(temp1)
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
    print(expression)

    #Greedy Strategy 2:
    print('TESSSSSS')
    nextTempStep3v2 = 100000; itemp3v2 = 0; ktemp3v2 = 0; ktemp2v2 = 0; selisih = 100000
    for k3 in range(0,4):
        for k2 in range (0,4):
            for k in range (0,4) :
                temp1 = eval(''.join([str(expressionNums[2]),operatorList[k],str(expressionNums[3])]))
                if (abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24) < abs(eval(str(nextTempStep3v2) + operatorList[k3] + str(temp1)) - 24)):
                    if (selisih > abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24)):
                        selisih = abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24)
                        nextTempStep3v2 = temp1; itemp3v2 = 2; ktemp3v2 = k; ktemp2v2 = k2

    for k3 in range (0,4):
        for k2 in range (0,4):
            for k in range (0,4) :
                temp1 = eval(''.join([str(expressionNums[2]),operatorList[k],str(expressionNums[3])]))
                if (abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24) < abs(eval(str(nextTempStep3v2) + operatorList[k3] + str(temp1)) - 24)):
                    if (selisih > abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24)):
                        selisih = abs(eval(str(nextTempStep2) + operatorList[k2] + str(temp1)) - 24)
                        nextTempStep3v2 = temp1; itemp3v2 = 2; ktemp3v2 = k; ktemp2v2 = k2

    if (itemp3v2 == 2):
        expressionv2 = expressionv2 + operatorList[ktemp2v2] + '(' + str(expressionNums[2]) + operatorList[ktemp3v2] + str(expressionNums[3]) + ')'
    else:
        expressiov2 = expressionv2 + operatorList[ktemp2v2] + '(' + str(expressionNums[3]) + operatorList[ktemp3v2] + str(expressionNums[2]) + ')'

    print(expressionv2)
    if (abs(24 - eval(expressionv2)) < abs(24 - eval (expression))):
        print(expressionv2)
        return expressionv2
    else:
        print(expression)
        return expression

#main()
'''
def main():
    userInput = input()
    userInput = userInput.split(' ')

    for (idx, val) in enumerate(userInput):
        userInput[idx] = int(val)

    expression = Solve(userInput)
    print((expression))
    print('Hasil : ' + str(eval(expression)))

if __name__ == "__main__":
    main()
'''