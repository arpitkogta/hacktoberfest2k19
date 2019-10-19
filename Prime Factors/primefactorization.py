n=int(input("Enter an integer:"))
print("Factors are:")
i=1 #i initialised to 1 instead of 0
#for(i=0;i<n;i++) this line of code is not required as the while loop is already there for iteration of the code
while(i<=n):
    k=0
    if(n%i==0): #bug in this line of code for i=0
        j=1
        while(j<=i):
            if(i%j==1):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1
