import tkinter
import tkintermapview 
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
Label1 = Label(text="Phone Number Tracker")
Label1.pack()


def getResult():
    num = number.get("1.0",END)
    num1 = phonenumbers.parse(num)

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    result.insert(END, "The country of this number is:" + location)
    result.insert(END, "The sim card of this number is:" + service_provider)


number = Text(height=1)
number.pack()

button = Button(text="Search")
button.pack(pady=10, padx=100)

result = Text(height=7)
result.pack()

root.mainloop()

