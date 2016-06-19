'''
Edit this file to complete the exercises in
'Iterate over Data with for Loops'

Edit this file to complete the exercises in
'Iterating over Data with for Loops and Comprehensions'
'''

#----------------------------------------------------------------------------
#Boilerplate code to set up the exercises. DO NOT MODIFY!
import random
random.seed(891)
account_id_list = range(1,51)
account_balance_list = [random.randint(-2000,2000) for id in account_id_list]
#End boilerplate.
account_balance_list

#----------------------------------------------------------------------------

#Set total_balance equal to the sum of all the items in
#account_balance_list:
total_balance = 0
for balance in account_balance_list:
    total_balance = total_balance + balance
total_balance

#set total_credit_balance equal to the sum of all the items
#in account_balance_list that are greater than or equal to zero.
#Additionally, set num_accounts_with_credit equal to the number
#of items that meet this criteria:
total_credit_balance = 0
num_accounts_with_credit = 0
for balance in account_balance_list:
    if balance>=0:
        total_credit_balance=total_credit_balance+balance
        num_accounts_with_credit=num_accounts_with_credit+1
total_credit_balance
num_accounts_with_credit

y=list(x for x in account_balance_list if x>=0)
len(y)




#set account_id_debt_list equal to a list of all the items
#in account_id_list that correspond (have the same index)
#as items in account_balance_list that are less than zero:
account_id_debt_list = list(i for i in account_id_list if account_balance_list[i-1]<0 )
account_id_debt_list


#set all balances less than zero to be zero in account_balance_list:


def islesszero(x):
    if x<0:
        x=0
    return x

map(islesszero, account_balance_list)




