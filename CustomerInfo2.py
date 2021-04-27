from tkinter import * # Import tkinter
import random   #import random for Order Numbers
def datavalid():
    if lastname.get() == '':
        Alert1.set('This is the required field. Please enter your last name.')
    elif lastname.get() != '':
        Alert1.set('')
    if firstname.get() == '':
        Alert2.set('This is the required field. Please enter your first name.')
    elif firstname.get() != '':
        Alert2.set('')
    if cellnumber.get() == '':
        Alert3.set('This is a required field. Please enter your cellphone number.')
    cell = list(cellnumber.get())
    for t in cell:
        try:
            number = int(t)
            pass
        except ValueError:
            Alert3.set('The cellphone number could not contain string.')
        if 0 < number < 9: 
            if len(cell) != 0:
                Alert3.set('')
    if email.get() == '':
        Alert4.set('This is the required field. Please enter your email')
    elif '@' not in email.get():
        Alert4.set('Please enter the valid email adress. Sample: name@gmail.com')
    elif '@' in email.get():
        Alert4.set('')
    if numdogs.get() == 'Up to 3 dogs':
        Alert5.set('Please choose your number of dogs')
    if numdogs.get() != 'Up to 3 dogs':
        Alert5.set('')
    if dogname1.get() == '':
        Alert6.set('This is the required field. Please enter your dog\'s name.')
    elif dogname1.get() != '':
        Alert6.set('')
    if dogbreed1.get() == '':
        Alert7.set('This is the required field. Please enter your dog\'s breed.')
    elif dogbreed1.get() != '':
        Alert7.set('')
    if SpayedNeutered.get() == 'Are all of your dog spayed or neutured?':
        Alert8.set('Please choose one of the option in drop-down menu list')
    elif SpayedNeutered.get() != 'Are all of your dog spayed or neutured?':
       Alert8.set('') 
    if shots.get() == 'Are all of your dog recieved shots?':
        Alert9.set('Please choose one of the option in drop-down menu list')
    else:
        Alert9.set('')
        Alert10.set('Customer information comfirmed. Please go to next page')
    
        
CusInfo=Tk()
CusInfo.geometry('450x650')
CusInfo.title("Customer Information") 
CusInfo.configure(background='orange')
pic = PhotoImage(file=
"D:\\Mutts.png")
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
Label(CusInfo, text = 'Number of Dogs',background='orange').grid(row=10, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=11)
Label(CusInfo, text = 'Dog 1 Name *',background='orange').grid(row=12, column=1, sticky=W )
Label(CusInfo, text = 'Dog 2 Name',background='orange').grid(row=14, column=1, sticky=W )
Label(CusInfo, text = 'Dog 3 Name',background='orange').grid(row=15, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=16)
Label(CusInfo, text = 'Dog 1 Breed *',background='orange').grid(row=17, column=1, sticky=W )
Label(CusInfo, text = 'Dog 2 Breed', background='orange').grid(row=19, column=1, sticky=W )
Label(CusInfo, text = 'Dog 3 Breed', background='orange').grid(row=20, column=1, sticky=W )
Label(CusInfo, text = '', background='orange').grid(row=21)
Label(CusInfo, text = 'Spayed/Neutered*', background='orange').grid(row=22, column = 1, sticky = W)
Label(CusInfo, text = '', background='orange').grid(row=23)
Label(CusInfo, text = 'Shots Received*', background='orange').grid(row=24, column = 1, sticky = W)
Label(CusInfo, text = '', background='orange').grid(row=25)
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
options = {'1', '2', '3'}
numdogs.set('Up to 3 dogs')
available_options = OptionMenu(CusInfo, numdogs, *options)
available_options.configure(width = 13, bg = 'white', highlightthickness = 1)
available_options.grid(row = 10, column = 2, sticky = W)

dogname1 = StringVar()
Entry(CusInfo, textvariable = dogname1, justify = LEFT, background='white').grid(row=12, column = 2, sticky = W)

dogname2 = StringVar()
Entry(CusInfo, textvariable = dogname2, justify = LEFT, background='white').grid(row=14, column = 2, sticky = W)

dogname3 = StringVar()
Entry(CusInfo, textvariable = dogname3, justify = LEFT, background='white').grid(row=15, column = 2, sticky = W)

dogbreed1 = StringVar()
Entry(CusInfo, textvariable = dogbreed1, justify = LEFT, background='white').grid(row=17, column = 2, sticky = W)

dogbreed2 = StringVar()
Entry(CusInfo, textvariable = dogbreed2, justify = LEFT, background='white').grid(row=19, column = 2, sticky = W)

dogbreed3 = StringVar()
Entry(CusInfo, textvariable = dogbreed3, justify = LEFT, background='white').grid(row=20, column = 2, sticky = W)

SpayedNeutered = StringVar()
options2 = {'Yes', 'No'}
SpayedNeutered.set('Are all of your dog spayed or neutured?')
available_options2 = OptionMenu(CusInfo, SpayedNeutered, *options2)
available_options2.configure(width = 40, bg = 'white', highlightthickness = 1)
available_options2.grid(row = 22, column = 2, sticky = W)

shots = StringVar()
options3 = {'Yes', 'No'}
shots.set('Are all of your dog recieved shots?')
available_options3 = OptionMenu(CusInfo, shots, *options3)
available_options3.configure(width = 40, bg = 'white', highlightthickness = 1)
available_options3.grid(row = 24, column = 2, sticky = W)

Alert1 = StringVar()
Label(CusInfo, textvariable = Alert1, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 3, column = 2, sticky = W)


Alert2 = StringVar()
Label(CusInfo, textvariable = Alert2, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 5, column = 2, sticky = W)

Alert3 = StringVar()
Label(CusInfo, textvariable = Alert3, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 7, column = 2, sticky = W)

Alert4 = StringVar()
Label(CusInfo, textvariable = Alert4, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 9, column = 2, sticky = W)

Alert5 = StringVar()
Label(CusInfo, textvariable = Alert5, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 11, column = 2, sticky = W)

Alert6 = StringVar()
Label(CusInfo, textvariable = Alert6, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 13, column = 2, sticky = W)

Alert7 = StringVar()
Label(CusInfo, textvariable = Alert7, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 18, column = 2, sticky = W)

Alert8 = StringVar()
Label(CusInfo, textvariable = Alert8, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 23, column = 2, sticky = W)

Alert9 = StringVar()
Label(CusInfo, textvariable = Alert9, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 25, column = 2, sticky = W)

Alert10 = StringVar()
Label(CusInfo, textvariable = Alert10, justify = LEFT, bg = 'orange', fg = 'red'). grid(row = 27, column = 2, sticky = W)

Button(CusInfo, text = 'Confirm submission', justify = LEFT, bg = 'white', command = datavalid). grid(row = 26, column = 2, columnspan = 2, sticky = W)
Button(CusInfo, text = 'Previous', justify = LEFT, bg = 'white'). grid(row = 26, column = 1, sticky = W)
Button(CusInfo, text = 'Next', justify = LEFT, bg = 'white').grid(row = 26, column = 3, sticky = W)
CusInfo.mainloop()