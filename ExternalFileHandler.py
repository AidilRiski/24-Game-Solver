import sys
import solver

try:
    with open(sys.argv[1], 'r') as input_file:
        inputContent = input_file.read()
except IndexError:
    print("Masukan Nama file Input, dan dengan benar\n")

try:
    inputContent = inputContent.split(' ')

    for (idx, val) in enumerate(inputContent):
        inputContent[idx] = int(val)

    result = solver.SolveComp(inputContent)
    with open(sys.argv[2], 'w') as output_file:
        output_file.write(result)
except IndexError:
    print("Masukan Nama file Output, dan dengan benar\n")

except NameError:
    pass
