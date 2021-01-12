from tkinter import *

win=Tk()
win.geometry("500x600+400+100")
win.configure(bg="lightblue")
win.title("Tic Tac Toe Game")

#####################VAriables Declared########################
player1=StringVar()
player2=StringVar()

stats=StringVar()

a=[[8,8,8],[8,8,8],[8,8,8]]
a1=StringVar()
a2=StringVar()
a3=StringVar()
a4=StringVar()
a5=StringVar()
a6=StringVar()
a7=StringVar()
a8=StringVar()
a9=StringVar()

a1.set(str(" 8 "))
a2.set(str(" 8 "))
a3.set(str(" 8 "))
a4.set(str(" 8 "))
a5.set(str(" 8 "))
a6.set(str(" 8 "))
a7.set(str(" 8 "))
a8.set(str(" 8 "))
a9.set(str(" 8 "))

counter=0
###############################################################

#####################functions declared########################
def instruction():
    win1=Tk()
    win1.geometry("500x600+400+100")
    win1.configure(bg="white")
    win1.title("Tic Tac Toe Game")

    lab=Label(win1,text="THE TIC TAC TOE GAME",font=("consolas",22,"bold"),bg="red",fg="LIGHTYELLOw")
    lab.pack(fill=X)

    text=Text(win1,font=("bahnscrift semibold",18),height=17,width=35,bg="lightblue",fg="black")
    text.pack(pady=10)

    text.insert(INSERT,"This is a game of 3X3 Matrix.")
    text.insert(INSERT,"\nYou have to play this game using your numpad:")
    text.insert(INSERT,"\n\t 7\t8\t9 ")
    text.insert(INSERT,"\n\t 4\t5\t6 ")
    text.insert(INSERT,"\n\t 1\t2\t3 ")
    text.insert(INSERT,"\nThe First Player will be alloted the number 0 and second player with 1 after when you click to all set Button.")
    text.insert(INSERT,"\nYou will win the game when either the diagonals or any one row or any one column will made equal with any one value(either with X or O).")
    text.insert(INSERT,"\nplayer's Chance will come alternatively.")
    text.insert(INSERT,"\n\n\tProject Made By: Sachin Gupta")
    text.insert(INSERT,"\n\t\tFrom BCA-3rd Sem.")

    bt_ex=Button(win1,text="Back to Main",font=("Consolas",18),bg="BLUE",fg="YELLOW",command=lambda: win1.destroy())
    bt_ex.pack(pady=5)
    
    win.mainloop()
    

def clear():
    global a
    global counter
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    global player1,player2
    
    a=[[8,8,8],[8,8,8],[8,8,8]] 
    
    a1.set(str(" 8 "))
    a2.set(str(" 8 "))
    a3.set(str(" 8 "))
    a4.set(str(" 8 "))
    a5.set(str(" 8 "))
    a6.set(str(" 8 "))
    a7.set(str(" 8 "))
    a8.set(str(" 8 "))
    a9.set(str(" 8 "))
    player1.set(str(" "))
    player2.set(str(" "))
    counter=0

def check():
    global a
    global stats

    #For Player 1
    if a[0][0]==0 and a[0][1]==0 and a[0][2]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))
    elif a[1][0]==0 and a[1][1]==0 and a[1][2]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))
    elif a[2][0]==0 and a[2][1]==0 and a[2][2]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))

    elif a[0][0]==0 and a[1][1]==0 and a[2][2]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))
    elif a[0][2]==0 and a[1][1]==0 and a[2][0]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))

    elif a[0][0]==0 and a[1][0]==0 and a[2][0]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))
    elif a[0][1]==0 and a[1][1]==0 and a[2][1]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))
    elif a[2][0]==0 and a[2][1]==0 and a[2][2]==0:
        stats.set(str(str("Player 0: ") + str(ent1.get()) + " Wins..."))

    #For Player 2
    if a[0][0]==1 and a[0][1]==1 and a[0][2]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))
    elif a[1][0]==1 and a[1][1]==1 and a[1][2]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))
    elif a[2][0]==1 and a[2][1]==1 and a[2][2]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))

    elif a[0][0]==1 and a[1][1]==1 and a[2][2]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))
    elif a[0][2]==1 and a[1][1]==1 and a[2][0]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))

    elif a[0][0]==1 and a[1][0]==1 and a[2][0]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))
    elif a[0][1]==1 and a[1][1]==1 and a[2][1]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))
    elif a[2][0]==1 and a[2][1]==1 and a[2][2]==1:
        stats.set(str(str("Player 1: ") + str(ent2.get()) + "Wins..."))

def player_set():
    global player1
    global player2

    player1.set(str(ent1.get()))
    player2.set(str(ent2.get()))

    print("the players are defined as:")
    print("Player 1: ",str(player1.get()))
    print("Player 2: ",str(player2.get()))

