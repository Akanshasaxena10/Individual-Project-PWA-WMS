"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""

from operator import truediv
from pickle import FALSE
from data import warehouse1, warehouse2
import time
import sys
import os


####################### Variables###########
menu_state=False
buyout=False
def checkout_process():
    sending = 'sendind data...'
    rc = 'Received credentials.'
    cc = 'Checking connection.'
    ct = 'Transfering money.'
    cf = 'Purchase completed.'
    
def clear_screen():
    os.system('clear') 


# YOUR CODE STARTS HERE


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
    

print(user_name,'Please choose an option: \n- 1.List items by warehouse \n- 2.Search an item and place an order \n- 3.Quit\n \n')

print('-------------------------------')
menu=int(input('Enter 1 ,2 or 3 : '))
print('-------------------------------')

buyout=False


# If they pick 1
if menu == 1: 
  print('***********************************************')  
  print('The items in warehouse1 are: ', len(warehouse1), '\n')
  
  w_len=len(warehouse1)
  for i in range(0, w_len):
    print('-', warehouse1[i])
    print('') 
    
    print('***********************************************') 
    print('The items in warehouse2 are: ', len(warehouse2), '\n') 
    
    w_len=len(warehouse2)
    for i in range(0,w_len):
        print('-', warehouse2[i])
    print('Back to the Menu-Press Enter')
   
   

        
    
      
# Else, if they pick 2
if menu == 2:
    item=input('What is the name of the Item?: ')
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
            print(user_name,'Would you like to purchase this item?(Yes/No) -Item:',item)
            print('***********************************************') 
            order_status=input('')
            if order_status == 'Yes':
                order_decision=True
            elif order_status == 'No':    
                  order_decision=True
                  quantity_valid=True
         ################################################################   
         
        while quantity_valid==False:
             quantity = int(input('Enter Quantity: '))
             if quantity <= sum_quantity:
                 print('Checkout Overview')
                 print('***************')
                 print('\nItem:',item,'\nQuantity:',quantity,'\nPick-up-location:',max_stock)
                 print('')
                 
                 buyout=input('Proceed to checkout?(Yes/No): ')
                 print('***********************************************') 
                 if buyout == 'Yes':
                    print('Purchase Accepted,Thankyou!!',user_name,'for your purchase with us')   
                    quantity_valid=True
                    buyout=True
                    checkout_process()
                 elif buyout == 'No':
                     print('Sorry!!!!',user_name,'We respect your choice!!!')  
                     
                     quantity_valid= True
                    
                   
                       
                 elif quantity > sum_quantity:         
                      print(user_name,'We regret we do not have this stock at this moment!!!!,Please try again!')
                      print('***********************************************')
                      
                      amount_is_valid = True
                      
                   
             else:
                print('')
                print(user_name,item,'was not found!!! Please search again!')

if menu == 3:               
    print(user_name,"Thankyou for visiting our warehouse")   
    print('***********************************************') 
   
    

      
    
    
    
             
    
                            
                 
                 
                 
               
            
            
                
        
    
     


