#! /usr/bin/python


EXTRA_CHARGE = 0.50

def procceedings(amount, balance):
    if amount + EXTRA_CHARGE > balance:
        return False 	
    elif amount%5 != 0:
        return False 
    else:
        return True

amount_balance = map(float, raw_input().split())
if procceedings(amount_balance[0], amount_balance[1]):
    print "%.2f"% (amount_balance[1] - (amount_balance[0] + EXTRA_CHARGE))
else:
    print "%.2f"% amount_balance[1]
