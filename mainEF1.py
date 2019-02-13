#Melakukan import untuk library yang diperlukan.
import random
import tkinter
import solver
from PIL import ImageTk, Image

#Dictionary  digunakan untuk pemilihan nama file gambar kartu.
ImageDictionary = {
    '1' : 'A',
    '2' : '2',
    '3' : '3',
    '4' : '4',
    '5' : '5',
    '6' : '6',
    '7' : '7',
    '8' : '8',
    '9' : '9',
    '10' : '10',
    '11' : 'J',
    '12' : 'Q',
    '13' : 'K'
}

def findPictureName(stringText):
    #Fungsi ini menerima sebuah string dan mengembalikan nama
    #file gambar kartu yang sesuai, jika string tidak berada
    #di dalam dictionary gambar sebelumnya, fungsi mengembalikan
    #nilai None (NULL).
    if (stringText in ImageDictionary):
        return ''.join(['./cards/',
            ImageDictionary[stringText],
            {
                1 : 'C',
                2 : 'D',
                3 : 'H',
                4 : 'S'
            }[random.randint(1, 4)],
            '.jpg'
        ])
    else:
        return None

class MainApplication(tkinter.Frame):
    #Kelas utama untuk GUI

    def __init__(self, master=None):
        #Inisialisasi GUI
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.testVar=1
        self.createWidgets()

    def createWidgets(self):
        #Pada fungsi ini dilakukan pembuatan elemen GUI seperti gambar, text box,
        #label, dan tombol.

        self.inputNum1Tracer = tkinter.StringVar()
        self.inputNum1 = tkinter.Entry(self, textvariable=self.inputNum1Tracer)
        self.inputNum1.grid(row=1, column=0, padx=10, pady=10)
        self.updateEntry('1', self.inputNum1)
        self.img1 = ImageTk.PhotoImage(Image.open(findPictureName(self.inputNum1.get())))
        self.entryImage1 = tkinter.Label(self, image=self.img1)
        self.entryImage1.grid(row=0, column=0, padx=10, pady=10)
        self.inputNum1Tracer.trace('w', lambda callback, entryStr, entryImg: self.entryChangeCallback(self.inputNum1.get(), self.entryImage1))

        self.inputNum2Tracer = tkinter.StringVar()
        self.inputNum2 = tkinter.Entry(self, textvariable=self.inputNum2Tracer)
        self.inputNum2.grid(row=1, column=1, padx=10, pady=10)
        self.updateEntry('2', self.inputNum2)
        self.img2 = ImageTk.PhotoImage(Image.open(findPictureName(self.inputNum2.get())))
        self.entryImage2 = tkinter.Label(self, image=self.img2)
        self.entryImage2.grid(row=0, column=1, padx=10, pady=10)
        self.inputNum2Tracer.trace('w', lambda callback, entryStr, entryImg: self.entryChangeCallback(self.inputNum2.get(), self.entryImage2))

        self.inputNum3Tracer = tkinter.StringVar()
        self.inputNum3 = tkinter.Entry(self, textvariable=self.inputNum3Tracer)
        self.inputNum3.grid(row=1, column=2, padx=10, pady=10)
        self.updateEntry('3', self.inputNum3)
        self.img3 = ImageTk.PhotoImage(Image.open(findPictureName(self.inputNum3.get())))
        self.entryImage3 = tkinter.Label(self, image=self.img3)
        self.entryImage3.grid(row=0, column=2, padx=10, pady=10)
        self.inputNum3Tracer.trace('w', lambda callback, entryStr, entryImg: self.entryChangeCallback(self.inputNum3.get(), self.entryImage3))

        self.inputNum4Tracer = tkinter.StringVar()
        self.inputNum4 = tkinter.Entry(self, textvariable=self.inputNum4Tracer)
        self.inputNum4.grid(row=1, column=3, padx=10, pady=10)
        self.updateEntry('4', self.inputNum4)
        self.img4 = ImageTk.PhotoImage(Image.open(findPictureName(self.inputNum4.get())))
        self.entryImage4 = tkinter.Label(self, image=self.img4)
        self.entryImage4.grid(row=0, column=3, padx=10, pady=10)
        self.inputNum4Tracer.trace('w', lambda callback, entryStr, entryImg: self.entryChangeCallback(self.inputNum4.get(), self.entryImage4))

        self.randomButton = tkinter.Button(self, text='Random', command=lambda: self.randomNumberAction())
        self.randomButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.solveButton = tkinter.Button(self, text='Solve!', command=lambda: self.solveButtonAction())
        self.solveButton.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        self.result = tkinter.Label(self, text="")
        self.result.grid(row=3, columnspan=4)

    def solveButtonAction(self):
        #Fungsi ini akan dipanggil ketika tombol 'Solve' ditekan.
        #Pada fungsi ini akan mengubah label agar menampilkan hasil dari keempat angka yang diterima.
        self.result['text'] = solver.Solve([int(self.inputNum1.get()), int(self.inputNum2.get()), int(self.inputNum3.get()), int(self.inputNum4.get())])

    def entryChangeCallback(self, newEntry, labelObject):
        #Fungsi ini dipanggil ketika terjadi perubahan pada entry text box.
        #Fungsi ini mengubah gambar kartu menjadi yang sesuai, jika isi tidak sesuai dengan kartu
        #manapun, maka gambar tidak diubah.
        print(newEntry)
        newEntryImagePath = findPictureName(newEntry)
        self.testVar += 1
        
        if (not newEntryImagePath == None):
            print(newEntryImagePath)
            newImageObj = ImageTk.PhotoImage(Image.open(newEntryImagePath))
            self.updateImage(newImageObj, labelObject)

    def updateImage(self, newImageObject, labelObject):
        #Fungsi ini melakukan perubahan gambar pada labelObject menjadi newImageObject.
        labelObject.configure(image=newImageObject)
        labelObject.photo = newImageObject

    def updateEntry(self, newEntry, entryObject, imageLabel = None):
        #Fungsi ini melakukan perubahan isi pada entry text box entryObject agar menjadi newEntry.
        #Jika disertakan imageLabel, maka gambar pada imageLabel akan diubah melalui fungsi updateImage().
        entryObject.delete(0, tkinter.END)
        entryObject.insert(0, newEntry)
        
        if (not imageLabel == None):
            imageObj = ImageTk.PhotoImage(Image.open(findPictureName(newEntry)))
            self.updateImage(imageObj, imageLabel)

    def randomNumberAction(self):
        #Fungsi ini dipanggil ketika tombol 'Random' ditekan.
        self.updateEntry(str(random.randint(1, 13)), self.inputNum1, self.entryImage1)
        self.updateEntry(str(random.randint(1, 13)), self.inputNum2, self.entryImage2)
        self.updateEntry(str(random.randint(1, 13)), self.inputNum3, self.entryImage3)
        self.updateEntry(str(random.randint(1, 13)), self.inputNum4, self.entryImage4)
        self.solveButtonAction()

mainApp = MainApplication()
mainApp.master.title('24 Game Solver')
mainApp.mainloop()
