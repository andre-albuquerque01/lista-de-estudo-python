from tkinter import *


class janela:

    def __init__(self, raiz):
        
        filename = 'a1.png'
        self.img = PhotoImage(file=filename)
        
        self.fr1 = Frame(raiz, bg="#fff", highlightbackground="gray", highlightthickness=3)
        self.fr1.pack()

        self.lb1 = Label(self.fr1, text='Vai Brasil!!!', background="#fff", font=("times", 20 ,"bold","italic"))
        self.lb1.pack()
                
        self.fr2 = Frame(raiz, bg="#fff")
        self.fr2.pack()
        self.bt1 = Button(self.fr2, text="Clique aqui", bg="#fff" , font=("arial",15,"italic"), command=self.muda_label)
        self.bt1.bind("<Return>", self.muda_label2)
        self.bt1.pack()
        self.bt1['relief'] = RAISED
        self.bt1['border'] = 10
        
        
        self.lb2 = Label(self.fr1, bg="#fff", text="        ", width=20)
        self.lb2.pack()    
        self.lb3 = Label(self.fr2, bg="#fff", text="        ", width=20)
        self.lb3.pack()
        
    def muda_label(self):
        # self.lb1['text'] = "Deu certo!"
        for i in range(1,5):
            self.lb1['text'] = i
        # self.lb_img = Label(raiz, image=self.img)
        # self.lb_img.pack()
        
    def muda_label2(self, event):
        self.lb1['text'] = "Deu certo!"
        # self.lb_img = Label(raiz, image=self.img)
        # self.lb_img.pack()
        
raiz = Tk()
janela(raiz)
raiz.geometry("500x500")
raiz.title("Testando Tkinter")
# fileicon = "icone.ico"
# raiz.iconbitmap(fileicon)

# Para remover a guia
# raiz.overrideredirect(TRUE)



raiz['bg'] = '#fff'
raiz.mainloop()