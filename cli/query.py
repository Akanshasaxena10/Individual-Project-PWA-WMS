"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from data import stock

import time
import sys
import os
from art import *


####################### Variables###########
menu_state=False
buyout=False

    


app_is_running = True
# YOUR CODE STARTS HERE
# tprint("Akki's Wonderland","rnd-xlarge")
tprint("Akki's House",font="rnd-medium")
#art=text2art("Akki",font="block",chr_ignore=True)
# print(art)
# tprint("Akki's  Warehouse")

print('')
print('WMS-Warehouse Management System')
print('-------------------------------')
print('-------------------------------')
print('Welcome To Our Warehouse')
print('-------------------------------')
print('-------------------------------')


# Get the user name
print('')
user_name=input('Please Type Your name here? ')
print('')


# Greet the user
print('********************************************')
print('Hello,', user_name, '!Welcome To our Warehouse.')
print('********************************************')
time.sleep(0.1)
print('Thankyou for choosing us.....')

time.sleep(1)
print("Let's us help you to make a better choice....!")
print('***********************************************')


# Show the menu and ask to pick a choice

print('')
for x in range(0,12):
    print(end="\r")
    
def option_menu():
    print(user_name,'Please choose an option: \n- 1.List items by warehouse \n- 2.Search an item and place an order \n- 3.Quit\n \n')

    print('-------------------------------')
    menu=int(input('Enter 1 ,2 or 3 : '))
    print('-------------------------------')
    if menu not in [1,2,3]:
        print('Invalid Input!!!Please Enter 1, 2 or 3') 
        print('**********************************************')
        buyout=False
    return menu
# def menu_1():
    

    # # If they pick 1
    # if menu == 1: 
    #     w_len1=len(warehouse1)
    #     print('***********************************************')  
    #     print('The items in warehouse1 are: ', len(warehouse1), '\n')
    #     for i in range(0, w_len1):
        

    #         print('-', warehouse1[i],)
        
    #     print('The items in warehouse2 are: ', len(warehouse2), '\n')   
    
    #     w_len2=len(warehouse2)
    
    #     for i in range(0,w_len2):
    #         print('-', warehouse2[i])
        
    # else:
    #     print('Back to the Menu-Press Enter')
    #     print('***********************************************') 
   
 ##'''I need to refractor this block of code as the stock and its type has change so the logic did.Refractor the code for doing that first understand the type of dictionary.
# from data import stock
# import datetime


# print('1: List all items')
# print('2: search and replace order')
# print('3: browse y category')
# print('4: Quit')

# user_input = input("Choose between 1 -4. ")
# # {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
# #  "date_of_stock": "2020-05-06 08:28:12"}
# while True:
#     if user_input == '1':
#         warehouse1 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 1]
#         warehouse2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2]

#         for item in set(warehouse1) | set(warehouse2):
#             print('')
#             print('-', item)
#         print(f"Total items in warehouse1: {len(warehouse1)}")
#         print(f"Total items in warehouse2: {len(warehouse2)}")
#         print('')
#         print('Thank you for your visit.')
#         break
# # {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
# #  "date_of_stock": "2020-05-06 08:28:12"}
#     if user_input == '2':
#         item_name = input('What is the name of the item? ')
#         wh1 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 1 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
#         wh2 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 2 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
#     if len(wh1 + wh2) == 0:
#         print("Sorry, we do not have that item in stock.")
#     else:
#         today = datetime.datetime.now()
#         for item in wh1:
#             print(f"- Warehouse1 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
#         for item in wh2:
#             print(f"- Warehouse2 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")

#         break
from data import stock
import datetime
import collections
from itertools import zip_longest


print('1: List all items')
print('2: search and replace order')
print('3: browse y category')
print('4: Quit')

user_input = input("Choose between 1 -4. ")
# {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
#  "date_of_stock": "2020-05-06 08:28:12"}
while True:
    if user_input == '1':
        warehouse1 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 1]
        warehouse2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2]

        for item in set(warehouse1) | set(warehouse2):
            print('')
            print('-', item)
        print(f"Total items in warehouse1: {len(warehouse1)}")
        print(f"Total items in warehouse2: {len(warehouse2)}")
        print('')
        print('Thank you for your visit.')
        break
