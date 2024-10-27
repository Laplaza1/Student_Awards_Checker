#Skyler Savage
#Student GPA
#Checks the GPA of a student to see if they make Honor roll and the deans list.




def GPA_Checker():

    while True:
        last_name= (input("Last Name of The Student :"))
        print(last_name,"\n",last_name.upper())
        if last_name and last_name.upper() == "ZZZ":
            print((last_name and last_name.upper() == "ZZZ"))
            return False
        else:
            pass
        first_name = input("First Name of the Student :")
        GPA = float(input("Please enter the GPA including any decimals :"))
        if GPA >= 3.25:
            if GPA>= 5.0:
                print("GPA way too high-->",first_name,last_name)
                return False 
            if GPA >= 3.5:
                awards =["Honor Roll","Deans List"]
            else:
                awards =["Honor Roll"]
        else:
            awards = ["None"]
        student = {
            "Name": first_name +" "+last_name,
            "GPA": GPA, 
            "Awards": awards}
        print("\n",student,"\n")
        


GPA_Checker()