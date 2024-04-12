
"""
income:
- how many income input?
  * different types of income sources
  * will input income at the end
  * calculates total

expenses:
- bills
- subscriptions
- other expenses
- not included

withdrawing money:
- savings account
- checking account
- cash
  * available cash to spend
  * should probably save
1. indicate how much is cash and will be put into checking and savings account 
"""

def calculateTotalIncome(x):
    incomeInfo = {
        "moneyIncome": [],
        "sourceIncome": []
    }

    i = "no"
    answer = "no"
    while i == answer:
        amountIncome = int(input("enter amount: "))
        sourceIncome = input("enter source: ")

        incomeInfo["money"].append(amountIncome)
        incomeInfo["source"].append(sourceIncome)

        answer = input("finish? answer, yes or no ").lower()

    else:
        print("test")

    print(incomeInfo)

def calculateExpense(y):
    expenseInfo = {
        "money": [],
        "expenseType": [],
        "expenseComments": []
    }

    expenseTypeOptions = {
       1: "bills",
       2: "" 
    }

    types = []

    i = "no"
    answer = "no"
    while i == answer:
        amountExpense = int(input("enter amount: "))
        expenseType = input("enter type: ")


        answer = input("finish? answer, yes or no ").lower()

