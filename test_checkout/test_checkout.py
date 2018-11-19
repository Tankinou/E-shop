# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 19:36:10 2018

@author: tancr
"""
#%%
from Checkout import checkout

from Checkout import checkout_insurance

lst1 = []

#%%
shopping_cart1 = {}
assert checkout(lst1) == "The shopping cart must not be empty"
assert checkout_insurance(lst1) == "The shopping cart must not be empty"


#%%

shopping_cart1 = {'Guitar': 1000,'Pick box': 5,'Guitar Strings': 10}


assert checkout(lst1) == 1015
assert checkout_insurance(lst1) == 1060

#%%

shopping_cart1 = {'Pick box': 5,'Guitar Strings': 10}

assert checkout(lst1) == 15
assert checkout_insurance(lst1) == 45

#%%

shopping_cart1 = {'Guitar': 1000,'Guitar': 1000,'Pick box': 5,'Guitar Strings': 10}


assert checkout(lst1) == 2015
assert checkout_insurance(lst1) == 2075






















