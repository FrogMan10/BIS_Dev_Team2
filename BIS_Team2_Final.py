from tkinter import * #import tkinter


#Beginning of the homepage
homepage = Tk()
homepage.title("Mutts' Home Page")
homepage.configure(background='orange')


button_location=Button(homepage, text='Location')
button_events=Button(homepage, text='Events')
button_menu=Button(homepage, text='Menu')
button_merchandise=Button(homepage, text='Merchandise')

button_location.grid(row=1, column=0, )
button_events.grid(row=1, column=2)
button_menu.grid(row=1, column=3)
button_merchandise.grid(row=1, column=4)

photo1 = PhotoImage(file='C:\\Mutts.png')

homepage.mainloop()
