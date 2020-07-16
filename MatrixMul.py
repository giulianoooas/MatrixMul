import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Matrix Multiplication")

fr1 = tk.LabelFrame(root,text = "Matrix 1")
fr1.grid(row = 0, column = 0)

matrix_first = None
matrix_second = None

def ver(h):
    if set(h) <= {'0','1','2','3','4','5','6','7','8','9'} and set(h):
        return True
    return False

class mat:
    def __init__(self, nr1,nr2,loc):
        self.__columns = nr2
        self.__rows = nr1
        self.__mat = [[tk.Entry(loc) for i in range(self.__columns)] for i in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__mat[i][j].grid(row = i,column = j)

    def matrix(self):
        g = [[self.__mat[i][j].get() for j in range(self.__columns)] for i in range(self.__rows)]
        return g

    def rows(self):
        return self.__rows

    def columns(self):
        return self.__columns


def generate1():
    global rows1, columns1, matrix_first
    val1, val2 = rows1.get(),columns1.get()
    if ver(val1) and ver(val2):
        if int(val1) != 0 and int(val2) != 0:
            rows1.configure(state=tk.DISABLED)
            columns1.configure(state=tk.DISABLED)
            val1 = min(int(val1),5)
            val2 = min(int(val2),5)
            matrix_first = mat(val1,val2,Mat1)

def generate2():
    global rows2, columns2, matrix_second
    val1, val2 = rows2.get(),columns2.get()
    if ver(val1) and ver(val2):
        if int(val1) != 0 and int(val2) != 0:
            rows2.configure(state=tk.DISABLED)
            columns2.configure(state=tk.DISABLED)
            val1 = min(int(val1),5)
            val2 = min(int(val2),5)
            matrix_second = mat(val1,val2,Mat2)

def fd1():
    global Mat1
    rows1.configure(state="normal")
    columns1.configure(state="normal")
    Mat1.destroy()
    Mat1 = tk.LabelFrame(fr1, borderwidth=1, text="Matrix Show")
    Mat1.grid(row=2, column=1)

def fd2():
    global Mat2
    rows2.configure(state="normal")
    columns2.configure(state="normal")
    Mat2.destroy()
    Mat2 = tk.LabelFrame(fr2, borderwidth=1, text="Matrix Show")
    Mat2.grid(row=2, column=1)

rows1= tk.Entry(fr1, borderwidth = 1)
rows1.grid(row = 0, column = 0)
columns1 = tk.Entry(fr1, borderwidth = 1)
columns1.grid(row = 0, column = 2)
d1 = tk.Button(fr1, text = "Destory", command = fd1)
d1.grid(row = 0, column = 1)
b1 = tk.Button(fr1, text = "Generate",command = generate1)
b1.grid(row = 1, column = 1)
Mat1 = tk.LabelFrame(fr1, borderwidth = 1, text = "Matrix Show")
Mat1.grid(row=2,column = 1)

fr2 = tk.LabelFrame(root, text = "Matrix 2")
fr2.grid(row = 0, column = 2)

rows2= tk.Entry(fr2, borderwidth = 1)
rows2.grid(row = 0, column = 0)
columns2 = tk.Entry(fr2, borderwidth = 1)
columns2.grid(row = 0, column = 2)
d2 = tk.Button(fr2, text = "Destory", command = fd2)
d2.grid(row = 0, column = 1)
b2 = tk.Button(fr2, text = "Generate", command = generate2)
b2.grid(row = 1, column = 1)
Mat2 = tk.LabelFrame(fr2, borderwidth = 1, text = "Matrix Show")
Mat2.grid(row=2,column = 1)

class afisare:
    def __init__(self, linii,coloane,matrice):
        self.__columns = coloane
        self.__rows = linii
        self.__mat = [[tk.Entry(res) for i in range(self.__columns)] for i in range(self.__rows)]
        for i in range(self.__rows):
            for j in range(self.__columns):
                self.__mat[i][j].insert(0,str(matrice[i][j]))
                self.__mat[i][j].grid(row=i, column=j)
                self.__mat[i][j].configure(state = tk.DISABLED)

def f():
    global res
    if matrix_first and matrix_second:
        if matrix_first.columns() == matrix_second.rows():
            ok1 = True
            ok2 = True
            a = matrix_first.matrix()
            b = matrix_second.matrix()
            for i in range(matrix_first.rows()):
                for j in range(matrix_second.columns()):
                    if not ver(a[i][j]):
                        ok1 = False
            for i in range(matrix_second.rows()):
                for j in range(matrix_second.columns()):
                    if not ver(b[i][j]):
                        ok2 = False
            if ok1 and ok2:
                res.destroy()
                res = tk.LabelFrame(root, text="Matricea rezultata")
                res.grid(row=2, column=1)
                afis.configure(text = "")
                a = [[int(a[i][j]) for j in range(matrix_first.columns())] for i in range(matrix_first.rows())]
                b = [[int(b[i][j]) for j in range(matrix_second.columns())] for i in range(matrix_second.rows())]
                a = np.array(a)
                b = np.array(b)
                g = np.matmul(a,b)
                g = afisare(matrix_first.rows(), matrix_second.columns(),g)

            else:
                res.destroy()
                res = tk.LabelFrame(root, text="Matricea rezultata")
                res.grid(row=2, column=1)
                afis.configure(text = "Imposibil")
        else:
            res.destroy()
            res = tk.LabelFrame(root, text="Matricea rezultata")
            res.grid(row=2, column=1)
            afis.configure(text = "Imposibil")

    else:
        res.destroy()
        res = tk.LabelFrame(root, text="Matricea rezultata")
        res.grid(row=2, column=1)
        afis.configure(text = "Imposibil")

b = tk.Button(root, text = " Calcul ", command = f)
b.grid(row = 1, column = 1)

res = tk.LabelFrame(root, text = "Matricea rezultata")
res.grid(row = 2,column = 1)

afis = tk.Label(root, text = "")
afis.grid(row = 3, column = 1)

def delete():
    global res,afis
    res.destroy()
    res = tk.LabelFrame(root, text="Matricea rezultata")
    res.grid(row=2, column=1)
    afis.configure(text = "")

clear = tk.Button(root, text = "Clear", command = delete)
clear.grid(row = 0, column = 1)

root.mainloop()