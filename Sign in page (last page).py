from tkinter import * #import tkinter
import random


signinpage = Tk()
signinpage.title("Mutts' Sign in")
signinpage.configure(background='orange')
signinpage.geometry('575x550')

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