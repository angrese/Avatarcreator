import tkinter as tk

class Finestra(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master.geometry("1000x1000")
        self.master.title("AvatarCreator")
        self.grid()

        self.vR = tk.IntVar()

        self.lblBenvenuto = tk.Label()
        self.lblBenvenuto.grid(row=0, column=3,  sticky=tk.N)
        self.lblBenvenuto.configure(background="#d9d9d9")
        self.lblBenvenuto.configure(foreground="#000000")
        self.lblBenvenuto.configure(text="Benvenuto in AvatarCreator, lo strumento creativo per dare vita al tuo avatar unico!")

        

        self.lblNome = tk.Label()
        self.lblNome.grid(row=4, column=0, sticky=tk.NW)
        self.lblNome.configure(background="#d9d9d9")
        self.lblNome.configure(foreground="#000000")
        self.lblNome.configure(text="Scegli il nome del tuo personaggio")

        self.lstNomi = tk.Listbox(width=10, height=4, selectmode=tk.SINGLE)
        self.lstNomi.grid(row=4, column=1)

        nomi=['Sara', 'Valeria','Giulia', 'Carlotta','Maria', 'Martina', 'Beatrice','Aurora','Fabio','Simone', 'Davide', 'Lorenzo', 'Vittorio', 'Paolo', 'Nicola', 'Gabriel'  ]
        for i in nomi:
            self.lstNomi.insert(tk.END, i)

        self.lstNomi.bind('<<ListboxSelect>>', self.selezione)

        self.scrb = tk.Scrollbar(orient=tk.VERTICAL)
        self.scrb.grid(row=4, column=2, sticky=tk.W + tk.N + tk.S )
        self.scrb.config(command=self.lstNomi.yview)



        
        self.lb1Anni = tk.Label()
        self.lb1Anni.grid(row=8, column=0, sticky=tk.W)
        self.lb1Anni.configure(background="#d9d9d9")
        self.lb1Anni.configure(foreground="#000000")
        self.lb1Anni.configure(text="Inserisci la tua età")

        self.vA = tk.IntVar()
        self.txtA = tk.Entry()
        self.txtA.grid(row=8, column=1, sticky=tk.W)
        self.txtA.configure(background="white")
        self.txtA.configure(foreground="#000001")



        self.vE = tk.IntVar()
        self.lblEtnia = tk.Label()
        self.lblEtnia.grid(row=10, column=0, sticky=tk.W)
        self.lblEtnia.configure(background="#d9d9d9")
        self.lblEtnia.configure(foreground="#000000")
        self.lblEtnia.configure(text="Seleziona la tonalità della carnagione")

        self.rdbEtnia1 = tk.Radiobutton(text="Europeo", variable=self.vE, value=1, command=self.get_etnia)
        self.rdbEtnia1.grid(row=10, column=1, sticky=tk.W)
        self.rdbEtnia2 = tk.Radiobutton(text="Africano", variable=self.vE, value=2, command=self.get_etnia)
        self.rdbEtnia2.grid(row=10, column=2, sticky=tk.W)
        self.rdbEtnia3 = tk.Radiobutton(text="Asiatico", variable=self.vE, value=3, command=self.get_etnia)
        self.rdbEtnia3.grid(row=10, column=3, sticky=tk.W)




        self.vC = tk.IntVar()
        self.lblCapelli = tk.Label()
        self.lblCapelli.grid(row=11, column=0, sticky=tk.W)
        self.lblCapelli.configure(background="#d9d9d9")
        self.lblCapelli.configure(foreground="#000000")
        self.lblCapelli.configure(text="Seleziona il colore dei capelli")

        self.rdbCapelli1 = tk.Radiobutton(text="Biondi", variable=self.vC, value=1, command=self.get_capelli)
        self.rdbCapelli1.grid(row=11, column=1, sticky=tk.W)
        self.rdbCapelli2 = tk.Radiobutton(text="Castani", variable=self.vC, value=2, command=self.get_capelli)
        self.rdbCapelli2.grid(row=11, column=2, sticky=tk.W)
        self.rdbCapelli3 = tk.Radiobutton(text="Grigi", variable=self.vC, value=3, command=self.get_capelli)
        self.rdbCapelli3.grid(row=11, column=3, sticky=tk.W)




        self.vM = tk.IntVar()
        self.lblMaglia = tk.Label()
        self.lblMaglia.grid(row=12, column=0, sticky=tk.W)
        self.lblMaglia.configure(background="#d9d9d9")
        self.lblMaglia.configure(foreground="#000000")
        self.lblMaglia.configure(text="Seleziona il colore della maglia")

        self.rdbMaglia1 = tk.Radiobutton(text="Arancione", variable=self.vM, value=1, command=self.get_maglia)
        self.rdbMaglia1.grid(row=12, column=1, sticky=tk.W)
        self.rdbMaglia2 = tk.Radiobutton(text="Verde", variable=self.vM, value=2, command=self.get_maglia)
        self.rdbMaglia2.grid(row=12, column=2, sticky=tk.W)
        self.rdbMaglia3 = tk.Radiobutton(text="Azzurro", variable=self.vM, value=3, command=self.get_maglia)
        self.rdbMaglia3.grid(row=12, column=3, sticky=tk.W)




        self.vP = tk.IntVar()
        self.lblPantaloni = tk.Label()
        self.lblPantaloni.grid(row=13, column=0, sticky=tk.W)
        self.lblPantaloni.configure(background="#d9d9d9")
        self.lblPantaloni.configure(foreground="#000000")
        self.lblPantaloni.configure(text="Seleziona il colore dei pantaloni")

        self.rdbPantaloni1 = tk.Radiobutton(text="Viola", variable=self.vP, value=1, command=self.get_pantaloni)
        self.rdbPantaloni1.grid(row=13, column=1, sticky=tk.W)
        self.rdbPantaloni2 = tk.Radiobutton(text="Blu", variable=self.vP, value=2, command=self.get_pantaloni)
        self.rdbPantaloni2.grid(row=13, column=2, sticky=tk.W)
        self.rdbPantaloni3 = tk.Radiobutton(text="Rosso", variable=self.vP, value=3, command=self.get_pantaloni)
        self.rdbPantaloni3.grid(row=13, column=3, sticky=tk.W)




        self.vS = tk.IntVar()
        self.lblScarpe = tk.Label()
        self.lblScarpe.grid(row=14, column=0, sticky=tk.W)
        self.lblScarpe.configure(background="#d9d9d9")
        self.lblScarpe.configure(foreground="#000000")
        self.lblScarpe.configure(text="Seleziona il colore delle scarpe")

        self.rdbScarpe1 = tk.Radiobutton(text="Nero", variable=self.vS, value=1, command=self.get_scarpe)
        self.rdbScarpe1.grid(row=14, column=1, sticky=tk.W)
        self.rdbScarpe2 = tk.Radiobutton(text="Bianco", variable=self.vS, value=2, command=self.get_scarpe)
        self.rdbScarpe2.grid(row=14, column=2, sticky=tk.W)
        self.rdbScarpe3 = tk.Radiobutton(text="Verde", variable=self.vS, value=3, command=self.get_scarpe)
        self.rdbScarpe3.grid(row=14, column=3, sticky=tk.W)

       

        # sfondo
        self.c1 = tk.Canvas(width=400, height=500, bg='lightblue')
        self.c1.grid(row=15, column=0)
        # testa
        self.c1.create_oval(155, 55, 245, 145, fill='white')
        #capelli
        self.c1.create_arc(155, 40, 245, 130, fill='white', start=0,extent=180)
        # corpo
        self.c1.create_rectangle(155, 145, 240, 300, fill='white')
        # braccia
        self.c1.create_rectangle(100,200,155,220, fill='white')
        self.c1.create_rectangle(240,200,295,220, fill='white')
        # gambe
        self.c1.create_rectangle(155,300,185,430, fill='white')
        self.c1.create_rectangle(210, 300, 240, 430, fill='white')
        # piedi
        self.c1.create_rectangle(150, 430, 190, 450, fill='white')
        self.c1.create_rectangle(205, 430, 245, 450, fill='white')

        
        self.vRis=tk.IntVar() 
        self.txt2 = tk.Entry(textvariable=self.vRis)
        self.txt2.grid(row=4, column=6)
        self.txt2.configure(background="white")
        self.txt2.configure(foreground="#000000")


        self.buttonEsci = tk.Button()
        self.buttonEsci.grid(row=15, column=1,sticky=tk.SE )
        self.buttonEsci.configure(background="#d9d9d9")
        self.buttonEsci.configure(foreground="#000000")
        self.buttonEsci.configure(text="Esci")
        self.buttonEsci.configure(command=self.master.destroy)





    def selezione(self,event):
        y=self.lstNomi.get(self.lstNomi.curselection())
        

        out="ciao "+y +"!"
        self.vRis.set(out)

        
    def get_capelli(self):
        a = self.vC.get()
        if a == 1:
            self.c1.create_arc(155, 40, 245, 130, fill='yellow', start=0,extent=180)
           
        elif a == 2:
            self.c1.create_arc(155, 40, 245, 130, fill='brown', start=0,extent=180)
          
        elif a == 3:self.c1.create_arc(155, 40, 245, 130, fill='grey', start=0,extent=180)
          

    def get_etnia(self):
        a = self.vE.get()
        if a == 1:
            self.c1.create_rectangle(100,200,155,220, fill='lightpink')
            self.c1.create_rectangle(240,200,295,220, fill='lightpink')
            self.c1.create_oval(155, 55, 245, 145, fill='lightpink')
        elif a == 2:
            self.c1.create_rectangle(100,200,155,220, fill='#6c3c0c')
            self.c1.create_rectangle(240,200,295,220, fill='#6c3c0c')
            self.c1.create_oval(155, 55, 245, 145, fill='#6c3c0c')
        elif a == 3:
            self.c1.create_rectangle(100,200,155,220, fill='lightyellow')
            self.c1.create_rectangle(240,200,295,220, fill='lightyellow')
            self.c1.create_oval(155, 55, 245, 145, fill='lightyellow')

    def get_maglia(self):
        a = self.vM.get()
        if a == 1:
            self.c1.create_rectangle(155, 145, 240, 300, fill='orange')
        elif a == 2:
            self.c1.create_rectangle(155, 145, 240, 300, fill='green')
        elif a == 3:
            self.c1.create_rectangle(155, 145, 240, 300, fill='cyan')

    def get_pantaloni(self):
        a = self.vP.get()
        if a == 1:
            self.c1.create_rectangle(155,300,185,430, fill='purple')
            self.c1.create_rectangle(210, 300, 240, 430, fill='purple')
        elif a == 2:
            self.c1.create_rectangle(155,300,185,430, fill='blue')
            self.c1.create_rectangle(210, 300, 240, 430, fill='blue')
        elif a == 3:
            self.c1.create_rectangle(155,300,185,430, fill='red')
            self.c1.create_rectangle(210, 300, 240, 430, fill='red')

    def get_scarpe(self):
        a = self.vS.get()
        if a == 1:
            self.c1.create_rectangle(150, 430, 190, 450, fill='black')
            self.c1.create_rectangle(205, 430, 245, 450, fill='black')
        elif a == 2:
            self.c1.create_rectangle(150, 430, 190, 450, fill='white')
            self.c1.create_rectangle(205, 430, 245, 450, fill='white')
        elif a == 3:
            self.c1.create_rectangle(150, 430, 190, 450, fill='green')
            self.c1.create_rectangle(205, 430, 245, 450, fill='green')


def main():
    f = Finestra()
    f.mainloop()

main()
