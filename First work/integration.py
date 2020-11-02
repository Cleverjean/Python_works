from tkinter import *

def addvar(first_input, second_input, myText):
    try:
        first_to_float = float(first_input.get())
        sec_to_float = float(second_input.get())
    except:
        myText.set('You have entered an invalid input.')
    else:
        result = first_to_float + sec_to_float
        myText.set(result)
        
def hello_world():
    newWindow = Toplevel(top)
    newWindow.title('First program')
    newWindow.geometry('250x100')
    Label(newWindow, text="Hello World").pack()

def add_floats():
    float_window = Toplevel(top)
    float_window.title('Add floats')
    float_window.geometry('400x100')
    myText = StringVar()
    
    Label(float_window, text='Enter a first number: ').grid(row=0)
    Label(float_window, text='Enter a second number: ').grid(row=1)
    Label(float_window, text='Fucking result!: ').grid(row=2, column=0)
    Label(float_window, text='', textvariable=myText).grid(row=2, column=1)
    
    first_input = Entry(float_window)
    second_input = Entry(float_window)

    first_input.grid(row=0, column=1)
    second_input.grid(row=1, column=1)

    submit = Button(float_window, text="Submit", command=lambda : addvar(first_input, second_input, myText))
    submit.grid(row=3, column=2)

def createFibo(length,myText):
    A = 0
    B = 1
    C = 0
    temp = []
    for x in range(int(length.get())):
        temp.append(A)
        A = A + B
        B = C
        C = A
    myText.set(temp)

def fibo():
    float_window = Toplevel(top)
    float_window.title('Fibo fucking nnaci series')
    float_window.geometry('350x100')
    myText = StringVar()

    Label(float_window, text='Enter a length for the fibo: ').grid(row=0)
    Label(float_window, text='Fucking result: ').grid(row=1, column=0)
    Label(float_window, text='', textvariable=myText).grid(row=1, column=1)
    
    length = Entry(float_window)
    length.grid(row=0, column=1)

    submit = Button(float_window, text="Submit", command=lambda : createFibo(length,myText))
    submit.grid(row=3, column=2)

top = Tk(className='My first python GUI')
top.geometry('300x100')

can = Canvas(top)
can.place(relx=200, rely=200, anchor=NW)

b = Button(top, text="Hello world", width='15', command=hello_world)
b_second = Button(top, text="Add two floats", width='15', command=add_floats)
b_third = Button(top, text="Fibonnaci series", width='15', command=fibo)

b.pack()
b_second.pack()
b_third.pack()
top.mainloop()
