from tkinter import *
 
formule = "" 
 
def click(num): 
 
    global formule 
    formule = formule + str(num) 
    equation.set(formule) 
 
def equalclick(): 
    try: 
        global formule 
 
        result = str(eval(formule)) 
        equation.set(result) 
        formule = result
 
    except: 
        equation.set(" error ") 
        formule = "" 
#définition des différentes fonctions pour les boutons
def pourcentage():
    global formule
    resultat = eval(formule)/100
    equation.set(resultat)
    formule = str(resultat)
def racine():
    global formule
    resultat = eval(formule)**0.5
    equation.set(resultat)
    formule = str(resultat)

def inverse():
    global formule
    resultat = 1/eval(formule)
    equation.set(resultat)
    formule = str(resultat) 
def effacer(): 
    global formule 
    formule = "" 
    equation.set("")
def bt0():
    global formule
    formule = formule + "0"
    equation.set(formule)
def bt1():
    global formule
    formule = formule + "1"
    equation.set(formule)
def bt2():
    global formule
    formule = formule + "2"
    equation.set(formule)
def bt3():
    global formule
    formule = formule + "3"
    equation.set(formule)
def bt4():
    global formule
    formule = formule + "4"
    equation.set(formule)
def bt5():
    global formule
    formule = formule + "5"
    equation.set(formule)
def bt6():
    global formule
    formule = formule + "6"
    equation.set(formule)
def bt7():
    global formule
    formule = formule + "7"
    equation.set(formule)
def bt8():
    global formule
    formule = formule + "8"
    equation.set(formule)
def bt9():
    global formule
    formule = formule + "9"
    equation.set(formule)
def bt_plus():
    global formule
    formule = formule + "+"
    equation.set(formule)
def bt_moins():
    global formule
    formule = formule + "-"
    equation.set(formule)
def bt_mult():
    global formule
    formule = formule + "*"
    equation.set(formule)
def bt_div():
    global formule
    formule = formule + "/"
    equation.set(formule)
def bt_point():
    global formule
    formule = formule + "."
    equation.set(formule)      
#mise en place du tableau des boutons ainsi que leurs styles 
if __name__ == "__main__": 
    master = Tk() 
    master.title("Calculatrice") 
    master.geometry("375x375") 
    master.configure(background="#272626")
    equation = StringVar() 
    zone_resultat = Entry(master, textvariable=equation, background="#272626", fg="white") 
    zone_resultat.grid(columnspan=4,  pady= 30 , padx = 20 , ipadx = 100 , ipady = 10 )
    
    bouton_0 = Button(master, text=' 0 ', command=bt0, height=2, width=10, background="#505050", fg="white") 
    bouton_0.grid(row=5,column=1)

    bouton_1 = Button(master, text=' 1 ', command=bt1, height=2, width=10, background="#505050", fg="white") 
    bouton_1.grid(row=4,column=0)

    bouton_2 = Button(master, text=' 2 ', command=bt2, height=2, width=10, background="#505050", fg="white") 
    bouton_2.grid(row=4,column=1)

    bouton_3 = Button(master, text=' 3 ', command=bt3, height=2, width=10, background="#505050", fg="white") 
    bouton_3.grid(row=4,column=2)

    bouton_4 = Button(master, text=' 4 ', command=bt4, height=2, width=10, background="#505050", fg="white") 
    bouton_4.grid(row=3,column=0)

    bouton_5 = Button(master, text=' 5 ', command=bt5, height=2, width=10, background="#505050", fg="white") 
    bouton_5.grid(row=3,column=1)

    bouton_6 = Button(master, text=' 6 ', command=bt6, height=2, width=10, background="#505050", fg="white") 
    bouton_6.grid(row=3,column=2)

    bouton_7 = Button(master, text=' 7 ', command=bt7, height=2, width=10, background="#505050", fg="white") 
    bouton_7.grid(row=2,column=0)

    bouton_8 = Button(master, text=' 8 ', command=bt8, height=2, width=10, background="#505050", fg="white")
    bouton_8.grid(row=2, column=1)

    bouton_9 = Button(master, text=' 9 ', command=bt9, height=2, width=10, background="#505050", fg="white")
    bouton_9.grid(row=2, column=2)
 
    plus = Button(master, text=' + ', command=bt_plus, height=2, width=10,background="#414141", fg="white") 
    plus.grid(row=2, column=3) 
 
    moins = Button(master, text=' - ', command=bt_moins, height=2, width=10,background="#414141", fg="white") 
    moins.grid(row=3, column=3) 
 
    mult = Button(master, text=' * ', command=bt_mult, height=2, width=10,background="#414141", fg="white") 
    mult.grid(row=4, column=3) 
 
    div = Button(master, text=' / ', command=bt_div, height=2, width=10,background="#414141", fg="white") 
    div.grid(row=5, column=3)

    point= Button(master, text='.', command=bt_point, height=2, width=10,background="#414141", fg="white") 
    point.grid(row=5, column=0)

    égal = Button(master, text=' = ', command=equalclick, height=2, width=10,background="#BCB972") 
    égal.grid(row=6, column=3) 
 
    effacer = Button(master, text='effacer', command=effacer, height=2, width=10,background="#414141", fg="white") 
    effacer.grid(row=6, column=0) 
 
    pourcentage = Button(master, text=' % ', command=pourcentage, height=2, width=10,background="#414141", fg="white") 
    pourcentage.grid(row=6, column=1)
    
    racine = Button(master, text=' √ ', command=racine, height=2, width=10,background="#414141", fg="white") 
    racine.grid(row=5, column=2)

    inverse = Button(master, text=' 1/x ', command=inverse, height=2, width=10,background="#414141", fg="white") 
    inverse.grid(row=6, column=2)
      
    
master.mainloop()