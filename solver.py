def main():
    print("Selamat datang di program Tubes Stima")
    user_input = input()
    nums = user_input.split()
    for (i, num) in enumerate(nums):
        nums[i] = int(num)
    nums.sort()
    expression = ''

    scores = [0, 0, 0, 0]
    currentScore = 0
    print(''.join(['Score ', str(currentScore)]))
    currentNumber = nums[0]
    expressionNums = []
    expressionNums.append(nums[0])
    nums.remove(nums[0])
    print(nums)

    operatorList = [
        '+',
        '-',
        '*',
        '/'
    ]

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
    print(''.join(['Score ', str(currentScore)]))

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
    print(''.join(['Score ', str(currentScore)]))

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
    print(''.join(['Score ', str(currentScore)]))

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

    print(''.join(['Final: ', str(s)]))

main()
