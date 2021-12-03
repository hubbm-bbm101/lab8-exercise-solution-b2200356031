import sys
file = open(sys.argv[1],"r")
dict = {}

for line in file:
    
    temp = line.split(":")
    name = (temp[0])
    school = (temp[1])
    dict[name] = school

for student in sys.argv[2].split(","):
    try:
        print("Name: {} , University: {}".format(student,dict[student]))
    except:
        print("No record of {} was found!".format(student))