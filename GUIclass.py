import tkinter as tk
from tkinter import messagebox
import functions
import readCSV


#Class for GUI application
class GUIclass:
    
    
    #constructor 
    def __init__(self):
      self.root = tk.Tk()
      self.root.geometry("900x400")
      self.root.title("Keele Library System")
      self.label = tk.Label(self.root,text="Welcome to Keele University Library System", font=('Times New Roman',20),fg="#191970")
      self.label.grid(row=0,column=1,columnspan=3)
      self.frame = tk.Frame(self.root, width=50, height=20)
      self.frame.grid(sticky=tk.W,row=0,column=0)
      img = tk.PhotoImage(file=("keele2.png"))
      self.label1=tk.Label(self.frame,image=img,)
      self.label1.grid(sticky=tk.W,row=0,column=0)
      
      
      
     #function to create Screen for subject user input
      def subjectScreen():
        try:    
            self.labl=tk.Label(self.root,text="Please enter a subject(part/full)",font=("calibri",13))
            self.labl.grid(row=1,column=0,sticky=tk.W)
            self.enter=tk.Entry(self.root,bd=2)
            self.enter.grid(row=1,column=1,sticky=tk.W)
            self.enter.focus()
            hidecanvas()
            self.btn = tk.Button(self.root,text="Search",command=SubjectshowResult)
            self.btn.grid(row=3,column=1,sticky=tk.S)
            self.btn1 = tk.Button(self.root,text="Back",command=HideSubjectScreen)
            self.btn1.grid(row=3,column=3,sticky=tk.S)
        except Exception as e:
            print(e)

      #function gets input from user and outputs subject result in listbox, exectues on button click
      def SubjectshowResult():

       try:
         
                entry = self.enter.get()
                if entry.isalpha() == False:
                    messagebox.showerror("Error","Please enter only letters!") #error message when user enters a number instead of a subject
                else:
                    result = functions.SubjectCall(self.enter.get())
                    if not result:
                      messagebox.showerror("Error","It doesn't exist.Please try again") #error message when makes an entry that doesn't exist
                    else: 
                    
                        self.frame1.grid(row=2,column=1)
                        self.listbox.delete(0, 'end')
                        for res in result:
                            self.listbox.insert("end", res)
                        
                        
       except Exception as e:
        print(e)
        
    
      #function to create Screen for class mark user input
      def ClassMarkScreen():
        try:    
            self.labl=tk.Label(self.root,text="Please enter a ClassMark",font=("calibri",13))
            self.labl.grid(row=1,column=0,sticky=tk.W)
            self.enter=tk.Entry(self.root,bd=2)
            self.enter.grid(row=1,column=1,sticky=tk.W)
            self.enter.focus()
            hidecanvas()
            self.btn = tk.Button(self.root,text="Search",command=ClassMarkshowResult)
            self.btn.grid(row=3,column=1,sticky=tk.S)
            self.btn1 = tk.Button(self.root,text="Back",command=HideSubjectScreen)
            self.btn1.grid(row=3,column=3,sticky=tk.S)
        except Exception as e:
            print(e)



      #function gets input from user and outputs classmark result in listbox, exectues on button click
      def ClassMarkshowResult():
        try:
            entry = self.enter.get()
            if entry.isalpha() == False:
             messagebox.showerror("Error","Please enter only letters!")    #error message when user enters a number instead of a classmark 
            else:
                result = functions.ClassMarkCall(self.enter.get())
                if not result:
                    messagebox.showerror("Error","It doesn't exist.Please try again")  #error message when makes an entry that doesn't exist
                else: 
                    
                    self.frame1.grid(row=2,column=1)
                    self.listbox.delete(0, 'end')
                    for res in result:
                        self.listbox.insert("end", res)
        except Exception as e:
            print(e)
                
     

      #function to create Screen for location user input
      def LocationScreen():
        try:
            locations =[]
            locations = functions.distinctLocations()
            self.labl = tk.Label(self.root,text="Choose a location", font=("calibri",13))
        
            self.labl.grid(row=1,column=0,sticky=tk.W)
            clicked = tk.StringVar()
            clicked.set(locations[0])
            self.drop = tk.OptionMenu(self.root,clicked,*functions.distinctLocations())
            self.drop.grid(row=1, column=0,padx=130)
            hidecanvas()
            
            self.btn = tk.Button(self.root,text="Search", command= lambda: LocationResult(clicked.get()))
            self.btn.grid(row=3,column=0,sticky=tk.S)
            self.btn1 = tk.Button(self.root,text="Back",command=HideLocationScreen)
            self.btn1.grid(row=3,column=2,sticky=tk.S)
        except Exception as e:
         print(e)
         
         
      
      
      #Gets drop down selection from user and displays result in listbox
      def LocationResult(clickedValue):
        try:
            self.frame1.grid(row=2,column=1)
            self.listbox.delete(0, 'end')
            subject =""
            for x in readCSV.locrows:
                if clickedValue in x[0]:
                    subject = functions.SubjectClassMark(x[1])
                    self.listbox.insert("end", subject + " | " + x[0] + " | " +  x[1])
        except Exception as e:
            print(e)
      

      
      #Opens Screen based on radio button selection
      def Radclicked(value):
       try:
            if value ==1:
                self.root.config(subjectScreen())
                
            elif value==2:
                self.root.config(ClassMarkScreen())
            elif value==3:
                self.root.config(LocationScreen())
       except Exception as e:
            print(e)


      #Function to take user back to home screen from location Screen
      def HideLocationScreen():
       try:
            self.canvas.grid()
            self.drop.grid_forget()
            self.labl.grid_forget()
            self.btn.grid_forget()
            self.btn1.grid_forget()       
            self.frame1.grid_forget()          
       except Exception as e:
        print(e)


      #Function to take user back to home screen from subject and classmark Screen
      def HideSubjectScreen(): 
          try:     
              self.canvas.grid()
              self.labl.grid_forget()
              self.btn.grid_forget()
              self.btn1.grid_forget() 
              self.enter.grid_forget()
              self.frame1.grid_forget()
          except Exception as e:
            print(e) 
          
            
            

      #Function to hide home screen and display different Screen based on user input
      def hidecanvas():
       try: 
         self.canvas.grid_forget()
       except Exception as e:
        print(e)
      
     
             
      #Canvas to house home screen widgets
      self.canvas = tk.Canvas(self.root, width=800, height=350)
      self.canvas.grid()
      
      
      #creating radio button widgets and placing them in a canvas
      self.rad = tk.IntVar()
      self.radio = tk.Radiobutton(self.canvas, text="Select to Input a Subject", font=("calibri",13),variable=self.rad, value=1,command=lambda: Radclicked(self.rad.get()))
  
      self.radio.grid(pady=10, row=1,column=0,sticky=tk.W)
      self.radio2 = tk.Radiobutton(self.canvas, text="Select to Input a ClassMark", font=("calibri",13),variable=self.rad,value=2,command=lambda: Radclicked(self.rad.get()))
      self.radio2.grid(pady=10,row=2,column=0,sticky=tk.W)
      
      self.radio3 = tk.Radiobutton(self.canvas, text="Select to Input a Location", font=("calibri",13),variable=self.rad,value=3,command=lambda: Radclicked(self.rad.get()))
      self.radio3.grid(pady=10,row=3,column=0,sticky=tk.W)
      
     #creates a frame and listbox, placing the listbox on the frame to display results
      self.frame1 = tk.Frame(self.root, bd=2, relief="groove")
      self.frame1.grid(row=2,column=1)
      self.listbox = tk.Listbox(self.frame1, width=70, height=10)
      self.listbox.grid(row=2,column=1)
      self.frame1.grid_forget()
      
    
      
     


      self.root.mainloop()

   
      
            

GUIclass()