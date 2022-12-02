import tkinter


window=tkinter.Tk()
window.title("Convert Milles to Km")
window.config(padx=20,pady=20)
#window.config(padx=100,pady=20)

#is equal to (label)
my_label=tkinter.Label(text="is equal to", font=("Arial",10,"bold"))
my_label.grid(column=0,row=1)

#input miles
input=tkinter.Entry(width=7)
input.grid(column=1,row=0)


def button_clicked():
    input_entry=input.get()
    my_label["text"]=float(input_entry)*1.6




#is equal to (label)
my_label=tkinter.Label(text="0", font=("Arial",10,"bold"))
my_label.grid(column=1,row=1)


#button2
button = tkinter.Button(text="Calculate",command=button_clicked)
# arranging button widgets
button.grid(column=1, row=2)

#is equal to (label)
my_label_miles=tkinter.Label(text="Miles", font=("Arial",10,"bold"))
my_label_miles.grid(column=2,row=0)


#is equal to (label)
my_label_km=tkinter.Label(text="Km", font=("Arial",10,"bold"))
my_label_km.grid(column=2,row=1)


window.mainloop()
