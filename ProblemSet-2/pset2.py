# Problem 1
# # Test Case 1:
# balance = 42
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
#
# # Result Your Code Should Generate Below:
# Remaining
# balance: 31.38
#
# # To make sure you are doing calculation correctly, this is the
# # remaining balance you should be getting at each month for this example
# Month 1 Remaining balance: 40.99
# Month 2 Remaining balance: 40.01
# Month 3 Remaining balance: 39.05
# Month 4 Remaining balance: 38.11
# Month 5 Remaining balance: 37.2
# Month 6 Remaining balance: 36.3
# Month 7 Remaining balance: 35.43
# Month 8 Remaining balance: 34.58
# Month 9 Remaining balance: 33.75
# Month 10 Remaining balance: 32.94
# Month 11 Remaining balance: 32.15
# Month 12 Remaining balance: 31.38

# balance = 5000
# payment = 5000*0.02 = 100
# unpaid  = 5000-100 = 4900
# interest = 4900*0.18/12.0 = 73.50
# next balance = 4900 + 73.50 = 4973.50

# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04

# # Paste your code into this box
for i in range(1, 12 + 1):
    payment = balance * monthlyPaymentRate
    unpaid = balance - payment
    interest = unpaid * (annualInterestRate / 12.0)
    remain = interest + unpaid
    balance = remain
print("Remaining balance: " + str(round(balance, 2)))

# Problem 2

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# Test Case 1:
# balance = 3926
# annualInterestRate = 0.2
# Result Your Code Should Generate:
# -------------------
# Lowest Payment: 310

total = balance
for payment in range(10, 500, 10):
    for j in range(1, 13):
        interest = annualInterestRate / 12.0
        unpaid = balance - payment
        remain = unpaid + (interest * unpaid)
        balance = remain
    if balance < 0:
        print("Lowest Payment: " + str(payment))
        break
    else:
        balance = total

# Problem 3

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0
# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2
# Result Your Code Should Generate:
# # -------------------
# Lowest Payment: 29157.09

total = balance
interest = annualInterestRate/12.0
lower = 0
upper = balance

for i in range (1,30):
    middle = (lower + upper) / 2.0
    for i in range(1, 13):
        unpaid = balance - middle
        remain = unpaid + (interest * unpaid)
        balance = remain
    if abs(balance) <= 0.05:
        print("Lowest Payment: " + str(round(middle,2)))
        break
    else:
        if round(balance,2) < 0:
            upper = middle
        else:
            lower = middle
        balance = total
