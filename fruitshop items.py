


fruits=['apple','banana','orange','mango']
cart=[] 
while True:
    for  f in fruits:
        print(f)
    print("**********FRUIT SHOP**********")
    print("1.ADD")
    print("2.REMOVE")
    print("3.VIEW")
    print("4.Exit")
   
    ch=int(input("choose one option"))
    if ch == 1:
        fruit=input("enter a fruit you want to add:")
        
     
        if fruit in fruits:
            if fruit in cart:
                print(fruit,"fruit is already in the cart")
            else:
                
                cart.append(fruit)
                print(fruit,"added to cart")
            
    elif ch == 2:
        fruit=input("enter fruit you want to remove")
        if fruit in cart:
            cart.remove(fruit)
            print(fruit,"removed ")
        else:
            print(" fruit is not existed in cart:")
    elif ch==3:
        for fr in cart:
            print("*"*20)
            
            print(fr)
            print("*"*20)
    elif ch==4:
        print("exit")
        break
    else:
        print("choose correct  option")
     
    print()
        
                
