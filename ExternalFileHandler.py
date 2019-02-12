import sys
import solver

#Mengecek argumen yang diterima, jika tidak sesuai akan menampilkan pesan error.
try:

    #Membuka file sesuai nama yang diterima.
    with open(sys.argv[1], 'r') as input_file:
        inputContent = input_file.read()
except IndexError:
    print("Masukan Nama file Input, dan dengan benar\n")

#Mengecek argumen yang diterima, jika tidak sesuai akan menampilkan pesan error.
try:
    inputContent = inputContent.split(' ')

    for (idx, val) in enumerate(inputContent):
        inputContent[idx] = int(val)

    #Melakukan penyelesaian dengan fungsi 24 Solver.
    result = solver.SolveComp(inputContent)

    #Menulis hasil ke file eksternal sesuai nama yang diterima.
    with open(sys.argv[2], 'w') as output_file:
        output_file.write(result)
except IndexError:
    print("Masukan Nama file Output, dan dengan benar\n")

except NameError:
    pass
