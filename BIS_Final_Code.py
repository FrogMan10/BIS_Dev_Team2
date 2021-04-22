from tkinter import * #import tkinter


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

button_dailypass=Button(insideframe3, text='Purchase\nDaily Pass')
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

button_monthlypass=Button(insideframe4, text='Purchase\nMonthly Pass')
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

button_yearlypass=Button(insideframe5, text='Purchase\nYearly Pass')
button_yearlypass.grid(row=1, column=0, pady=(17,0), padx=24)

help_yearlypass=Label(insideframe5, fg='blue', text='More info')
help_yearlypass.grid(row=2, column=0)

#Frame 6 Contact us & FAQ
frame6=Frame(homepage)
frame6.grid(row=3, column=0)

contactus_label=Label(frame6, text='Contact Us     FAQ', fg='blue')
contactus_label.grid(row=0, column=0, pady=(20,0))


homepage.mainloop()