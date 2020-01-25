bill=int(input("enter the bill Amount\n"))
print("Coose one option from following list")
print("1. 15%")
print("2. 18%")
print("3. 20%")
print("4. More than given above\n")
option=int(input())
if option==4:
    tip=input("Enter Tip amount\n")
    if '$' in list(tip):
        x=tip.replace('$','')
        x=int(x)
        bill=bill+x
    else:
        tip=int(tip)
        bill=bill+tip
if option==1:
    bill=bill+(bill*15/100)
if option==2:
    bill=bill+(bill*18/100)
if option==3:
    bill=bill+(bill*20/100)
print("Total amount=",int(bill))
