import time as t

def restart():
    '''function to restart the timer'''
    x=input("do you want to reset the timer? y/n")
    if x =="y" or x=="Y":
        timer()
    else:
        print("\nThankyou,have a good day !!")
        

def timer():
    try:
        sec=int(input("enter time in seconds as integer"))
    except:
        print("error occured, only integer value accepted")
        sec=int(input("set the timer in seconds as integer"))
    try:
        print("to pause the timer press ctrl+c")#timer can only be paused one time
        for i in range(sec,0,-1):
            print(i)
            t.sleep(1)
        print("\nTime ended")
        restart()
        
    except KeyboardInterrupt :
        print("timer paused")
        q=input("do you want to resume the timer ? y/n")
        if q=="y" or q=="Y":
            r=i-1
            for z in range(r,0,-1):
                print(z)
                t.sleep(1)
            print("time ended")
            restart()
        else:
            restart()
timer()

