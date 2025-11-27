x=[1,2,3,4,5,6]
r_type=input("enter rotation type (RR/LR):")
no_ele=int(input("Enter no of elements you want to enter:"))
no_ele=no_ele%len(x)
if r_type=='RR':
    output=x[-no_ele:]+x[:-no_ele]
    print(output)
elif r_type=='LR':s
    output=x[no_ele:]+x[:no_ele]
    print(output)
else:
    print("enter a correct option:")