# {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
#  "date_of_stock": "2020-05-06 08:28:12"}
    if user_input == '2':
        item_name = input('What is the name of the item? ')
        wh1 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 1 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        wh2 = [item['date_of_stock'] for item in stock if item.get('warehouse') == 2 and f"{item['state']} {item['category']}".lower() == item_name.lower()]
        if len(wh1 + wh2) == 0:
            print("Amount available: 0")
            print('Location: Not in Stock')
        else:
            today = datetime.datetime.now()
            for item in wh1:
                print(f"- Warehouse1 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            for item in wh2:
                print(f"- Warehouse2 (in stock {(today - datetime.datetime.strptime(item, '%Y-%m-%d %H:%M:%S')).days} days)")
            
            if len(wh1) > 0 or len(wh2) > 0:
                wh_d = {len(wh1): 'Warehouse 1', len(wh2): 'Warehouse 2'}
                maximum = max(wh_d.keys())
                print(f"Maximum availability: {maximum} in {wh_d[maximum]}")
            break
# {"state": "Almost new", "category": "Keyboard", "warehouse": 1, 
#  "date_of_stock": "2020-05-06 08:28:12"}
    if user_input == '3':
        categories = [item['category'] for item in stock ]
        categories_ct = collections.Counter(categories)
        cat_d = {id: f"{category} ({categories_ct[category]})" for id, category in enumerate(categories_ct, start = 1)}
        print()
        for id, category in cat_d.items():
            print(f"{id}. {category}")
        get_id = int(input('Choose a category'))
        print()
        selected_cat = cat_d[get_id].split(" ")[0]
        print(f'List of {selected_cat} available:')

        wh1 = [ f"{item['state']} {item['category']}" 
        for item in stock if item.get('warehouse') == 1 and item.get('category') == selected_cat]
        wh2 = [ f"{item['state']} {item['category']}" for item in stock if item.get('warehouse') == 2 and item.get('category') == selected_cat]

        print(len(set(wh1)))
        print(len(set(wh2)))
        print(list(zip(set(wh1), set(wh2))))
        print(list(zip_longest(set(wh1), set(wh2), fillvalue=False)))

        for item_wh1, item_wh2 in zip_longest(set(wh1), set(wh2), fillvalue=False):
            if item_wh1: print(f"{item_wh1}, warehouse1")
            if item_wh2: print(f"{item_wh2}, warehouse2")
        print("Thank you for your visit")
        break
    
def menu_1():
    if menu == 1:
        def filter_data(key,value):
            result = []
            for item in stock:
                if item[key] == value:
                    result.append(item)
            return result
        warehouse1 = filter_data('warehouse',1)
        for item in warehouse1:
            #print(filter_data('category',item['category']))
            print('---')
            print(' ')
            print('Item:----',item['category'])
            ## no of items
            print('total items of in warehouse1', len(filter_data('category',item['category'])))
            #print('~',item)
            #print(item['category'])
        warehouse2 = filter_data('warehouse',2)
        for item in warehouse2:
            pass
            #print(filter_data('category',item['category']))
            #print('~',item)
            #print(item['category'])
        
def menu_2():
    
      
    # Else, if they pick 2
    if menu == 2:
        item=input('What is the name of the Item?: ')
        item=item[0].upper()+item[1:]
        if item in warehouse1 or item in warehouse2:
            print('')
            print(user_name,'Congratualations!!!!',item,'-','was found')
            print('***********************************************') 
            max_stock=''
            max_count=0
            item_quantity1=warehouse1.count(item)
            item_quantity2=warehouse2.count(item)
            sum_quantity=item_quantity1+item_quantity2
            print('Total Quantity: ', sum_quantity)
            if item_quantity1 >= 1  and  item_quantity2  >=1:
                print(user_name,'Your item  is available in :Both warehouses')
                print('***********************************************') 
                if item_quantity1 > item_quantity2:
                    max_stock =' In warehouse1'
                    max_count=warehouse1.count(item)
                elif item_quantity1 < item_quantity2:
                    max_stock='In warehouse2'
                    max_count=warehouse2.count(item)
            elif item_quantity1 >= 1 and item_quantity2 == 0:
                print(user_name,'Your item  is available in : warehouses 1') 
                print('***********************************************') 
                max_stock=  'warehouse 1'
                max_count=warehouse1.count(item)
            elif item_quantity2 >= 1 and item_quantity1== 0:
                print(user_name,'Your item  is available in : warehouses 2')
                print('***********************************************') 
                max_stock='warehouse 2'
                max_count=warehouse2.count(item)
            if item_quantity1==item_quantity2:
                print('Maximum Stock: ',warehouse1.count(item),'in both warehouses')
                max_stock='Both warehouses'
            else:    
                print('Availability of your item: ',max_count,'in',max_stock)
                print('***********************************************') 
            
            ############################################################   
                quantity_valid=False
                order_decision = False
               
            while order_decision == False:
                print(user_name,'Would you like to purchase this item?(y/n) -Item:',item)
                print('***********************************************') 
                
                order_status=input('')
                # order_status=item[0].upper()+item[1:]
                if order_status == 'y':
                    order_decision=True
                    quantity_valid=False
                    print('check')
                elif order_status == 'n':    
                    order_decision=True
                    quantity_valid=True
            ################################################################   
            
            while quantity_valid==False:
                quantity = int(input('Enter Quantity: '))
                if quantity <= sum_quantity:
                    
                    print('***************')
                    print('\nItem:',item,'\nQuantity:',quantity,'\nPick-up-location:',max_stock)
                    print('')
                 
                    buyout=input('Proceed to checkout?(y/n): ')
                    print('***********************************************') 
                    if buyout == 'y':
                        print('Purchase Accepted,Thankyou!!',user_name,'for your purchase with us')   
                        quantity_valid=True
                        buyout=True
                        
                    elif buyout == 'n':
                        print('Sorry!!!!',user_name,'We respect your choice!!!') 
                        print('***********************************************')
                        print('***********************************************') 
                        
                        quantity_valid= True
                        
                    
                        
                    elif quantity > sum_quantity:         
                        print(user_name,'We regret we do not have this stock at this moment!!!!,Please try again!')
                        print('***********************************************')
                        
                        amount_is_valid = True
                        
                    
        else:
            print('')
            print(user_name,item,'was not found!!! Please search again!')



def menu_3():
    
    if menu == 3:               
        print(user_name,"Thankyou for visiting our warehouse")   
        print('***********************************************') 
        global app_is_running
        app_is_running = False
   
app_is_running = True

while app_is_running == True:
    menu=option_menu()
    if menu == 1:
        menu_1()
        
    elif menu == 2:
        menu_2()
        
    elif menu == 3:
        menu_3()
        break
    

      
    
    
    
             
    
                            
                 
                 
                 
               
            
            
                
        
    
     


