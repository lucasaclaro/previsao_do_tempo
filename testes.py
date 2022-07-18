from tkinter import *
master = Tk()
master.geometry('490x560+650+200')
master.title('Previsão do tempo')
img_sol = PhotoImage(file='sol.png')
label_sol = Label(master, image=img_sol)
label_sol.place(width=300, height=200, x=100, y=330)
label_sol.pack()






master.mainloop()
