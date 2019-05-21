from tkinter import *
import time


def Main():

    global  root
    root=Tk()
    root.title("StopWatch")

    width=600
    height=200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    top=Frame(root,width=600)
    top.pack(side=TOP)
    bottom=Frame(root,width=600)
    bottom.pack(side=BOTTOM)
    stopWatch = StopWatch(root)
    stopWatch.pack(side=TOP)


    start=Button(bottom,padx=25,text='Start',height=2,bg='white',command=stopWatch.Start,fg='orange',font=('arial',9,'bold'))
    start.pack(side=LEFT)

    stop=Button(bottom,padx=25,text='Stop',width=4,height=2,bg='white',command=stopWatch.Stop,fg='orange',font=('arial',9,'bold'))
    stop.pack(side=LEFT)

    reset=Button(bottom,padx=25,text='Reset',width=4,height=2,bg='white',command=stopWatch.Reset,fg='orange',font=('arial',9,'bold'))
    reset.pack(side=LEFT)

    close=Button(bottom,padx=25,text='Close',width=4,height=2,bg='white',command=stopWatch.Exit,fg='orange',font=('arial',9,'bold'))
    close.pack(side=LEFT)

    txt=Label(top,pady=10,font=('arial',15,'bold'),bg='powder blue',fg='orange',text='StopWatch for beginner !!')
    txt.pack(fill=X)
    root.config(bg='powder blue')
    root.mainloop()





class StopWatch(Frame):

    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime = 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()

    def MakeWidget(self):
        timeText = Label(self, textvariable=self.timestr, font=("times new roman", 50), fg="white", bg="powder blue")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady=2, padx=2)

    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, miliSeconds))

    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1

    def Stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0

    def Exit(self):
            root.destroy()
            exit()

    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)


if __name__ == '__main__':
    Main()

