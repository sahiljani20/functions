# class laptop:
#     discount = 50
#     count = 0
#     def __init__(self,brandname,price,laptopp):
#         self.brandname=brandname
#         self.price=price
#         self.laptopp=laptopp
#         laptop.count = laptop.count+1


#     def apply_discount(self):
#         offprice=(laptop.discount/100)*self.price
#         print("Price = %d" %(self.price))

#         return self.price-offprice
    
# laptop1=laptop('hp',200,'abc')
# print("the name of the laptop : %s \nDiscount :%d \n\n" %(laptop1.brandname,laptop1.apply_discount()) )




# laptop2=laptop('ht',70,'abc')
# print("Discount :%d" %(laptop2.apply_discount()) )

# print("the number of laptop :",laptop.count )
from gtts import gTTS
import os

from array import array as var
class pro:

    d = int(input("Enter the number of products :"))
    c=int(0)
      
    os.system("espeak 'hello wolrld'")
    def disc(price,discount):
            return price-((discount/100)*price)

    for i in range(c , d):


        name = input("Enter product name :")
        # tts = gTTS(text='the name of product is '+name, lang='en')
        # tts.save("names.mp3")
        # os.system("mpg321 names.mp3")
        # print(name)
        price=int(input("Enter any price :"))
        # print(price)
        discount = int(input("Enter amount of discount in percentage :"))
        # print(discount)

        
        
        

        
        print("\n\nThe last Price of " + name +  "  : ", disc(price,discount) )
        print("\n")
        s=str(disc(price,discount))
        tts=gTTS(text='The last price of '+ name +' is '+s,lang='en')
        tts.save('discount.mp3')
        os.system("mpg321 discount.mp3")

        # print("\nThe last price of entered products : ",var)
