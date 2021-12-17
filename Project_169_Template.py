
#create an application which generates dynamic elements like button, label and dropdown

from tkinter import * 
from tkinter import ttk

root = Tk()  
root.geometry("900x600") 
root.title("Classes")

gui_elements = ["Label", "Button", "Dropdown"]
dropdown = ttk.Combobox(root,state="readonly" ,values = gui_elements)
dropdown.pack()


class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label = Label(root,text ="A new label is been created using class", fg="red")
        label.pack() 

#deifne a function to create a button and write a text on it  as Button, call the function self.message
    def createButton(self):
        class_btn = Button(root,text="button",command=self.message)
        class_btn.pack(padx=20, pady = 10)


#deifne a function to create a dropdown createDropdown(self)
    def createDropdown(self):
        #create a list, name it value and pass values 1,2,3,4 in it
        list1=[1,2,3,4,5]
        
        
        #create a dropdown using ttk.Combobox, set it to root, and keep the state as readonly, pass the list for values
        class_dropdown = ttk.Combobox(root,state="readonly",values=list1)
        class_dropdown.pack()
        
#define a function choose(self) to choose between label, button or dropdown 
    def choose(self):
       global dropdown
       element=dropdown.get()
       if(element=="Label"):
           self.createLabel()
       elif(element=="Button"):
           self.createButton()
       elif(element=="Dropdown"):
           self.createDropdown()
           
        
        
#define a message to show the information when clicked                   
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class") 

        
#copy the last three lines of class activity, to create object, call the object.choose when the button is clicked
#complete the code
obj=CreateElements()

#create a button to create label and button when clicked, call the object when the button is clicked
btn = Button(root,text="Click to create label and button instantly",command=obj.choose)
btn.pack()

root.mainloop()