import time as t
import matplotlib.pyplot as p
moves=[0]
def toh(n,s,i,p):
    if n==1:
        if p==1:
            print("Move disc",n,"from",s,"to",d)
            moves[0]+=1
        else:
            t.sleep(0.3)
    else:
        toh(n-2,s,i,d,p)
        if p==1:
            print("Move disc",n,"from",s,"to",d)
            moves[0]+=1
        else:
            t.sleep(0.3)
            toh(n-1,i,d,s,p)
if __name__=='__main__':
    while True:
        print('1:Execute\n2:plot graph\n3:exit')
        op=int(input('Enter your choice:'))
        if op==1:
            n=int(input("Enter numbewr of discs:"))
            s=int(input("Enter source pole:"))
            d=int(input("Enter destination pole:"))
            i=int(input("Enter intermediate pole:"))
            moves=[0]
            toh(n,s,d,i,1)
            print("Total no of moves=",moves[0])
        elif op==2:
            size_list=[]
            time_list=[]
            for size in range(2,10):
                `size_list.append(size)

                moves=[0]
                start=t.time()
                toh(size,A,C,B,2)
                stop=t.time()
                time_list.append(stop-start)
            p.xlabel("Size")
            p.ylabel("Time")
            p.plot(size_list,time_list)
            p.show()
        elif op==3:
            print('Thank you')
            break
        else:
            print("Invalid choice")
                  
        
