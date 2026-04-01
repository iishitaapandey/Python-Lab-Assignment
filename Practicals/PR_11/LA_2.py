import matplotlib.pyplot as plt

companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Amdocs']
data = [120, 150, 180, 90, 95]

# a) Bar Chart
plt.bar(companies, data)
plt.show()

# b) Pie Chart
plt.pie(data, labels=companies)
plt.show()

# c) Doughnut Chart
plt.pie(data, labels=companies)
circle = plt.Circle((0,0),0.7,color='white')
plt.gca().add_artist(circle)
plt.show()

# d) Comparison
plt.bar(['IBM','Amdocs'], [90,95])
plt.show()