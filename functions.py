class laptop:
    name=input("Enter your Name :")
    price=input("Enter your price :")
    discount=input("Enter your discount :")

    try:
        c = int(price)
        print("yes")

    except:
        print("not")


    print("Name : " + str(name) + " price : " + str(price) + " discount :" + str(discount)  )

class laptop1:  
    def __init__(self,name,id,price):  
        self.name = name  
        self.id = id
        self.price = price  
  
l = laptop1("sa",1,2500)  
  
print(getattr(l,'name'))  
  
setattr(l,"price",5000)  
  
print(getattr(l,'price'))  
  
  
print(hasattr(l,'id'))  

delattr(l,'price')  

print(l.price)  