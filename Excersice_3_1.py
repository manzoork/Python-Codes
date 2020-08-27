hrs=float(input ("Enter Hours:"))
rt=float(input ("Enter Rate:"))
if hrs<= 40: pay= hrs* rt
else :
    pay = (hrs-40)*(rt*1.5)+(40*rt)
print(pay)
