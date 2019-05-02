# class average:

    
#     num1 = int(input("Enter number 1 :"))
#     # print(name)
#     num2=int(input("Enter number 2 :"))
#     # print(price)

#     ave=(num1+num2)/2




#     print("The average of two numebrs : " ,ave)
from array import array as var
class average:

    d=int(input("Enter the number of numbers :"))
    a=d
    c=0
    var=[]
    sum =0
    for i in range(c , d):
        
        while c<a:
            num=int(input("Enter the number :"))
            sum=sum+num
            var.append(num)
            c=c+1
            
        
    print("The total +",sum)      
    print(len(var))
    c=len(var)
    ave=sum/c
    print("Average =",ave)


        