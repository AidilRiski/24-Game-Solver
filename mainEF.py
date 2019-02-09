#import solver
import tkinter as tk
from tkinter import filedialog

def file_dialog():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename( filetypes = (("Input", ".txt"), ("All files" , "*.*")))
    return file_path

def main():
    print("Welcome to 24 Solver From External File")
    print("Type a number from bellow options:")
    print("Type \"1\" to write filename from keyboard")
    print("Type \"2\" to choose file via File Dialog")
    option = input()
    if (option == '1'):
        input_filename = input("Input filename with format \"FileName.txt\": \n")
        while (input_filename[len(input_filename)-4:] != ".txt" ):
            input_filename = input("Input filename with format \"FileName.txt\": \n")
    if (option == '2'):
        input_filename = file_dialog()

    print("Write output filename")
    output_filename = input("format \"FileName.txt\"\n")
    while (output_filename[len(output_filename)-4:] != ".txt" ):
            output_filename = input("format \"FileName.txt\": \n")
    input_file = open(input_filename,"r")
    output_file = open(output_filename,"w")

if __name__ == "__main__":
    main()