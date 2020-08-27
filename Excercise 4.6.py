def computepay(h,r):
    
    if h<= 40: p= h*r
    else :
        p = (h-40)*(r*1.5)+(40*r)
    return (p)

hrs = input("Enter Hours:")
rt = input("Enter Rate:")
pay = computepay(float(hrs),float(rt))
print("Pay",pay)
