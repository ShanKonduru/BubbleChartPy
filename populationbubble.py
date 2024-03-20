import matplotlib.pyplot as plt
import numpy as np

# Sample dataset
countries = ['USA', 'China', 'India', 'Japan', 'Germany', 'UK', 'France', 'Brazil', 'Italy', 'Canada']
population = np.random.randint(100, 2000, size=len(countries)).astype(float)  # Initial population in millions as float
growth_rate = np.random.uniform(0.95, 1.05, size=len(countries))  # Growth rate for each country
data_values = population.copy()  # Initial data values for each country

# Create the initial scatter plot with a larger figure size
plt.figure(figsize=(12, 8))
scatter = plt.scatter(range(len(countries)), population, s=data_values*10, c=range(len(countries)), cmap='viridis', alpha=0.5)
plt.title('Bubble Chart - Population Growth')
plt.xlabel('Countries')
plt.ylabel('Population (Millions)')
plt.xticks(range(len(countries)), countries)  # Set country names as x-axis ticks
plt.grid(True)

# Add color bar legend
cbar = plt.colorbar(scatter)
cbar.set_label('Country Index')

# Update the scatter plot for each time step
for t in range(1, 51):  # 50 time steps
    # Update population using growth rate
    population *= growth_rate
    
    # Update bubble sizes and colors
    data_values = population.copy()
    scatter.set_sizes(data_values*10)
    scatter.set_array(np.arange(len(countries)))
    
    # Update the title to show the current time step
    plt.title(f'Bubble Chart - Population Growth (Time Step {t})')
    
    # Pause briefly to create the animation effect
    plt.pause(0.5)

# Display the plot after all time steps
plt.show()
