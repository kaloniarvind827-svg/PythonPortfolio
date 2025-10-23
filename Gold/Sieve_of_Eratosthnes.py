# program to print list of prime within a range
def PrimeUpTo(num):
    Checklist = [True]*(num+1)
    Checklist[0]=False  
    Checklist[1]=False  #making it standard by including 0 and 1 else not needed 
    
    
    for i in range(2,int(num**0.5+1)):
        if(Checklist[i]==True):
            for j in range(i*i,num+1,i):
                Checklist[j]=False
                
                
    for p in range(2,num+1):#tell why this
        if(Checklist[p]==True):
            print(p,end="  ")          

PrimeUpTo(60)
