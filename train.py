t=int(input())
for _ in range(t):
    n=int(input())
    if(n>0 and n<=108):
        c=((((n-1)//3)+1)%4)
        if(c==1):
            if(n%3==1):
                print(n+11,"WS")
            elif(n%3==2):
                print(n+9,"MS")        
            else:
                print(n+7,"AS")
        elif(c==2):
            if(n%3==1):
                print(n+5,"AS")
            elif(n%3==2):
                print(n+3,"MS")        
            else:
                print(n+1,"WS")
        elif(c==3):
            if(n%3==1):
                print(n-1,"WS")
            elif(n%3==2):
                print(n-3,"MS")        
            else:
                print(n-5,"AS")
        else:
            if(n%3==1):
                print(n-7,"AS")
            elif(n%3==2):
                print(n-9,"MS")        
            else:
                print(n-11,"WS")
    else:
        print("invalid input")
    
      
        
    
