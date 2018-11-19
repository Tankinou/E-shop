# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:14:52 2018

@author: tancr
"""
#%%
'White Belt'
# =============================================================================
# Our e-shop sells the following products:
# 
#    1. Guitar: $1000
#    2. Pick box: $5
#    3. Guitar Strings: $10
# 
#    Create a function named checkout that takes a list that represents a shopping cart and returns the total cost of it.  This function should check that the shopping cart must not be empty.
# 
#    Create also some tests for the function.  Try to think of the corner cases.
# 
#    Hint: you can represent a product as a dictionary with a name and a price.
# =============================================================================

#shopping_cart1 = {}
shopping_cart1 = {'Guitar': 1000,'Pick box': 5,'Guitar Strings': 10}
lst1 = []

def checkout(lst):
    if not bool(shopping_cart1):
        print("The shopping cart must not be empty")
    else:
    
        for a in shopping_cart1:
            lst.append(shopping_cart1[a])
        return sum(lst)
        


#%%
        
    
'Blue Belt'

# =============================================================================
#   You want to give more features to the user, so you decide that you will allow them to purchase an insurance package on their purchase and also priority mail.  Consider that these two new services can only be purchase once per order.
# 
#    1. Insurance: $5
#    2. Priority mail: $10
# 
#    Modify your checkout function so it handles these cases correctly, and add more tests that check your functionality.
# 
# =============================================================================
 
        
#shopping_cart1 = {}
shopping_cart1 = {'Guitar': 1000,'Pick box': 5,'Guitar Strings': 10}
lst1 = []
add_insurance = 'Yes'
add_priority_mail = 'Yes'
def checkout_insurance(lst):
    if not bool(shopping_cart1):
        print("The shopping cart must not be empty")
    else:
        if add_insurance == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] += 5
        else:
            None
        if add_priority_mail == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] += 10
        else:
            None
        for a in shopping_cart1:
            lst.append(shopping_cart1[a])

        return sum(lst)
        
        
        
        
#%%
        
'Black Belt'

# =============================================================================
#    You want to add a new feature to your ecommerce, you want to create three different tiers of customers:
# 
#    - normal: No added benefits
#    - silver: 2% discount on products from the ecommerce
#    - gold: 5% discount on everything
# 
#    Modify the checkout function to accept another parameter with the tier of the customer and apply the discounts as needed.
# 
#    Implement this feature in the checkout function and add tests that prove that your implementation is correct.
# 
# =============================================================================


#shopping_cart1 = {}
shopping_cart1 = {'Guitar': 1000,'Pick box': 5,'Guitar Strings': 10}
lst1 = []
add_insurance = 'Yes'
add_priority_mail = 'Yes'
normal= ''
silver = ''
gold = 'Yes'

def checkout_subscription(lst):
    if not bool(shopping_cart1):
        print("The shopping cart must not be empty")
    else:
        if normal == 'Yes':
            None
        if silver == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] = shopping_cart1[a]-(shopping_cart1[a]*0.02)
        else:
            None
        if add_insurance == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] += 5
        else:
            None
        if add_priority_mail == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] += 10
        else:
            None
        if gold == 'Yes':
            for a in shopping_cart1:
                shopping_cart1[a] = shopping_cart1[a]-(shopping_cart1[a]*0.05)
        else:
            None
        for a in shopping_cart1:
            lst.append(shopping_cart1[a])

        return sum(lst)
        
        






































