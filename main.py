from tkinter import *
import stats
from stats import *

count = 0
count2 = 0
matrix_B = []
matrix_I = []
answer_dict = {}
matrix_dict = []
occ = 0
ok90 = 0
ok180 = 0
ok270 = 0

class VentanaPlay():

    #init function
    def __init__(self):
        self.all_buttons = []
        self.all_buttons2 = []
        self.matrice = []
        self.matrice2 = []
        self.answer_list = []
        self.answer_list2 = []
        self.ventana = Tk()
        self.ventana.title('Pattern Matching GUI')
        self.ventana.geometry("1200x800")
        self.ventana.frame = Frame()
        self.ventana.frame.pack()
        self.txt1 = Entry(self.ventana)
        self.txt1.pack()
        btn = Button(self.ventana, text="Set Rows", bg="yellow",command=self.setRows)
        btn.pack()
        self.txt2 = Entry(self.ventana)
        self.txt2.pack()
        btn2 = Button(self.ventana,text="Set Cols",bg="yellow",command=self.setCols)
        btn2.pack()
        btn3 = Button(self.ventana, text="Create Game Matrix",bg="green", command=self.creaMatriz)
        btn3.pack()
        btnmatrix2 = Button(self.ventana, text="Create Mini Pattern", bg="yellow", command=self.creaMini)
        btnmatrix2.pack(padx=20, pady=30)
        btn4 = Button(self.ventana, text="Exit Game",bg="blue", command=self.exitGame)
        btn4.pack()
        btn5 = Button(self.ventana, text="Info", command=self.about)
        btn5.pack()
        btnCheckPattern = Button(bg="blue", text="Find Pattern", command=self.FindPattern)
        btnCheckPattern.place(x=100, y=350)

    def setRows(self):
            print(self.txt1.get())
            self.rows = int(self.txt1.get())

    def setCols(self):
            print(self.txt2.get())
            self.cols = int(self.txt2.get())

    # funzioni per la minimatrice
    def setRowsMini(self):
            print("Row minimatrix",self.txt3.get())
            self.rows2 = int(self.txt3.get())
            if(self.rows2 == '' or self.rows2 <= 0):
                messagebox.showinfo("Error Rows", "Error in typing rows number!")
    def setColsMini(self):
            print("Cols minimatrix",self.txt4.get())
            self.cols2 = int(self.txt4.get())
            if (self.cols2 == '' or self.cols2 <= 0):
                messagebox.showinfo("Error Columns", "Error in typing cols number!")

    def generateMini(self):
        global rows, cols
        rows2 = int(self.txt3.get())
        cols2 = int(self.txt4.get())
        print("Rows : ", rows2, " - COLS : ", cols2)
        if(rows2 <= self.rows or cols2 <= self.cols):
            self.matrice2 = [[0 for _ in range(cols2)] for _ in range(rows2)]
            self.mmatrice = [[0 for _ in range(rows2 + 1)] for _ in range(cols2 + 1)]
            for y in range(rows2):
                btns_row = []
                for x in range(cols2):
                    boton = Button(self.ventana.frame, text=0, fg="blue", width=2, height=2,
                                   command=lambda a=x, b=y: self.onButtonMiniPressed(a, b))
                    boton.grid(row=5+y, column=5+x)
                    btns_row.append(boton)
                    self.matrice2[y][x] = boton["text"]
                self.all_buttons2.append(btns_row)

            print("Matrice2 : ", self.matrice2)
        else:
             messagebox.showinfo("Pattern Matching Exception!", "Number of Rows/Coloumns too big than #of rows and cols of the larger matrix!")
             rows = 0
             cols = 0

    def onButtonMiniPressed(self, i, j):
        global count2, matrice2, answer_list2
        if self.all_buttons2[j][i]['text'] == 0 and count2 < 100:
                self.all_buttons2[j][i]['text'] = 1
                count2 += 1
                # prima dell'incremento stampo la lista answer_list
                print("count2 : ", count2)
                print("M_text : ",self.all_buttons2[j][i]["text"])
                self.matrice2[j][i] = self.all_buttons2[j][i]["text"]
                self.answer_list2.append(self.all_buttons2[j][i]["text"])
                print(self.answer_list2)
        elif count2 >= 100:
                # reimposto valori di default
                count2 = 0
                messagebox.showinfo("Pattern Matching", "Hai cliccato su una casella piena!")

    def about(self):
        messagebox.showinfo("Info Window","App Name: Pattern Matching\nAuthors : \n Lobascio Giuseppe Pio\n La Fauci Daniele\n Fouah Manal\n Course: IUM-TWEB\n Year:2021/2022")
    def run(self):
        self.ventana.mainloop()

    def exitGame(self):
        self.ventana.destroy()

    def creaMini(self):
        self.root = Tk()
        self.root.title("Mini Matrix Frame")
        self.root.geometry("500x500")
        self.root.frame2 = Frame()
        self.root.frame2.pack()
        self.txt3 = Entry(self.root)
        self.txt3.pack()
        self.btnrow = Button(self.root, text="Set Rows", bg="yellow", command=self.setRowsMini)
        self.btnrow.pack()
        self.txt4 = Entry(self.root)
        self.txt4.pack()
        self.btncol = Button(self.root, text="Set Cols", bg="yellow", command=self.setColsMini)
        self.btncol.pack()
        self.btncrea = Button(self.root, text="Generate mini Matrix", command=self.generateMini)
        self.btncrea.pack()
        self.btnexit = Button(self.root, text="Exit", command=self.root.destroy)
        self.btnexit.pack()

    def creaMatriz(self):
        global rows, cols
        rows = int(self.txt1.get())
        cols = int(self.txt2.get())
        print("Rows : ", rows, " - COLS : ", cols)
        self.matrice3 = [[0 for _ in range(cols)] for _ in range(rows)]
        self.matrice = [[0 for _ in range(rows+1)] for _ in range(cols+1)]
        for y in range(rows):
            buttons_row = []
            for x in range(cols):
                boton = Button(self.ventana.frame, text=0,fg="blue",width=2, height=2, command=lambda a=x,b=y: self.onButtonPressed(a,b))
                boton.grid(row=y, column=x)
                buttons_row.append( boton )
                self.matrice3[y][x] = boton["text"]
            self.all_buttons.append( buttons_row )

        self.matrix_B = self.matrice3.copy()
        print("Matrice3 : ", self.matrice3)

    def onButtonPressed(self, i, j):
        print( "pressed: x=%s y=%s" % (i, j))
        global count, matrice3, answer_list
        print("count : ", count)
        if self.all_buttons[j][i]['text'] == 0 and count < 100:
                self.all_buttons[j][i]['text'] = 1
                count += 1
                # prima dell'incremento stampo la lista answer_list
                self.answer_list.append(self.all_buttons[j][i]["text"])
                answer_dict[self.all_buttons[j][i]] = self.all_buttons[j][i]["text"]
                matrix_dict.append(self.all_buttons[j][i])
                print("count : ", count)
                print("texto : ",self.all_buttons[j][i]["text"])
                print("answer_dict = ",answer_dict)
                print("matrix_dict = ",matrix_dict)
                self.matrice3[j][i] = self.all_buttons[j][i]["text"]
                print("Answer_List contiene : ",self.answer_list)
        elif count >= 100:
                # reimposto valori di default
                count = 0
        else:
            messagebox.showinfo("Pattern Matching", "Hai cliccato su una casella piena!")

    def patternCheck(self, b_r, b_c):
        global occ
        rI = len(self.matrix_I)
        cI = len(self.matrix_I[0])
        reset_bc = b_c
        ok = 0
        same = 0
        maxsame = rI * cI
        for i_r in range(0, rI):
            b_c = reset_bc
            for i_c in range(0, cI):
                if self.matrix_I[i_r][i_c] == self.matrix_B[b_r][b_c]:
                    same += 1
                b_c += 1
            b_r += 1
        if same == maxsame:
            ok = 1
            occ += 1
            print("Ok : ", occ)
        return ok

    def cercaP(self, dest, init):
        global ok
        self.matrix_I = init.copy()
        self.matrix_B = dest.copy()
        trovati = 0
        ok = 0
        rlimit = cols - (len(self.matrix_I[0]) - 1)
        # num colonne grande - (num colonne piccola - 1)
        climit = rows - (len(self.matrix_I) - 1)
        # num righe grande - (num righe piccola - 1)
        dimR = len(self.matrix_I)
        dimC = len(self.matrix_I[0])
        dimRB = len(self.matrix_B)
        dimCB = len(self.matrix_B[0])
        if dimC > dimR:
            #caso in cui matrix_I è lunga
            if climit > rlimit:
                tempR = rlimit
                rlimit = climit
                climit = tempR

        elif dimC < dimR:
            if climit < rlimit:
                tempR = rlimit
                rlimit = climit
                climit = tempR

        else:
            #caso in cui è quadrata
            if dimRB > dimCB:
                if climit > rlimit:
                    tempR = rlimit
                    rlimit = climit
                    climit = tempR
            else:
                if climit < rlimit:
                    tempR = rlimit
                    rlimit = climit
                    climit = tempR

        for i in range(rlimit):
            for c in range(climit):
                ok = self.patternCheck(i, c)
                trovati = trovati + ok
                ok = 0  # azzeramento di ok
        return trovati

    def RotateM(self, m):
        self.rows2 = len(m)
        self.cols2 = len(m[0])
        Tm = list(zip(*m))
        print("Transposed matrix = ",Tm)
        return Tm

    def FindPattern(self):
        global matrice2, rows2, cols2, matrix_B
        print("Sei finito in 'Find Pattern'!")
        print("righe matrice bottoni : ", self.rows, " e colonne : ", self.cols)
        print("Matrice2 contiene : ", self.matrice2)
        m = []
        mb = []  # matrix with buttons values
        m = self.matrice2.copy()
        mb = self.matrix_B.copy()
        ris = self.cercaP(mb, m)
        print("----------------------------\n")
        print("Checking for 90° Matrix...\n")
        ok90 = 0
        mT = self.RotateM(m)
        print("Pattern da cercare ruotato di 90° = ", mT)
        print("Tm is = ", mT)
        ris90 = self.cercaP(mb, mT)
        print("----------------------------\n")
        print("Checking for 180° Matrix...\n")
        ok180 = 0
        mTT = self.RotateM(mT)
        print("Pattern da cercare ruotato a 180° = ", mTT)
        ris180 = self.cercaP(mb, mTT)
        print("----------------------------\n")
        print("Checking for 270° Matrix...\n")
        ok270 = 0
        m270 = self.RotateM(mTT)
        print("Pattern da cercare ruotato a 270° = ", mT)
        ris270 = self.cercaP(mb, m270)
        print("----------------------------\n")
        stats.Stats(ris, ris90, ris180, ris270)

VentanaPlay().run()