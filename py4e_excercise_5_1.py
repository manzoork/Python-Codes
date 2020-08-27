largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break 
    try:
        num = float(num)        
    except: 
        print("Invalid Entry")
        continue
    ifs largest == None : 
        largest = num
        smallest = num
    if num > largest : largest = num
    if num < smallest : smallest = num    
print("Maximum is", largest)
print("Minimum is", smallest)