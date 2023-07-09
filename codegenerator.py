from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_characters
    password_length=int(lengthsb.get())

    if choice.get()==1:
        passwordfield.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordfield.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordfield.insert(0,random.sample(all,password_length))

    #password=random.sample(all,password_length)
    #passwordfield.insert(0,password)

def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)

#creating object
root=Tk()
#for background color
root.config(bg='gray20')

#defining variable choice and font
choice=IntVar()
Font=('arial',15,'bold')

#creating label password
passwordlb=Label(root,text='Password Generator',font=('times new roman',22,'bold'),bg='gray20',fg='white')
#to place label on the screen
passwordlb.grid(pady=10)

#for weak
#creating radio button
weakrb=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
#to place radio button on the screen
weakrb.grid(pady=5)

#for medium
#creating radio button
mediumrb=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
#to place radio button on the screen
mediumrb.grid(pady=5)

#for strong
#creating radio button
strongrb=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
#to place radio button on the screen
strongrb.grid(pady=5)

#creating label password length
lengthlb=Label(root,text='Password length',font=('arial',13,'bold'),bg='gray20',fg='white')
#to place label on the screen
lengthlb.grid()

#creating spinbox for length
lengthsb=Spinbox(root,from_=5,to_=18,width=5,font=Font)
lengthsb.grid()

#creating button generate
generateb=Button(root,text='Generate',font=Font,command=generator)
generateb.grid(pady=5)

#creating password field 
passwordfield=Entry(root,width=25,bd=2,font=Font)  #bd for border
passwordfield.grid()

#creating button copy
copyb=Button(root,text='Copy',font=Font,command=copy)
copyb.grid(pady=5)

#to remain in the loop
root.mainloop()