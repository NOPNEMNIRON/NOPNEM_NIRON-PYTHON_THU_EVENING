
#
with open("content.txt","w") as fnew:
    fnew.write("NIRON \n22")
#
with open("content.txt", "r") as filex:
    line=filex.readlines()
    print("Lines = ",len(line))
#
with open("content.txt","r") as sf:
    for line in sf:
        if "NIRON" in line: 
            print("Access")
#
with open("content.txt","a") as new:
    new.write("RICKY \n23")
    new.close
