import matplotlib.pyplot as plt

# Sample dataset
x = [1, 2, 3, 4, 5]  # x-values
y = [10, 15, 20, 25, 30]  # y-values
sizes = [100, 200, 300, 400, 500]  # Bubble sizes

# Plotting the bubble chart
plt.scatter(x, y, s=sizes, alpha=0.5)

# Customizing the plot
plt.title('Bubble Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Showing the plot
plt.show()
