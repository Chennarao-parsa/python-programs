amount=int(input("Enter a amount"))
if amount>10000:
    discount=amount*0.3
elif amount>5000:
    discount=amount*0.2
elif amount>1000:
    diccount=amount*10
else:
    discount=0
final=amount-discount
print(f"amount={amount:.2f}")
print(f"discount={discount:.2f}")
print(f"final={final:.2f}")
