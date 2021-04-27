from tkinter import * #import tkinter
from random import *


def open_cusinfo():
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




    def open_payment_page():
        def checkdata():
            if cardholder.get() == '':
                Mess1.set('This is a required field. Please fill in this field.')
            elif cardholder.get() != '':
                Mess1.set('')
            if option.get() == 'Credit/Debit':
                Mess2.set('Please choose your payment method.')
            elif option.get() != 'Credit/Debit':
                Mess2.set('')
            if cardnumber.get() == '':
                Mess3.set('This is a required field. Please enter your card number.')
            listcardnumber = list(cardnumber.get())
            for i in listcardnumber:
                try:
                    number = int(i)
                    pass
                except ValueError:
                    Mess3.set('The card number could not contain string.')
                if 0 < number < 9: 
                    if len(listcardnumber) != 16:
                        Mess3.set('Please enter 16-digit card number')
                    elif len(listcardnumber) == 16:
                        Mess3.set('')
            if exp_date.get() == '':
                Mess5.set('This is a required field. Please enter your card expiration date')
            elif exp_date.get() != '':
                Mess5.set('')
            if cvv.get() == '':
                Mess4.set('This is a required field. Please enter your cvv code number.')
            code = list(cvv.get())
            
            for t in code:
                try:
                    newcode = int(t)
                    pass
                except ValueError:
                    Mess4.set('CVV code can not have string')
                if 0 < newcode < 9:
                    if len(code) != 3:
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

        def open_confirm_page():
            def open_sign_in():
                signinpage = Toplevel()
                signinpage.title("Mutts' Sign in")
                signinpage.configure(background='orange')
                signinpage.geometry('575x550')
                Confirmpage.withdraw()

                #Frame 1 for logo and help text
                topframe=Frame(signinpage, bg='orange')
                topframe.pack()

                signin_logo = PhotoImage(file='C:\Mutts.png')
                resize_signin_logo = signin_logo.subsample(2, 2)
                signin_logo_label=Label(topframe, image=resize_signin_logo)
                signin_logo_label.grid(row=0, column=0, sticky=W)

                help_label=Label(topframe, text="Ask for help", fg='blue', bg='orange')
                help_label.grid(row=0, column=1, padx=340)

                #Frame 2 Used for outline
                middleframe=Frame(signinpage, bg='orange',  width=400, highlightbackground='black', highlightthickness=1)
                middleframe.pack(pady=(30,0))


                member_signin_label=Label(middleframe, text='Member Sign In', font=(None, 20), bg='orange')
                member_signin_label.pack(padx=90)

                email_address_label=Label(middleframe, text='Email Address', bg='orange')
                email_address_label.pack(pady=(20,0))

                email_entry=Entry(middleframe)
                email_entry.pack()

                password_label=Label(middleframe, text='Password', bg='orange')
                password_label.pack(pady=(10,0))

                password_entry=Entry(middleframe)
                password_entry.pack()

                signin_button=Button(middleframe, text='Sign in', bg='grey', fg='white', height=1, width=15)
                signin_button.pack(pady=(10,0))

                #Frame 3 for 'New here?' and 'Create Account'
                new_here_frame = Frame(middleframe, bg='orange')
                new_here_frame.pack(pady=(20,0))

                new_here_label = Label(new_here_frame, bg='orange', text='New Here?')
                new_here_label.grid(row=0, column=0)

                create_acct_label = Label(new_here_frame, bg='orange', text='Create Account', fg='blue')
                create_acct_label.grid(row=0, column=1)

                forgot_password = Label(middleframe, bg='orange', text='Forgot Password?', fg='Blue')
                forgot_password.pack()

                #Frame 4 Contact us 
                bottomframe=Frame(signinpage, background='orange')
                bottomframe.pack(pady=50)

                contact_us = Label(bottomframe, bg='orange', text='Contact Us', fg='blue')
                contact_us.pack()

                signinpage.mainloop()


            Confirmpage = Toplevel()
            Confirmpage.title("Mutts' Confirmation Page")
            Confirmpage.configure(background='orange')
            Confirmpage.geometry('420x475')
            payment.withdraw()

            #Frame 1 Banner at top of page
            frame1 = Frame(Confirmpage, bg='orange')
            frame1.pack()

            outline=Frame(frame1, bg='black')
            outline.pack(pady=15)

            thankyou_label=Label(outline, background="white", text='Thank You For Signing Up!', font=(None, 25))
            thankyou_label.grid(row=0, column=2, pady=2, padx=2)


            #Frame 2 Mutts' Logo
            frame2 = Frame(Confirmpage, bg='orange')
            frame2.pack()

            logo = PhotoImage(file='C:\Mutts.png')
            resize_logo = logo.subsample(2,2)
            logo_label=Label(frame2, image=resize_logo)
            logo_label.pack()


            #Frame 3 Pass Type and Order Confirmation Number 
            frame3 = Frame(Confirmpage, bg='orange')
            frame3.pack(pady=10)

            pass_type=Label(frame3, bg='orange', text='Pass type purchased:')
            pass_type.grid(row=0, column=0, sticky=W)

            pass_type_answer=Label(frame3, bg='orange', text='**Needs Functionality**')
            pass_type_answer.grid(row=0, column=1)

            order_confirm_text=Label(frame3, bg='orange', text='Order confirmation number:')
            order_confirm_text.grid(row=1, column=0, sticky=W)

            order_confirm_number=Label(frame3, bg='orange', text='**Needs functionality')
            order_confirm_number.grid(row=1, column=1)


            #Frame 4 Both Buttons
            frame4 = Frame(Confirmpage, bg='orange') 
            frame4.pack()

            back_button = Button(frame4, text='Return to homepage', height=1, width=18, bg='grey', fg='white')
            back_button.grid(row=1, column=1, pady=4)

            create_acct_button = Button(frame4, text='Create Account', height=1, width=18, bg='grey', fg='white', command=open_sign_in)
            create_acct_button.grid(row=1, column=2, padx=16)


            #Frame 5 Last picture
            frame5 = Frame(Confirmpage, bg='orange')
            frame5.pack(pady=(20,0))

            chairphoto = PhotoImage(file='C:\dogsonchair.png')
            resize_picture2 = chairphoto.subsample(1,1)
            picture2_label=Label(frame5, image=resize_picture2)
            picture2_label.pack()

            Confirmpage.mainloop()

        payment=Toplevel()
        payment.geometry('560x620')
        payment.title("Payment Method") 
        payment.configure(background='orange')
        CusInfo.withdraw()

        pic = PhotoImage(file=
        "C:\\Mutts.png")
        pic = pic.zoom(20,5) 
        pic = pic.subsample(46,15)
        Label(payment, image = pic, background='orange').grid(row=0, column = 0, sticky = W+E)
        Label(payment, text = ' ', background='orange').grid(row=2, column= 2, columnspan = 3)
        Label(payment, text = 'Payment ', background='orange', font = 5000).grid(row=1, column= 2, columnspan = 1, sticky = W)
        Button(payment, text = 'Ask for help ?', background='orange', fg = 'blue', bd = 0, highlightthickness=0).grid(row=24, column= 2, sticky = W)
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
        popupMenu.configure(bg = 'white', width = 13, highlightthickness = 1)
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
        available_states.configure(width = 13, bg = 'white', highlightthickness = 1)
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

        Button(payment, text="Next Page", command = open_confirm_page).grid(row=22, column=3)

        payment.mainloop()

    CusInfo=Toplevel()
    CusInfo.geometry('600x690')
    CusInfo.title("Customer Information") 
    CusInfo.configure(background='orange')
    homepage.withdraw()

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
    SpayedNeutered.set('Are all of your dogs spayed or neutured?')
    available_options2 = OptionMenu(CusInfo, SpayedNeutered, *options2)
    available_options2.configure(width = 40, bg = 'white', highlightthickness = 1)
    available_options2.grid(row = 22, column = 2, sticky = W)

    shots = StringVar()
    options3 = {'Yes', 'No'}
    shots.set('Are all dogs up to date on shots?')
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
    Button(CusInfo, text = 'Next', justify = LEFT, bg = 'white', command = open_payment_page).grid(row = 26, column = 3, sticky = W)
    CusInfo.mainloop()

            
