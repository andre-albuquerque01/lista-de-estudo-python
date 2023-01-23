import os
import random
import sys
from tkinter import * 
from calculo import calculo
import tkinter.messagebox as msbox
# import win32gui, win32con

# def restart_program():
#     python = sys.executable
#     os.execl(python, python, * sys.argv)
        
# try:
#     ocultar_janela = win32gui.GetForegroundWindow()
#     win32gui.Showindow(ocultar_janela, win32con.SW_HIDE)
    
# except:
#     pass

class janela:
    # Class construtora do interface
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg='#1c1c1c')        
        self.fr1.pack()
        
        self.fresult = Frame(raiz, bg='#1c1c1c')        
        self.fresult.pack()
         
        self.fr2 = Frame(raiz, bg='#1c1c1c')        
        self.fr2.pack()
        
        self.fr3 = Frame(raiz, bg='#1c1c1c')        
        self.fr3.pack()
        
        self.fr4 = Frame(raiz, bg='#1c1c1c')        
        self.fr4.pack()
        
        self.fr5 = Frame(raiz, bg='#1c1c1c')        
        self.fr5.pack()
        
        self.fr6 = Frame(raiz, bg='#1c1c1c')        
        self.fr6.pack()
        

        self.lb1 = Label(self.fr1, text="PAR OU ÍMPA", bg="#1c1c1c", fg="#fff" , font=("Times", 20, "italic"), pady=10, padx=50)
        self.lb1.pack(side=LEFT)
        
        self.btn_restart = Button(self.fr1, text="Reiniciar", relief=RAISED, command=self.reiniciar, padx=0, pady=0, font=("Times", 10, "underline"))
        # Para habilitar o uso do teclado
        self.btn_restart.bind("<Return>", self.reiniciar2)
        self.btn_restart.pack(side=LEFT)

        self.img_player = PhotoImage(file="par_impa/imagens/ninja.png")
        self.img_robo = PhotoImage(file="par_impa/imagens/robo.png")
        self.img0 = PhotoImage(file="par_impa/imagens/numero_0.png")
        self.img1 = PhotoImage(file="par_impa/imagens/numero_1.png")
        self.img2 = PhotoImage(file="par_impa/imagens/numero_2.png")
        self.img3 = PhotoImage(file="par_impa/imagens/numero_3.png")
        self.img4 = PhotoImage(file="par_impa/imagens/numero_4.png")
        self.img5 = PhotoImage(file="par_impa/imagens/numero_5.png")
        self.img6 = PhotoImage(file="par_impa/imagens/numero_6.png")
        self.img7 = PhotoImage(file="par_impa/imagens/numero_7.png")
        self.img8 = PhotoImage(file="par_impa/imagens/numero_8.png")
        self.img9 = PhotoImage(file="par_impa/imagens/numero_9.png")
        self.img10 = PhotoImage(file="par_impa/imagens/numero_10.png")
        
        self.result = Label(self.fresult, text="", fg="green", font=("Times", 20, "italic"), bg="#1c1c1c" )
        self.result.pack()
        
        self.placar1 = 0
        self.placar2 = 0
        self.lb2 = Label(self.fr2, text="       Jogador    "+str(self.placar1)+"   x   "+str(self.placar2) + "    Computador", bg="#1c1c1c", fg="#fff", font=("Times", 15, "italic"),padx=40, pady=15)
        self.lb2.pack()
        
        self.lb_imgPlayer = Label(self.fr3, image=self.img_player, bg="#1c1c1c")
        self.lb_imgPlayer.pack(side=LEFT)
        
        self.lb_sperador = Label(self.fr3, text="          ", bg="#1c1c1c")
        self.lb_sperador.pack(side=LEFT)
        
        self.lb_imgRobo = Label(self.fr3, image=self.img_robo, bg="#1c1c1c")
        self.lb_imgRobo.pack(side=LEFT)
        
        # Para ter a escolha do radio
        self.escolha = StringVar()
        # Radio 1
        self.rb_par = Radiobutton(self.fr4, text="PAR", value="par", variable=self.escolha, bg="#1c1c1c", fg="#f3f", font=("Times", 20, "italic"), pady=20)
        self.rb_par.pack(side=LEFT)
        
        # Radio 2
        self.rb_impa = Radiobutton(self.fr4, text="ÍMPA", value="impa", variable=self.escolha, bg="#1c1c1c", fg="#f2f", font=("Times", 20, "italic"), pady=20)
        self.rb_impa.pack(side=LEFT)
        
        self.lb3 = Label(self.fr5, text="Número de 0 a 10: ", bg="#1c1c1c", fg="green", font=("Times", 20, "italic"), width=15, pady=20)
        self.lb3.pack(side=LEFT)
        
        # Para enviar os dados
        self.num = Entry(self.fr5, width=3, font=("Times", 20, "italic"))
        self.num.pack(side=LEFT)
        
        self.bt1 = Button(self.fr6, text="Jogar", bg="#A3A3A3",font=("Times", 20, "italic"), relief=RAISED, command=self.jogar)
        self.bt1.bind("<Return>", self.jogar2)
        self.bt1.focus_force()
        self.bt1.pack()
        
        self.lb4 = Label(self.fr6, text="", font=("Times", 20, "bold"), fg="red", bg="#1c1c1c")
        self.lb4.pack()
        
    def jogar(self):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            escolha_pc = random.randrange(0,10)
            if escolha == "par" or escolha == "impa":
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_imgPlayer['image'] = self.img0
                        print()
                    elif num == 1:
                        self.lb4['text'] = ""
                        self.lb_imgPlayer['image'] = self.img1
                    elif num == 2:
                        self.lb_imgPlayer['image'] = self.img2
                        self.lb4['text'] = ""
                    elif num == 3:
                        self.lb_imgPlayer['image'] = self.img3
                        self.lb4['text'] = ""
                    elif num == 4:
                        self.lb_imgPlayer['image'] = self.img4
                        self.lb4['text'] = ""
                    elif num == 5:
                        self.lb_imgPlayer['image'] = self.img5
                        self.lb4['text'] = ""
                    elif num == 6:
                        self.lb_imgPlayer['image'] = self.img6
                        self.lb4['text'] = ""
                    elif num == 7:
                        self.lb_imgPlayer['image'] = self.img7
                        self.lb4['text'] = ""
                    elif num == 8:
                        self.lb_imgPlayer['image'] = self.img8
                        self.lb4['text'] = ""
                    elif num == 9:
                        self.lb_imgPlayer['image'] = self.img9
                        self.lb4['text'] = ""
                    elif num == 10:
                        self.lb_imgPlayer['image'] = self.img10
                        self.lb4['text'] = ""
                    
                    
                    if escolha_pc == 0:
                        self.lb_imgRobo['image'] = self.img0
                        pass
                    elif escolha_pc == 1:
                        self.lb_imgRobo['image'] = self.img1
                        pass
                    elif escolha_pc == 2:
                        self.lb_imgRobo['image'] = self.img2
                        pass
                    elif escolha_pc == 3:
                        self.lb_imgRobo['image'] = self.img3
                        pass
                    elif escolha_pc == 4:
                        self.lb_imgRobo['image'] = self.img4
                        pass
                    elif escolha_pc == 5:
                        self.lb_imgRobo['image'] = self.img5
                        pass
                    elif escolha_pc == 6:
                        self.lb_imgRobo['image'] = self.img6
                        pass
                    elif escolha_pc == 7:
                        self.lb_imgRobo['image'] = self.img7
                        pass
                    elif escolha_pc == 8:
                        self.lb_imgRobo['image'] = self.img8
                        pass
                    elif escolha_pc == 9:
                        self.lb_imgRobo['image'] = self.img9
                        pass
                    elif escolha_pc == 10:
                        self.lb_imgRobo['image'] = self.img10
                        pass
                    
                    par_impa = calculo(num, escolha_pc)
                    if num >= 0 and num <= 10:            
                        if par_impa  == "Par":
                            self.result['text'] = "Par o vencedor"
                        elif par_impa == "Ímpa":
                            self.result['text'] = "Ímpa o vencedor"
                        else:
                            self.result['text'] = "Aconteceu um imprevisto"
                    
                    if par_impa == "Par" and escolha == "par":
                        self.placar1 += 1
                        
                    elif par_impa == "Ímpa" and escolha == "impa":
                        self.placar1 += 1
                        
                    elif par_impa == "Ímpa" and escolha == "par":
                        self.placar2 += 1
                        
                    elif par_impa == "Par" and escolha == "impa":
                        self.placar2 += 1
                    self.lb2['text'] = "       Jogador    "+str(self.placar1)+"   x   "+str(self.placar2) + "    Computador"
                else:
                    self.lb4['text'] = "Escolha par ou ímpa e um  número de 1 a 10"
                    
            else:
                self.lb4['text'] = "Precisa escolher PAR ou ÍMPA"
                self.lb4['text'] = ""
                
        except:
            self.lb4['text'] = "Escolha par ou ímpa e um  número de 1 a 10"
            
    
    def jogar2(self, event):
        try:
            num = int(self.num.get())
            escolha = self.escolha.get()
            escolha_pc = random.randrange(0,10)
            if escolha == "par" or escolha == "impa":
                if num >= 0 and num <= 10:
                    if num == 0:
                        self.lb_imgPlayer['image'] = self.img0
                        print()
                    elif num == 1:
                        self.lb4['text'] = ""
                        self.lb_imgPlayer['image'] = self.img1
                    elif num == 2:
                        self.lb_imgPlayer['image'] = self.img2
                        self.lb4['text'] = ""
                    elif num == 3:
                        self.lb_imgPlayer['image'] = self.img3
                        self.lb4['text'] = ""
                    elif num == 4:
                        self.lb_imgPlayer['image'] = self.img4
                        self.lb4['text'] = ""
                    elif num == 5:
                        self.lb_imgPlayer['image'] = self.img5
                        self.lb4['text'] = ""
                    elif num == 6:
                        self.lb_imgPlayer['image'] = self.img6
                        self.lb4['text'] = ""
                    elif num == 7:
                        self.lb_imgPlayer['image'] = self.img7
                        self.lb4['text'] = ""
                    elif num == 8:
                        self.lb_imgPlayer['image'] = self.img8
                        self.lb4['text'] = ""
                    elif num == 9:
                        self.lb_imgPlayer['image'] = self.img9
                        self.lb4['text'] = ""
                    elif num == 10:
                        self.lb_imgPlayer['image'] = self.img10
                        self.lb4['text'] = ""
                    
                    
                    if escolha_pc == 0:
                        self.lb_imgRobo['image'] = self.img0
                        pass
                    elif escolha_pc == 1:
                        self.lb_imgRobo['image'] = self.img1
                        pass
                    elif escolha_pc == 2:
                        self.lb_imgRobo['image'] = self.img2
                        pass
                    elif escolha_pc == 3:
                        self.lb_imgRobo['image'] = self.img3
                        pass
                    elif escolha_pc == 4:
                        self.lb_imgRobo['image'] = self.img4
                        pass
                    elif escolha_pc == 5:
                        self.lb_imgRobo['image'] = self.img5
                        pass
                    elif escolha_pc == 6:
                        self.lb_imgRobo['image'] = self.img6
                        pass
                    elif escolha_pc == 7:
                        self.lb_imgRobo['image'] = self.img7
                        pass
                    elif escolha_pc == 8:
                        self.lb_imgRobo['image'] = self.img8
                        pass
                    elif escolha_pc == 9:
                        self.lb_imgRobo['image'] = self.img9
                        pass
                    elif escolha_pc == 10:
                        self.lb_imgRobo['image'] = self.img10
                        pass
                    
                    par_impa = calculo(num, escolha_pc)
                    if num >= 0 and num <= 10:            
                        if par_impa  == "Par":
                            self.result['text'] = "Par o vencedor"
                        elif par_impa == "Ímpa":
                            self.result['text'] = "Ímpa o vencedor"
                        else:
                            self.result['text'] = "Aconteceu um imprevisto"
                    
                    if par_impa == "Par" and escolha == "par":
                        self.placar1 += 1
                        
                    elif par_impa == "Ímpa" and escolha == "impa":
                        self.placar1 += 1
                        
                    elif par_impa == "Ímpa" and escolha == "par":
                        self.placar2 += 1
                        
                    elif par_impa == "Par" and escolha == "impa":
                        self.placar2 += 1
                    self.lb2['text'] = "       Jogador    "+str(self.placar1)+"   x   "+str(self.placar2) + "    Computador"
                else:
                    self.lb4['text'] = "Escolha par ou ímpa e um  número de 1 a 10"
                    
            else:
                self.lb4['text'] = "Precisa escolher PAR ou ÍMPA"
                self.lb4['text'] = ""
                
        except:
            self.lb4['text'] = "Escolha par ou ímpa e um  número de 1 a 10"
    
    def reiniciar(self):
        # py = sys.executable
        # os.execl(py, py, sys.argv)
        
        resposta = msbox.askquestion("Restart","Deseja reiniciar?")
        if resposta == "yes":
            self.lb_imgPlayer['image'] = self.img_player
            self.lb_imgRobo['image'] = self.img_robo
            self.placar1 = 0
            self.placar2 = 0
            self.result['text'] = ""
            self.lb2['text'] = "       Jogador    "+str(self.placar1)+"   x   "+str(self.placar2) + "    Computador"
    def reiniciar2(self, event):
        resposta = msbox.askquestion("Restart","Deseja reiniciar?")
        if resposta == "yes":
            self.lb_imgPlayer['image'] = self.img_player
            self.lb_imgRobo['image'] = self.img_robo
            self.placar1 = 0
            self.placar2 = 0
            self.result['text'] = ""
            self.lb2['text'] = "       Jogador    "+str(self.placar1)+"   x   "+str(self.placar2) + "    Computador"
        
        

raiz = Tk()
raiz.geometry("640x650")
raiz.title("Par ou Ímpa")
raiz['bg'] = "#1c1c1c"

abertura = janela(raiz)

raiz.mainloop()