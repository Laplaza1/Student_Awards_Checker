#Skyler Savage
#Student GPA
#Checks the GPA of a student to see if they make Honor roll and the deans list.




def GPA_Checker():

   while True:
        last_name= input("Last Name of The Student :")

        #Checks if user entered the exit phrase "ZZZ" or forgot to capitialize it then Returns False to close the loop
        if last_name and last_name.upper() == "ZZZ":
            return False
        else:
            pass
        first_name = input("First Name of the Student :")

        #asks for the input then converts it to float if GPA was entered as a string i.e "Five" then an error will occur
        GPA = float(input("Please enter the GPA including any decimals :"))
        
        #Checks if GPA meets Honor roll requirements
        if GPA >= 3.25:
            #checks if GPA entered was way too high resulting in students name being brought up and a closing of loop
            if GPA>= 5.0:
                print("GPA way too high-->",first_name,last_name)
                return False 
            
            #Checks if GPA is greater than or equal to 3.5 if true then awards are both Honor roll and Deans list
            if GPA >= 3.5:
                awards =["Honor Roll","Deans List"]
            
            #If GPA was less than 3.5 then awards are just Honor roll    
            else:
                awards =["Honor Roll"]
        
        #If GPA below 3.25 then student has no awards
        else:
            awards = ["None"]

        student = {
            "Name": first_name +" "+last_name,
            "GPA": GPA, 
            "Awards": awards}
        
        #Prints the name, GPA, Awards
        print("\n",student,"\n")
        


GPA_Checker()
