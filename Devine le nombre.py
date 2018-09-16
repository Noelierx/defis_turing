from random import randrange
from tkinter import*
print("Je vais vous faire deviner un nombre entre 0 et 100")
N = randrange(0,  101)
a=0
b=0
while ( int(a)!=N) :
     a = input ("Alors à votre avis quelle est la valeur du nombre :")
     b = b+1
     if int(a)==N :
         print("Bien jouer tu as gagné en",b,"coups")
         fen1 =Tk()
         tex1 = Label(fen1, text='Bien joué tu as gagné !!!!', fg= 'blue')
         tex1.pack()
         bou1 = Button(fen1, text='OK', command=fen1.destroy)
         bou1.pack()
         fen1.geometry("150x90+350-350")
         fen1.mainloop()
         break
     elif int(a) <N :
         print("C'est trop petit")
     else :
         print("C'est trop grand")
         
     


        
