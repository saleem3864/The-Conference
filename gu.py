import time
from tkinter import *
from threading import Thread
from multiprocessing import Process
from tkinter import StringVar


def timer():
    def tim1():
        min =59
        hr=23
        sec=55
        while True:
            sec+=1
            if sec==60:
                min +=1
                sec=00
            if min==60:
                hr+=1
                min=00
            if hr==24:
                hr=00
            print(str(hr)+":"+str(min)+":"+str(sec))
            time.sleep(1)
    def tim2():
        min1 =59
        hr1=23
        sec1=55
        while True:
            sec1+=1
            if sec1==60:
                min1 +=1
                sec1=00
            if min1==60:
                hr1+=1
                min1=00
            if hr1==24:
                hr1=00
            print(str(hr1)+":"+str(min1)+":"+str(sec1))
            #var1.set(str(hr1)+":"+str(min1)+":"+str(sec1))
            time.sleep(1)
    thread1=Thread(target=tim1)
    thread2=Thread(target=tim2)
    thread1.start()
    thread2.start()
def Threader():
    print(var.get())
    if var.get() == "Run Process":
        var.set("Stop Process")
        all_process.append(Process(target=timer))
        all_process[0].start()
        var1.set("Process running Total are : "+str(len(all_process)))
        print(len(all_process))
    else :
        all_process[0].terminate()
        all_process.pop(0)
        var1.set("Process Stoped Total are : "+str(len(all_process)))
        var.set("Run Process")
        print(len(all_process))


    """print(str(all_process[0].is_alive()))
    all_process[0].terminate()
    all_process.append(Process(target=timer))
    print(all_process[len(all_process)-1].is_alive())
    all_process[len(all_process)-1].start()
    print(len(all_process))"""
if __name__ == '__main__':
    all_process=[]
    window = Tk()
    window.geometry("300x300")
    var = StringVar()
    var1 =StringVar()  # type: StringVar
    var1.set("NOT RUNNING YET...")
    var.set("Run Process")
    btn =Button(window,textvariable=var,command=Threader)
    btn.grid(column=10,row=10)
    lbl=Label(window,textvariable=var1)
    lbl.grid(column=10,row=15)
    window.mainloop()
