# Check below descriptions for details on the Excercise
filename = input("Enter file name: ")
if len(filename) < 1 : fhandle = open("mbox-short.txt")
else : fhandle = open(filename)
count = 0
wds = list()
for line in fhandle:
    line = line.rstrip()
    if line.startswith("From: "): continue
    if line.startswith("From "):
        wds = line.split()  
        count= count + 1 
        print(wds[1]) 
        
print("There were", count, "lines in the file with From as the first word")
