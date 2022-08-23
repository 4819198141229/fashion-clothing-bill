CN=input("Enter the customer name:")
CM=int(input("Enter the customer mobile number:"))
Add=input("Enter address:")
amount=int(input("Enter the amount:"))
if amount>6000:
    disc=20/100
    Discount=amount*disc
    total=amount-Discount
elif amount>4000 and amount<=6000:
    disc=15/100
    Discount=amount*disc
    total=amount-Discount
elif amount>1000 and amount<=4000:
    disc=10/100
    Discount=amount*disc
    total=amount-Discount
else:
    total=amount
print("Total amount to be paid={}".format(total))
print("Thank You")
