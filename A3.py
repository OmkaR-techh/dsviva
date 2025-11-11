class TextEditor:
    def __init__(self):
        
      self.undos=[]
      self.redos=[]
      self.currentext=""
    def display(self):
        print(f"\n Current text:{self.currentext} ")
    def makechange(self):
        self.undos.append(self.currentext)
        change=input("enter text to add :")
        self.redos.clear()
        self.currentext+=" "+change
        self.display()
    def undo(self):
        if self.undos:
          self.redos.append(self.currentext)
          self.currentext=self.undos.pop()
          print("undo successful")
        else:
          print("nothing to undo")
        self.display()
    def redo(self):
        if self.redos: 
            self.undos.append(self.currentext)
            self.currentext=self.redos.pop()
            print("redo successful")
        else:
            print("nothing to undo")
        self.display()

if __name__=="__main__":
   TextEditor1=TextEditor()

   while True:
        print("welcome to over text editor")
        print("1.makechange") 
        print("2.display")
        print("3.undo")
        print("4.redo")
        print("5.exit")
        value=int(input("choose any option"))
        if value==1:
            TextEditor1.makechange()
        elif value==2:
            TextEditor1.display()
        elif value==3:
            TextEditor1.undo()
        elif value==4:
            TextEditor1.redo()
        elif value==5:
            print("exiting the text editor")
            break
        else:
            print("invalid input")
          
      




   
