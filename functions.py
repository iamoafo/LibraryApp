import readCSV
import ConsoleApp

#This function recieves the classmark as a parameter and iterates through the location csv file to return corresponding location based on classmark
def LocClassMark(classmark): 
  try:   
    for x in readCSV.locrows:
        if classmark in x[1]:
            return x[0]
  except Exception as e:
    print(e)          
            
#This function recieves the classmark as a parameter and iterates through the subject csv file to return corresponding location based on classmark
def SubjectClassMark(classmark):
 try:
    for x in readCSV.subjectRows:
        if classmark in x[1]:
            return x[0]
 except Exception as e:
    print(e)


#This function accepts a subject input from the user, iterates through the subject csv file,
#returns the corresponding classmark and passes it into the locClassMark function to get the corressponding
#location, appends it to a list and returns that list
def SubjectCall(subject):
 try:
        arr=[]
        for x in readCSV.subjectRows:
         if subject.lower() in x[0].lower():
            loc = LocClassMark(x[1])
            arr.append(x[0] + " | " + loc + " | " + x[1])
        return arr
 except Exception as e:
    print(e)

      
#This function accepts a classmark input from the user, iterates through the subject csv file,
#returns the corresponding classmark and passes it into the locClassMark function to get the corressponding
#location, appends it to a list and returns that list
def ClassMarkCall(classmark):
  try:  
        arr=[]
    
        for x in readCSV.subjectRows:
         if classmark.lower() in x[1].lower():
            loc = LocClassMark(x[1])
            arr.append(x[0] + " | " + loc + " | " + x[1])
            
        return arr 
  except Exception as e:
    print(e)


#function to get distinct/unique locations from csv file
def distinctLocations():
    try:
        uniqueLocations = []
        
        for x in readCSV.locrows:
            uniqueLocations.append(x[0])
        uniqueLocations = list(dict.fromkeys(uniqueLocations[1:]))
        return uniqueLocations
    except Exception as e:
        print(e)
 


#Gets unique locations from distinctLocations function, recieves input from the user and returns the location, subject and classmark
def LocCall():
 try:   
    n=1
    dup= distinctLocations()
    print("\n")
    for a in dup:
        print("{}.{}".format(n,a)) 
        n=n+1
    
    location = int(input("Please select a location from options 1 to 6\n location: "))
    print("\n")
    if location == 1:
        for b in readCSV.locrows:
             if dup[0] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + " | " + b[1])
    elif location == 2:
        for b in readCSV.locrows:
            if dup[1] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + "  | " + b[1])
    elif location == 3:
        for b in readCSV.locrows:
            if dup[2] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + " | " + b[1])
    elif location == 4:
        for b in readCSV.locrows:
            if dup[3] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + " | " + b[1])
    elif location == 5:
        for b in readCSV.locrows:
            if dup[4] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + " | " + b[1])
    elif location == 6:
        for b in readCSV.locrows:
            if dup[5] in b[0]:
                 subject = SubjectClassMark(b[1])
                 print( subject + " | " + b[0] + " | " + b[1])             
                
 except Exception as e:
    print(e)        



#function to prompt user to run again
def Runagain():
    try:
      runAgain = input("\nDo you want to run again?\n y for yes and n for no: ")
      if runAgain == 'y':
            Keelelibrary()
      elif runAgain =='n':
            print("\nThank you, come again!")
            exit()
    except Exception as e:
        print(e)







 #Function which contains user interface code for console application
def Keelelibrary():
 try:
    print("Hello! Welcome to the keele University Library System!")
    start = int(input("Please select:\n 1 for subject(part/full)\n 2 for classmark \n 3 for location \n you selected:"))
    #If user selects 1, SubjectCall function is called which allows the user to search by typing a subject in part or full
    if start == 1:
        subjectresult=[]
        subject = input("please input a subject part or full\n subject: ")
        subjectresult =  SubjectCall(subject)
        if not subjectresult:
            print("\nSorry, that doesn't exist")
            Runagain()
        else:
            for i in subjectresult:
                print("\n",i)
            Runagain()
    #If user selects 2, ClassMarkCall function is called which allows the user to search by typing a classmark in part or full
    elif start == 2:
        classMarkresult=[]
        classMark = input("please input a classmark\n Your ClassMark: ")
        classMarkresult =  ClassMarkCall(classMark)
        if not classMarkresult:
            print("\nSorry, that doesn't exist")
            Runagain()
        else:
            for i in classMarkresult:
                print("\n",i)
            Runagain()

    #If user selects 3, LocCall function is called which allows to user to select a location and display results based on the location

    elif start ==3:
        LocCall()
        Runagain()
    else : print("Please enter only numbers 1,2 or 3"),Keelelibrary()
 except ValueError:
    print("Please only enter numbers")
    Runagain()
          