#Beginning of the homepage
homepage = Tk()
homepage.title("Mutts' Home Page")
homepage.configure(background='white')
homepage.geometry('552x575')

frame1=Frame(homepage, background='orange')
frame1.grid(row=0, column=0, sticky=W)

button_location=Button(frame1, text='Location')
button_events=Button(frame1, text='Events')
button_menu=Button(frame1, text='Menu')
button_merchandise=Button(frame1, text='Merchandise')

button_location.grid(row=1, column=0, sticky=NW)
button_events.grid(row=1, column=2, sticky=NW)
button_menu.grid(row=1, column=3, sticky=NW)
button_merchandise.grid(row=1, column=4, sticky=NW)

photo1 = PhotoImage(file='C:\Mutts.png')
resize_photo1 = photo1.subsample(3, 3)
pic_label=Label(frame1, image=resize_photo1)
pic_label.grid(row=1, column=5, sticky=NW)

button_membership=Button(frame1,text="Membership Sign in")
button_membership.grid(row=1, column=6, padx=(113,0), sticky=N)

#Frame 2
frame2=Frame(homepage, background='white')
frame2.grid(row=1, column=0)

photo2 = PhotoImage(file='C:\littledog.png')
resize_photo2 = photo2.subsample(2, 2)
pic_label2=Label(frame2, image=resize_photo2)
pic_label2.grid(row=1, column=1)


