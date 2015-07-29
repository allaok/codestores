__author__ = 'root'
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
month=0
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1
    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        newbalance += (monthlyInterestRate * newbalance)
        month += 1
print "Lowest Payment:",monthlyPayment
