import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

# a) Line Plot
plt.plot(data['month_number'], data['total_profit'])
plt.show()

# b) Multiline Plot
plt.plot(data['month_number'], data['facecream'])
plt.plot(data['month_number'], data['facewash'])
plt.show()

# c) Bar Chart
plt.bar(data['month_number'], data['facecream'])
plt.bar(data['month_number'], data['facewash'])
plt.show()

# d) Pie Chart
total = [data['facecream'].sum(), data['facewash'].sum()]
labels = ['Face Cream', 'Face Wash']
plt.pie(total, labels=labels)
plt.show()