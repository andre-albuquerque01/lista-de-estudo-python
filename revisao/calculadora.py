from tkinter import *
from calculo import *

class Calculadora:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz)
        self.fr1.pack()
        
        self.fr2 = Frame(raiz)
        self.fr2.pack()
        
        self.fr3 = Frame(raiz)
        self.fr3.pack()
        
        self.fresult = Frame(raiz)
        self.fresult.pack()
        
        self.fr4 = Frame(raiz)
        self.fr4.pack()
        
        self.frerro = Frame(raiz)
        self.frerro.pack()        
        
        # Titulo
        self.lb1 = Label(self.fr1, text="Calculadora", fg="#f0f")
        self.lb1.pack()
        
        self.escolha = StringVar()
        # Button radio de soma
        self.soma = Radiobutton(self.fr2, text="Soma", value="soma", variable=self.escolha)
        self.soma.pack()
        
        # Button radio de subtração
        self.sub = Radiobutton(self.fr2, text="Subtração", value="sub", variable=self.escolha)
        self.sub.pack()
        
        # Button radio de multiplicação
        self.mult = Radiobutton(self.fr2, text="Multiplicação", value="mult", variable=self.escolha)
        self.mult.pack()
        
        # Button radio de divisão
        self.div = Radiobutton(self.fr2, text="Divisão", value="div", variable=self.escolha)
        self.div.pack()
        
        self.num = Entry(self.fr3, width=3)
        self.num.pack(side=LEFT)
        
        self.esco = Label(self.fr3, text="")
        self.esco.pack(side=LEFT)
        
        self.num2 = Entry(self.fr3, width=3)
        self.num2.pack(side=LEFT)
        
        self.result = Label(self.fresult, text="")
        self.result.pack()
        
        self.bt1 = Button(self.fr4, text="Calcular", relief=RAISED, command=self.calcular)
        self.bt1.bind("<Return>", self.calcular2)
        self.bt1.pack()
        
        self.erro = Label(self.frerro, text="", fg="#f00")
        
    def calcular(self):
        try:
            num = int(self.num.get())
            num2 = int(self.num2.get())
            escolha = self.escolha.get()
            if escolha == "soma" or escolha == "div" or escolha == "mult" or escolha == "sub":
                if escolha == "soma":
                    som = soma(num, num2)  
                    self.result['text'] = "A soma é de %i"%som
                    self.esco["text"] = "    +    "
                elif escolha == "div":
                    divi = div(num, num2)          
                    self.result['text'] = "A divisão é de %i"%divi
                    self.esco["text"] = "    /    "
                elif escolha == "mult":
                    multi = mult(num, num2)        
                    self.result['text'] = "A multiplicação é de %i"%multi
                    self.esco["text"] = "    x    "
                elif escolha == "sub":
                    subi = sub(num, num2)    
                    self.result['text'] = "A subtração é de %i"%subi
                    self.esco["text"] = "    -    "
            else:
                self.erro["text"] = "Escolha uma operação"                
            
        except:
            self.erro["text"] = "Houve um erro na tentativa"
    def calcular2(self, event):
        try:
            num = int(self.num.get())
            num2 = int(self.num2.get())
            escolha = self.escolha.get()
            
            if escolha == "soma":
                som = soma(num, num2)  
                self.result['text'] = "A soma é de %i"%som
            elif escolha == "div":
                divi = div(num, num2)          
                self.result['text'] = "A divisão é de %i"%divi
            elif escolha == "mult":
                multi = mult(num, num2)        
                self.result['text'] = "A multiplicação é de %i"%multi
            elif escolha == "sub":
                subi = sub(num, num2)    
                self.result['text'] = "A subtração é de %i"%subi
            
            self.esco["text"] = "    " + str(self.escolha) + "    "
        except:
            self.erro["text"] = "Houve um erro na tentativa"
    
raiz = Tk()
raiz.title("Calculadora")
raiz.geometry("300x300")
abertura = Calculadora(raiz)

raiz.mainloop()