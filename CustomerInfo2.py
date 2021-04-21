from tkinter import * # Import tkinter
import random   #import random for Order Numbers

CusInfo=Tk()
CusInfo.geometry('450x600')
CusInfo.title("Customer Information") 
CusInfo.configure(background='orange')
pic = PhotoImage(file=
"C:\\Mutts.png")
pic = pic.zoom(20,5) 
pic = pic.subsample(46,15)
Label(CusInfo, image = pic, background='orange').grid(row=0, columnspan = 3, sticky = W+E)
Label(CusInfo, text = '', background='orange').grid(row=1, column=1)
Label(CusInfo, text = 'First Name*', background='orange').grid(row=4, column=1, sticky = W)
Label(CusInfo, text = '', background='orange').grid(row=3)
Label(CusInfo, text = 'Last Name*', background='orange').grid(row=2, column=1, sticky=W)
Label(CusInfo, text = '', background='orange').grid(row=5)
Label(CusInfo, text = 'Cell Number*',background='orange').grid(row=6, column=1, sticky=W)
Label(CusInfo, text = '', background='orange').grid(row=7)
Label(CusInfo, text = 'Email*',background='orange').grid(row=8, column=1, sticky=W)
Label(CusInfo, text = '', background='orange').grid(row=9)
Label(CusInfo, text = 'Number of Dogs(Up to 3)',background='orange').grid(row=10, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=11)
Label(CusInfo, text = '', background='orange').grid(row=12)
Label(CusInfo, text = 'Dog 1 Name *',background='orange').grid(row=13, column=1, sticky=W )
Label(CusInfo, text = 'Dog 2 Name',background='orange').grid(row=14, column=1, sticky=W )
Label(CusInfo, text = 'Dog 3 Name',background='orange').grid(row=15, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=16)
Label(CusInfo, text = 'Dog 1 Breed *',background='orange').grid(row=17, column=1, sticky=W )
Label(CusInfo, text = 'Dog 2 Breed', background='orange').grid(row=18, column=1, sticky=W )
Label(CusInfo, text = 'Dog 3 Breed', background='orange').grid(row=19, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=20)
Label(CusInfo, text = 'Spayed/Neutered*', background='orange').grid(row=21, column = 1, sticky = W)
Label(CusInfo, text = '', background='orange').grid(row=22)
Label(CusInfo, text = 'Shots Received*', background='orange').grid(row=23, column = 1, sticky = W)
Label(CusInfo, text = '', background='orange').grid(row=24)
option = StringVar()


firstname = StringVar()
Entry(CusInfo, textvariable = firstname, justify = LEFT, background='white').grid(row=4, column = 2, sticky = W)

lastname = StringVar()
number = Entry(CusInfo, textvariable = lastname, justify = LEFT, background='white').grid(row=2, column = 2,sticky = W)

cellnumber = StringVar()
Entry(CusInfo, textvariable = cellnumber, background='white').grid(row=6, column = 2,sticky = W)

email = StringVar()
Entry(CusInfo, textvariable = email, justify = LEFT, background='white').grid(row=8, column = 2, sticky = W)

numdogs = StringVar()
Entry(CusInfo, textvariable = numdogs, justify = LEFT, background='white').grid(row=10, column = 2,sticky = W)

dogname1 = StringVar()
Entry(CusInfo, textvariable = dogname1, justify = LEFT, background='white').grid(row=13, column = 2, sticky = W)

dogname2 = StringVar()
Entry(CusInfo, textvariable = dogname2, justify = LEFT, background='white').grid(row=14, column = 2, sticky = W)

dogname3 = StringVar()
Entry(CusInfo, textvariable = dogname3, justify = LEFT, background='white').grid(row=15, column = 2, sticky = W)

dogbreed1 = StringVar()
Entry(CusInfo, textvariable = dogname3, justify = LEFT, background='white').grid(row=17, column = 2, sticky = W)

dogbreed2 = StringVar()
Entry(CusInfo, textvariable = dogname3, justify = LEFT, background='white').grid(row=18, column = 2, sticky = W)

dogbreed3 = StringVar()
Entry(CusInfo, textvariable = dogname3, justify = LEFT, background='white').grid(row=19, column = 2, sticky = W)

spayNeuter = StringVar()
Entry(CusInfo, textvariable = spayNeuter, justify = LEFT, background = 'white').grid(row = 21, column = 2, sticky = W)

shots = StringVar()
Entry(CusInfo, textvariable = shots, justify = LEFT, background = 'white').grid(row = 23, column = 2, sticky = W)


Button(CusInfo, text = 'Confirm submission', justify = LEFT, bg = 'white'). grid(row = 25, column = 2, columnspan = 2, sticky = W)
Button(CusInfo, text = 'Previous', justify = LEFT, bg = 'white'). grid(row = 25, column = 1, sticky = W)

CusInfo.mainloop()