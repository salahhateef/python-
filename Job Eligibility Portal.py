print("hello to the process for the jop")
python = input("Does the student know Python well ? (yes/no) : ")
python = python.lower()
experience = int(input("how many years of experience do you have ? : "))
bootcamp = input("Do you have a certificate in computer science or for completion of a Bootcamp ? (yes/no) : ")
bootcamp = bootcamp.lower()
if python == "yes" and experience >= 2 or bootcamp == "yes" :
    print("glad to inform you that you are eligible for the job")
else :
    print("unfortunately You are not eligible for the job")
    
