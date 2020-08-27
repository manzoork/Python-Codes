#Check description below for details on the excercise
filename = input("Enter file name: ")

if len(filename) < 1:
    fhandle = open("mbox-short.txt")
else:
    fhandle = open(filename)

words = list()
email_dict = dict()

for line in fhandle:
    line = line.rstrip()
    if line.startswith("From: "):
        continue
    if line.startswith("From "):
        words = line.split()
        email_dict[words[1]] = email_dict.get(words[1], 0) + 1

#lst = list()
lst = sorted([(v, k) for k, v in email_dict.items()])
count, email = max(lst)
print(email, count)
