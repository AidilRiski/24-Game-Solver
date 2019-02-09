#import solver
import sys

with open(sys.argv[1], 'r') as input_file:
    inputContent = input_file.read()

result = inputContent #Solver(inputContent)
with open(sys.argv[2], 'w') as output_file:
    output_file.write(result)