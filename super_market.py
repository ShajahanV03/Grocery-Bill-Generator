from datetime import datetime
name=input("Enter your Name--")
phone=int(input("Enter Your Contact Number--"))

                # Available Items
available_items='''
rice    60/kg
sugar   45/kg
salt    20/each
oil     100/litre
maggi   25/each
apples  150/kg
banana  50/kg
'''
            # Declarations
items=[]
quantities=[]
prices=[]
total_price=0
grand_total=0

item={'rice':60,'sugar':45,'salt':20,'oil':100,'maggi':25,'apples':150,'banana':50}

option=int(input("Enter 1 For Available Items --"))
if(option==1):
    print(available_items)
else:
    print("invalid input")
    
num_items=int(input("Enter Number Of Items You Want To Buy --"))

for i in range(num_items):
    print(f"\n Enter Your Item {i + 1}:")
    item_name = input(" Item name-- ")
    quantity = int(input(" Quantity-- "))
    
    if item_name in item.keys():
        items.append(item_name)
        quantities.append(quantity)
        price = quantity * item[item_name]
        prices.append(price)
        total_price+=price
        gst=total_price*5/100
        grand_total=gst+total_price
    else:
        print("Item is unavailable")

bill=int(input("Enter 1 to Generate Your Bill --\n"))
if(bill==1):
    print(35*"=","S MART",35*"=")
    print(34*" ","Bengaluru")
    print(f"Name: {name:<20} Contact: {phone:<15} Date: {datetime.now()}")
    print(79*"-")
    print(f"{'S.NO.':<17}{'Items':<20}{'Quantity':<23}{'Price':<25}")

    print(79*"-")
    for i in range(len(items)):
        print(f"{i + 1:<17}{items[i]:<20}{quantities[i]:<23}{prices[i]:<25}")
print(79*"-")    
print(55*" ","Total Price:",total_price)
print(55*" ","GST:",gst)
print(79*"-") 
print(55*" ","Grand Total:",grand_total)
print(79*"-") 
print(20*" ","Thank You! Visit Again")
print(79*"-")       
       