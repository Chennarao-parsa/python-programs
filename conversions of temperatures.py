print("temperature conversion")
print("1.celsius to fahrenheit con:")
print("2.Fahrenheit to celsius con:")
choice=int(input("Enter your choice(1 or 2):"))
if choice==1:
    celsius=float(input("Enter tempearatur  in a celsius:"))
    fahrenheit=(celsius*(9/5))+32
    print(f"{celsius}^oc={fahrenheit}^of")

elif choice==2:
    fahrenheit=float(input("enter temperature in fah:"))
    celsius=(fahrenheit-32)*(5/9)
    print(f"{fahrenheit}^of={celsius}^oc")
else:
    print("Invalid input:")
