item=[] 
product=0
number=0
total_price=0
total_amount=0

while(number!=4):
  number=int(input("\nWatchmen Security Supply\n 1. Add to Inventory\n 2. View Inventory\n 3. Product Report\n 4. Exit\n"))
  
  if(number==1):
      product=int(input("\nEnter number of product to add:"))
      for i in range(0,product):
         name=input("\nEnter product name:")
         price=int(input("Enter price of the product:"))
         amount=int(input("Enter amount of the product:"))
         item.append([name,price,amount]) 
  
  if(number==2):
      print("Product\tPrice\tAmount\n")
      for i in range(0,product): 
         print(item[i][0],"\t",item[i][1],"\t",item[i][2],"\n")
  
  if(number==3):
      for i in range(0,product):
        total_price+=item[i][1]*item[i][2]
        total_amount+=item[i][2]
      print("Total price = ",total_price,"\nTotal Amount = ",total_amount)