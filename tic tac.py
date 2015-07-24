from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createbuttons(self):
        for x in xrange(0,9):
            self.button = Button(self)
            self.button["text"] = "     "
            self.button["command"] =  self.quit
            self.button.pack({"side": "left"})
            self.button.grid(row=x, column=0)
            for i in xrange()

    Buttons = ()

   # def pressButton(self):
    #    changevalue()
     #   checkWin()
      #  nextTurn()

  #  def checkWin(self):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createbuttons()

root = Tk()
app = Application(master=root)
app.mainloop()

root.destroy()

