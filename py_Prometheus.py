#import module
from tkinter import *

# initialize window
root = Tk()
canvas1 = Canvas(root, width=500, height=750)
canvas1.pack()
root.title('Mad Libs Generator')

# creates input fields for user to enter words
label1 = Label(root, text= 'Final Project Mad Libs Generator \n Enter your words below!' , font = ('helvetica', 20))
canvas1.create_window(250, 40, window=label1)

label2 = Label(root, text='Adverb:', font = ('helvetica', 15))
canvas1.create_window(150, 100, window=label2)

entry1 = Entry(root)
canvas1.create_window(300, 100, window=entry1)

label2 = Label(root, text='Noun:', font = ('helvetica', 15))
canvas1.create_window(150, 130, window=label2)

entry2 = Entry(root)
canvas1.create_window(300, 130, window=entry2)

label2 = Label(root, text='Liquid:', font = ('helvetica', 15))
canvas1.create_window(150, 160, window=label2)

entry3 = Entry(root)
canvas1.create_window(300, 160, window=entry3)

label2 = Label(root, text='Verb:', font = ('helvetica', 15))
canvas1.create_window(150, 190, window=label2)

entry5 = Entry(root)
canvas1.create_window(300, 190, window=entry5)

label2 = Label(root, text='Number:', font = ('helvetica', 15))
canvas1.create_window(150, 220, window=label2)

entry6 = Entry(root)
canvas1.create_window(300, 220, window=entry6)

label2 = Label(root, text='Noun(Plural):', font = ('helvetica', 15))
canvas1.create_window(150, 250, window=label2)

entry7 = Entry(root)
canvas1.create_window(300, 250, window=entry7)

label2 = Label(root, text='Verb:', font = ('helvetica', 15))
canvas1.create_window(150, 280, window=label2)

entry8 = Entry(root)
canvas1.create_window(300, 280, window=entry8)

label2 = Label(root, text='Adjective:', font = ('helvetica', 15))
canvas1.create_window(150, 310, window=label2)

entry9 = Entry(root)
canvas1.create_window(300, 310, window=entry9)

label2 = Label(root, text='Noun:', font = ('helvetica', 15))
canvas1.create_window(150, 340, window=label2)

entry10 = Entry(root)
canvas1.create_window(300, 340, window=entry10)

label2 = Label(root, text='Noun(Plural):', font = ('helvetica', 15))
canvas1.create_window(150, 370, window=label2)

entry11 = Entry(root)
canvas1.create_window(300, 370, window=entry11)

label2 = Label(root, text='Illness:', font = ('helvetica', 15))
canvas1.create_window(150, 400, window=label2)

entry12 = Entry(root)
canvas1.create_window(300, 400, window=entry12)

label2 = Label(root, text='Occupation:', font = ('helvetica', 15))
canvas1.create_window(150, 430, window=label2)

entry14 = Entry(root)
canvas1.create_window(300, 430, window=entry14)

label2 = Label(root, text='Body Part(Plural):', font = ('helvetica', 15))
canvas1.create_window(150, 460, window=label2)

entry15 = Entry(root)
canvas1.create_window(300, 460, window=entry15)

label2 = Label(root, text='Body Part:', font = ('helvetica', 15))
canvas1.create_window(150, 490, window=label2)

entry16 = Entry(root)
canvas1.create_window(300, 490, window=entry16)

# function that retrieves words and transfers them into the story
def generateMadLib():
    adverb=entry1.get()
    noun=entry2.get()
    liquid=entry3.get()
    verb=entry5.get()
    number=entry6.get()
    nounp=entry7.get()
    verb2=entry8.get()
    adjective=entry9.get()
    noun2=entry10.get()
    nounp2=entry11.get()
    illness=entry12.get()
    occupation=entry14.get()
    bodypartp=entry15.get()
    bodypart=entry16.get()

    label3 = Label(root, text= 'Here is your Mad Lib!', font = 'helvetica')
    canvas1.create_window(250, 580, window=label3)

    label4 = Label(root, text = ('In order to wash your face ' +adverb+ ' , you must wet your ' +noun+ ' in warm ' +liquid+'. \n Then, '+verb+' it across your face '+number+' times. This will wash off any remaining '+nounp+'. \n When you are done you should '+verb2+' the cloth in '+adjective+' water to clean it. \nYou should also wash your face with a '+noun2+' to keep it smooth and shiny. \n This will keep also keep away '+nounp2+'. Don`t worry. \n It is normal to experience '+illness+' the first time you try this. \n Consult your '+occupation+' if you break out in '+bodypartp+'. This works well on your '+bodypart+' too!'), font=('helvetica', 9))
    canvas1.create_window(250, 650, window=label4)

# button that calls the function to generate the completed story
button1 = Button(text='Generate  Lib!', command=generateMadLib, bg='red', fg='white', font=('helvetica', 9, 'bold'))
canvas1.create_window(250, 525, window=button1)

root.mainloop()