def val_upd(data):
    global a
    global counter
    global a1,a2,a3,a4,a5,a6,a7,a8,a9
    if counter%2==0 and counter!=10:
        if data==7:
            a[0][0]=0
            a7.set(str(" " + str(a[0][0]) + " "))
        if data==8:
            a[0][1]=0
            a8.set(str(" " + str(a[0][1]) + " "))
        if data==9:
            a[0][2]=0
            a9.set(str(" " + str(a[0][2]) + " "))
        if data==4:
            a[1][0]=0
            a4.set(str(" " + str(a[1][0]) + " "))
        if data==5:
            a[1][1]=0
            a5.set(str(" " + str(a[1][1]) + " "))
        if data==6:
            a[1][2]=0
            a6.set(str(" " + str(a[1][2]) + " "))
        if data==1:
            a[2][0]=0
            a1.set(str(" " + str(a[2][0]) + " "))
        if data==2:
            a[2][1]=0
            a2.set(str(" " + str(a[2][1]) + " "))
        if data==3:
            a[2][2]=0
            a3.set(str(" " + str(a[2][2]) + " "))
        check()
    elif counter%2==1 and counter!=10:
        if data==7:
            a[0][0]=1
            a7.set(str(" " + str(a[0][0]) + " "))
        if data==8:
            a[0][1]=1
            a8.set(str(" " + str(a[0][1]) + " "))
        if data==9:
            a[0][2]=1
            a9.set(str(" " + str(a[0][2]) + " "))
        if data==4:
            a[1][0]=1
            a4.set(str(" " + str(a[1][0]) + " "))
        if data==5:
            a[1][1]=1
            a5.set(str(" " + str(a[1][1]) + " "))
        if data==6:
            a[1][2]=1
            a6.set(str(" " + str(a[1][2]) + " "))
        if data==1:
            a[2][0]=1
            a1.set(str(" " + str(a[2][0]) + " "))
        if data==2:
            a[2][1]=1
            a2.set(str(" " + str(a[2][1]) + " "))
        if data==3:
            a[2][2]=1
            a3.set(str(" " + str(a[2][2]) + " "))
    counter+=1
    check()
        
###############################################################

lab=Label(win,text="THE TIC TAC TOE GAME",font=("consolas",22,"bold"),bg="red",fg="LIGHTYELLOw")
lab.pack(fill=X)
        
frame1=Frame(win,bg="lightblue")
frame1.pack(side=TOP)

lb1=Label(frame1,text="Player 1 with O:",font=("consolas",16),bg="lightblue",fg="black")
lb1.grid(row=0,column=0,pady=10)

lb2=Label(frame1,text="Player 2 with X:",font=("consolas",16),bg="lightblue",fg="black")
lb2.grid(row=1,column=0)

ent1=Entry(frame1,bg="white",fg="black",font=("consolas",15),width=20)
ent1.grid(row=0,column=1,pady=10)
        
ent2=Entry(frame1,bg="white",fg="black",font=("consolas",15),width=20)
ent2.grid(row=1,column=1)

set_but=Button(win,text="All Set Click Here To Go...",font=("consolas",12),bg="lightyellow",fg="black",command=player_set)
set_but.pack(pady=5)

main=Frame(win,bg="lightcyan")
main.pack()

but1=Button(main,textvariable=a7,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(7))
but1.grid(row=0,column=0,padx=10,pady=10)

but2=Button(main,textvariable=a8,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(8))
but2.grid(row=0,column=1,padx=10,pady=10)

but3=Button(main,textvariable=a9,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(9))
but3.grid(row=0,column=2,padx=10,pady=10)

but4=Button(main,textvariable=a4,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(4))
but4.grid(row=1,column=0,padx=10,pady=10)

but5=Button(main,textvariable=a5,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(5))
but5.grid(row=1,column=1,padx=10,pady=10)

but6=Button(main,textvariable=a6,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(6))
but6.grid(row=1,column=2,padx=10,pady=10)

but7=Button(main,textvariable=a1,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(1))
but7.grid(row=2,column=0,padx=10,pady=10)

but8=Button(main,textvariable=a2,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(2))
but8.grid(row=2,column=1,padx=10,pady=10)

but9=Button(main,textvariable=a3,font=("bahnscrift semibold",20),bg="white",fg="GREEN",command=lambda:val_upd(3))
but9.grid(row=2,column=2,padx=10,pady=10)

lab3=Label(win,text="Result of the Game:",font=("bahnscrift semibold",15),bg="lightblue",fg="blue")
lab3.pack(pady=30)

txt=Entry(win,textvariable=stats,font=("bahnscrift semibold",16),width=35,bg="black",fg="YELLOW")
txt.pack()

inst=Button(win,text="INSTRUCTION",font=("bahnscrift semibold",16),bg="lightgreen",fg="green",command=instruction)
inst.pack(side=LEFT,padx=10,pady=5)

clear=Button(win,text="CLEAR",font=("bahnscrift semibold",16),bg="lightgreen",fg="green",command=clear)
clear.pack(side=LEFT,padx=10,pady=5)

end_=Button(win,text="END GAME",font=("bahnscrift semibold",16),bg="lightgreen",fg="green",command=lambda: win.destroy())
end_.pack(side=LEFT,padx=10,pady=5)

win.mainloop()