welcomelabel=Label(frame2, text='Welcome to Mutts!', background='white', width='15', height='4',font=(None, 30))
welcomelabel.grid(row=1, column=2)

photo3 = PhotoImage(file='C:\labrador.png')
resize_photo3 = photo3.subsample(2, 2)
pic_label3=Label(frame2, image=resize_photo3)
pic_label3.grid(row=1, column=3)

#Frame 3 For Daily Pass
frame3=Frame(homepage, bg='orange')
frame3.grid(row=2, column=0, padx=(0,300))

insideframe3=Frame(frame3, background='white')
insideframe3.grid(row=0, column=0, padx=10, pady=10)

text_daypass=Label(insideframe3, text='Day Pass\n\nPrice\n\n$9.95', font='20')
text_daypass.grid(row=0, column=0, pady=30)

button_dailypass=Button(insideframe3, text='Purchase\nDaily Pass', command=open_cusinfo)
button_dailypass.grid(row=1, column=0, pady=(17,0), padx=27)

help_dailypass=Label(insideframe3, fg='blue', text='More info')
help_dailypass.grid(row=2, column=0)

#Frame 4 For Monthly Pass
frame4=Frame(homepage, bg='orange')
frame4.grid(row=2, column=0)

insideframe4=Frame(frame4, background='white')
insideframe4.grid(row=0, column=0, padx=10, pady=10)

monthly_daypass=Label(insideframe4, text='Monthly Pass\n\nPrice\n\n$16.95', font='20')
monthly_daypass.grid(row=0, column=0, pady=30)

button_monthlypass=Button(insideframe4, text='Purchase\nMonthly Pass', command=open_cusinfo)
button_monthlypass.grid(row=1, column=0, pady=(17,0), padx=20)

help_monthlypass=Label(insideframe4, fg='blue', text='More info')
help_monthlypass.grid(row=2, column=0)

#Frame 5 for Yearly Pass
frame5=Frame(homepage, bg='orange')
frame5.grid(row=2, column=0, padx=(300,0))

insideframe5=Frame(frame5, background='white')
insideframe5.grid(row=0, column=0, padx=10, pady=10)

yearly_daypass=Label(insideframe5, text='Yearly Pass\n\nPrice\n\n$169.95', font='20')
yearly_daypass.grid(row=0, column=0, pady=30)

button_yearlypass=Button(insideframe5, text='Purchase\nYearly Pass', command=open_cusinfo)
button_yearlypass.grid(row=1, column=0, pady=(17,0), padx=24)

help_yearlypass=Label(insideframe5, fg='blue', text='More info')
help_yearlypass.grid(row=2, column=0)

#Frame 6 Contact us & FAQ
frame6=Frame(homepage)
frame6.grid(row=3, column=0)

contactus_label=Label(frame6, text='Contact Us     FAQ', fg='blue')
contactus_label.grid(row=0, column=0, pady=(20,0))


homepage.mainloop()
        


