import sys
import solver

try:
    with open(sys.argv[1], 'r') as input_file:
        inputContent = input_file.read()

    print(inputContent.split(' '))
    result = solver.Solve(inputContent.split(' '))
    with open(sys.argv[2], 'w') as output_file:
        output_file.write(result)
except IndexError:
    raise "Error! Argumen Input belum dimasukan"
except TypeError:
    pass