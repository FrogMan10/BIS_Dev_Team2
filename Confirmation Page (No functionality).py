from tkinter import * #import tkinter
import random


Confirmpage = Tk()
Confirmpage.title("Mutts' Confirmation Page")
Confirmpage.configure(background='orange')
Confirmpage.geometry('420x475')

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

create_acct_button = Button(frame4, text='Create Account', height=1, width=18, bg='grey', fg='white')
create_acct_button.grid(row=1, column=2, padx=16)


#Frame 5 Last picture
frame5 = Frame(Confirmpage, bg='orange')
frame5.pack(pady=(20,0))

chairphoto = PhotoImage(file='C:\dogsonchair.png')
resize_picture2 = chairphoto.subsample(1,1)
picture2_label=Label(frame5, image=resize_picture2)
picture2_label.pack()

Confirmpage.mainloop()