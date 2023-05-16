# from tkinter import *
# from time import strftime
# main_window=Tk()
# main_window.title('DigitalClock')
# main_window.geometry('630*135')
# main_window.minsize(630,135)
# main_window.maxsize(630,135)
# main_window.config(bg="black")
#
# def good_time():
#     cur_time=strftime("%I:%M:%S %p")
#     clock_label.config(text=cur_time)
#     clock_label.after(1000,good_time)
#
# clock_label=Label(main_window,text="DigitalClock",font=('Arial,80'),fg="green",padx=5,pady=5)
# clock_label.pack()
# good_time()
# main_window.mainloop()

from tkinter import *
from time import strftime

main_window=Tk()
main_window.title('DigitalClock')
main_window.geometry("100x50")
main_window.minsize(100,50)
main_window.maxsize(100,50)
main_window.config(bg="black")

def good_time():
    cur_time=strftime("%I:%M:%S %p")
    clock_label.config(text=cur_time)
    clock_label.after(1000,good_time)

clock_label=Label(main_window,text="DigitalClock",font=('Arial,100'),bg="black",fg="pink",padx=5,pady=5)
clock_label.pack()
good_time()

main_window.mainloop()



