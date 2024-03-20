import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
x = np.random.rand(10) * 10  # x-values
y = np.random.rand(10) * 10  # y-values
sizes = np.random.rand(10) * 100  # Initial bubble sizes

# Create the initial scatter plot with a larger figure size
plt.figure(figsize=(10, 6))
scatter = plt.scatter(x, y, s=sizes, alpha=0.5)
plt.title('Bubble Chart')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)

# Sample time period
time_period = np.arange(1, 101)  # 100 time steps

# Update the scatter plot for each time step
for t in time_period:
    # Adjust bubble sizes over time
    sizes = sizes + np.random.rand(10) * 100  # Add random values to current sizes

    # Update the scatter plot with new data
    scatter.set_offsets(np.column_stack((x, y)))  # Update bubble positions
    scatter.set_sizes(sizes)  # Update bubble sizes
    
    # Update the title to show the current time step
    plt.title(f'Bubble Chart - Time Step {t}')
    
    # Pause briefly to create the animation effect
    plt.pause(0.5)

# Display the plot after all time steps
plt.show()
