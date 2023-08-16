from tkinter import *
window=Tk()

window.title('GUI Calculator')
window.geometry("380x400")
window.configure(bg='pink')

app_label=Label(window, text="GUI CALCULATOR", fg = "black", bg = "pink", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle_label=Label(window, text="Principal", fg = "black", bg = "pink", font=("Calibri", 12),bd=1)
principle_label.place(x=20, y=90)

principle=Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)

ROR_label=Label(window, text="Enter The rate of return", fg = "black", bg = "pink", font=("Calibri", 12),bd=1)
ROR_label.place(x=20, y=140)

ROR_entry=Entry(window, text="", bd=2, width=15)
ROR_entry.place(x=150, y=142)

time_label=Label(window, text="Enter time", fg = "black", bg = "pink", font=("Calibri", 12),bd=1)
time_label.place(x=20, y=185)

time_entry=Entry(window, text="", bd=2, width=15)
time_entry.place(x=150, y=187)

calculate_button=Button(window, text="Calculate", fg = "black", bg = "pink", bd=4, command=calculate_gui)
calculate_button.place(x=20, y=250)

result_frame = LabelFrame(window,text="Result", bg = "pink", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "pink", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

def calculate_gui():
  p=float(principle.get())
  r=float(ROR_entry.get())
  t=float(time_entry.get())
  i=(p*r*t)/100
  i=round(i,2)
  result_label.destroy()
  
  message =()
  output_message=Label(result_frame,"your GUI is"+str(i)+"and"+message,bg="pink",font=("calibri",12),width=42)          
  output_message.place(x=20, y=40)
  output_message.pack()
      
window.mainloop()