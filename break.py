i=0
num=int(input("Input the number"))
if(num<100):
    print("Enter number greater then 100")
else:
    while(i<num):

        print(i)
        i=i+1
        if(i==100):
             break
        
    print("Congratulation u have printed till 100")
