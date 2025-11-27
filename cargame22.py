state='stop'
while True:
    print('1.start')
    print('2.stop')
    print('3.exit')
    ch=int(input("Enter one option:"))
    if ch==1:
        if state=='stop':
            print("car is started")
            state='start'
        else:
            print("car is already started")
    elif ch==2:
        if state=='start':
            print("car is stopped:")
            state='stop'
        else:
            print("car is already stopped")
    else:
        print("
        
else:
    print("choose correct option:")
                
            
        
