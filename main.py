import random

import tkinter

import solver

class MainApplication(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.inputNum1 = tkinter.Entry(self)
        self.inputNum1.grid(row=0, column=0)

        self.inputNum2 = tkinter.Entry(self)
        self.inputNum2.grid(row=0, column=1)

        self.inputNum3 = tkinter.Entry(self)
        self.inputNum3.grid(row=0, column=2)

        self.inputNum4 = tkinter.Entry(self)
        self.inputNum4.grid(row=0, column=3)

        self.randomButton = tkinter.Button(self, text='Random', command=lambda: self.randomNumberAction())
        self.randomButton.grid(row=1, column=0, columnspan=2)

        self.solveButton = tkinter.Button(self, text='Solve!', command=lambda: self.solveButtonAction())
        self.solveButton.grid(row=1, column=2, columnspan=2)

        self.result = tkinter.Label(text="")
        self.result.grid(row=2, columnspan=4)

    def solveButtonAction(self):
        self.result['text'] = solver.Solve([int(self.inputNum1.get()), int(self.inputNum2.get()), int(self.inputNum3.get()), int(self.inputNum4.get())])

    def randomNumberAction(self):
        self.inputNum1.delete(0, tkinter.END)
        self.inputNum1.insert(0, str(random.randint(0, 13)))

        self.inputNum2.delete(0, tkinter.END)
        self.inputNum2.insert(0, str(random.randint(0, 13)))

        self.inputNum3.delete(0, tkinter.END)
        self.inputNum3.insert(0, str(random.randint(0, 13)))

        self.inputNum4.delete(0, tkinter.END)
        self.inputNum4.insert(0, str(random.randint(0, 13)))

mainApp = MainApplication()
mainApp.master.title('24 Game Solver')
mainApp.mainloop()