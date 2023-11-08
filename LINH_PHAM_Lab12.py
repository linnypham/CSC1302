import pandas as pd

revenue = pd.Series([1000,900,1100,400,2000],['Mon','Tue','Wed','Thu','Fri'], name='revenue')
print(revenue)
print()

expenses = pd.Series([900,900,900,900,900],['Mon','Tue','Wed','Thu','Fri'], name='expenses')
print(expenses)
print()
print('Wed revenue: ', revenue.Wed)
print()
data = expenses.iloc[1:4]

print('expenses:')
print(data)
print()
net_profit = pd.Series(revenue - expenses)
print('Profit:')
print(net_profit)
print()
avg = sum(net_profit)/5
print("Average:", avg)
