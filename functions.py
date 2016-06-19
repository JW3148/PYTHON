'''
Edit this file to complete the exercises in
'Writing Functions for Repeatability and Portability'
'''

def compute_monthly_interest(balance,apr_percent):
    '''
    Compute the monthly interest, based on a
    balance and an APR.

    Arguments:
    balance: The balance of an account.
    apr_percent: The APR as a percent (e.g. 19.99)

    Returns:
    interest: The amount of monthly interest owed on the
        balance, based on the APR
    '''
    
    interest = balance*apr_percent/100.0/12.0
    return interest

def compute_min_pay(balance, monthly_interest):
    '''
    Compute a minimum payment based on the following rules:
    1. if balance plus the monthly interest is less than 25,
        the balance plus the monthly interest.
    2. if 1% of the balance plus the monthly interest is
        less than 25, 25.
    3. otherwise, 1% of the balance plus the monthly interest.
    4. If the mininum payment is less than zero, set it to zero.

    Arguments:
    balance: The balance of the account.
    monthly_interest: The amount of monthly interest owed.

    Returns
    min_pay: The minimum payment owed, based on the above rules.
    '''
    if balance + monthly_interest < 25:
        min_pay = balance + monthly_interest
    elif 0.01 * balance + monthly_interest < 25:
        min_pay=25
    else:
        min_pay=0.01*balance+monthly_interest
    
    if min_pay<0:
        min_pay=0
        
    return min_pay

def compute_min_pay_list(balance_list, apr_percent=19.99):
    '''
    Compute the minimum payment (based on the same rules as
    'compute_min_pay', above) for a list of balances
    at a given APR.

    Arguments:
    balance_list: A list of balances.
    apr_percent: The APR for all of the balances.

    Returns:
    min_pay_list: A list of all the minimum payments owed,
        one for each balance.
    '''
    

def create_lambda():
    '''
    Return a lambda function that takes in a
    slope, intercept, and x-value (in that order),
    and computes the corresponding y-value for the line.

    Arguments:
    None

    Returns:
    lambda_line_compute: the lambda.
    '''
    return lambda x,y: x*y

print(create_lambda())
t= create_lambda()
type(t)

print
t(1,3)


if __name__ == "__main__":
    pass
