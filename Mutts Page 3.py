
from tkinter import * # Import tkinter
import random   #import random for Order Numbers
def checkdata():
    if cardholder.get() == '':
        Mess1.set('This is a required field. Please fill in this field.')
    elif cardholder.get() != '':
        Mess1.set('')
    if option.get() == 'Credit/Debit':
        Mess2.set('Please choose your payment method.')
    elif option.get() != 'Credit/Debit':
        Mess2.set('')
    listcardnumber = list(cardnumber.get())
    for i in listcardnumber:
        try:
            number = int(i)
            pass
        except ValueError:
            Mess3.set('The card number could not contain string.')
        if 0 < number < 9: 
            if len(listcardnumber) == 0:
                Mess3.set('This is a required field. Please enter your card number.')
            elif len(listcardnumber) != 16:
                Mess3.set('Please enter 16-digit card number')
            elif len(listcardnumber) == 16:
                Mess3.set('')
    if exp_date.get() == '':
        Mess5.set('This is a required field. Please enter your card expiration date')
    elif exp_date.get() != '':
        Mess5.set('')
    code = list(cvv.get())
    for t in code:
        try:
            newcode = int(t)
            pass
        except ValueError:
            Mess4.set('CVV code can not have string')
        if 0 < newcode < 9:
            if len(code) == 0:
                Mess4.set('This is a required field. Please enter your cvv code number.')
            elif len(code) != 3:
                Mess4.set('Please enter 3-digit CVV code')
            elif len(code) == 3:
                Mess4.set('')
    if address1.get() == '':
        Mess6.set('This is a required field. Please enter your billing address')
    elif exp_date.get() != '':
        Mess6.set('') 
    if state.get() == 'State':
        Mess7.set('This is a required field. Please choose a state')
    elif exp_date.get() != 'State':
        Mess7.set('')
    if city.get() == '':
        Mess8.set('This is a required field. Please enter your city')
    elif city.get() != '':
        Mess8.set('')
    if zipcode.get() == '':
        Mess9.set('This is a required field. Please enter your zipcode')
    elif zipcode.get() != '':
        Mess9.set('')
        Mess.set('Payment confirmed')
    
payment=Tk()
payment.geometry('560x620')
payment.title("Payment Method") 
payment.configure(background='orange')
pic = PhotoImage(file=
"D:\\Mutts.png")
pic = pic.zoom(20,5) 
pic = pic.subsample(46,15)
Label(payment, image = pic, background='orange').grid(row=0, column = 0, sticky = W+E)
Label(payment, text = ' ', background='orange').grid(row=2, column= 2)
Label(payment, text = 'Payment ', background='orange', font = 1000).grid(row=1, column= 2, sticky = W)
Label(payment, text = ' ', background='orange').grid(row=2, column= 2)
Label(payment, text = 'Payment Method', background='orange').grid(row=4, column=1, sticky = W)
Label(payment, text = '', background='orange').grid(row=3)
Label(payment, text = 'Cardholder Name ', background='orange').grid(row=2, column=1, sticky=W)
Label(payment, text = '', background='orange').grid(row=5)
Label(payment, text = 'Card Number',background='orange').grid(row=6, column=1, sticky=W)
Label(payment, text = '', background='orange').grid(row=7)
Label(payment, text = 'Expiration date',background='orange').grid(row=8, column=1, sticky=W)
Label(payment, text = '', background='orange').grid(row=9)
Label(payment, text = 'CVV code',background='orange').grid(row=10, column=1, sticky=W )
Label(payment, text = '', background='orange').grid(row=11)
Label(payment, text = '', background='orange').grid(row=12)
Label(payment, text = 'Billing Address',background='orange').grid(row=13, column=1, sticky=W )
Label(payment, text = '', background='orange').grid(row=15)
Label(payment, text = 'State',background='orange').grid(row=16, column=1, sticky=W )
Label(payment, text = '', background='orange').grid(row=17)
Label(payment, text = 'City', background='orange').grid(row=18, column = 1, sticky = W)
Label(payment, text = '', background='orange').grid(row=19)
Label(payment, text = 'Zip code', background='orange').grid(row=20, column = 1, sticky = W)
option = StringVar()
# Dictionary with options
choices = {'Credit','Debit'}
option.set('Credit/Debit') # set the default option
popupMenu = OptionMenu(payment, option, *choices)
popupMenu.configure(bg = 'white')
popupMenu.grid(row = 4, column = 2, sticky = W)

cardholder = StringVar()
Entry(payment, textvariable = cardholder, justify = LEFT, background='white').grid(row=2, column = 2, sticky = W)

cardnumber = StringVar()
number = Entry(payment, textvariable = cardnumber, justify = LEFT, background='white').grid(row=6, column = 2,sticky = W)

exp_date = StringVar()
Entry(payment, textvariable = exp_date, background='white').grid(row=8, column = 2,sticky = W)

cvv = StringVar()
Entry(payment, textvariable = cvv, justify = LEFT, background='white').grid(row=10, column = 2, sticky = W)

address1 = StringVar()
Entry(payment, textvariable = address1, justify = LEFT, background='white').grid(row=13, column = 2,sticky = W)

address2 = StringVar()
Entry(payment, textvariable = address2, justify = LEFT, background='white').grid(row=14, column = 2, sticky = W)

state = StringVar()
state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]
state.set('State')
available_states = OptionMenu(payment, state, *state_names)
available_states.configure(width = 9)
available_states.grid(row = 16, column =2, sticky = W)

city = StringVar()
Entry(payment, textvariable = city, justify = LEFT, background = 'white').grid(row = 18, column = 2, sticky = W)

zipcode = StringVar()
Entry(payment, textvariable = zipcode, justify = LEFT, background = 'white').grid(row = 20, column = 2, sticky = W)

Mess1= StringVar()
Label(payment, textvariable = Mess1, background='orange', fg = 'red').grid(row = 3, column = 2, columnspan=2, sticky = W)

Mess2= StringVar()
Label(payment, textvariable = Mess2, background='orange', fg = 'red').grid(row = 5, column = 2, columnspan=2, sticky = W)

Mess3= StringVar()
Label(payment, textvariable = Mess3, background='orange', fg = 'red').grid(row = 7, column = 2, columnspan=2, sticky = W)

Mess4= StringVar()
Label(payment, textvariable = Mess4, background='orange', fg = 'red').grid(row = 11, column = 2, columnspan=2, sticky = W)

Mess5= StringVar()
Label(payment, textvariable = Mess5, background='orange', fg = 'red').grid(row = 9, column = 2, columnspan=2, sticky = W)

Mess6= StringVar()
Label(payment, textvariable = Mess6, background='orange', fg = 'red').grid(row = 15, column = 2, columnspan=2, sticky = W)

Mess7= StringVar()
Label(payment, textvariable = Mess7, background='orange', fg = 'red').grid(row = 17, column = 2, columnspan=2, sticky = W)

Mess8= StringVar()
Label(payment, textvariable = Mess8, background='orange', fg = 'red').grid(row = 19, column = 2, columnspan=2, sticky = W)

Mess9= StringVar()
Label(payment, textvariable = Mess9, background='orange', fg = 'red').grid(row = 21, column = 2, columnspan=2, sticky = W)

Mess = StringVar()
Label(payment, textvariable = Mess, background='orange', fg = 'red').grid(row = 23, column = 2, columnspan=2, sticky = W)

Button(payment, text = 'Submit Payment', command = checkdata).grid(row = 22, column = 2)
payment.mainloop()