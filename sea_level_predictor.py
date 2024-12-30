import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.head()

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize=(16, 9))

    plt.scatter(x, y, color='blue', label='Data points')

    # Create first line of best fit
    lr1 = linregress(x, y)

    # Extend x values for the plot
    x_extended = pd.Series(range(1880, 2060))
    y_pred_extended = lr1.slope * x_extended + lr1.intercept  # Predicted y values

    predicted_df = pd.DataFrame({'Year': x_extended, 'Predicted Sea Level': y_pred_extended})


    # Plot original data and regression line
    
    plt.plot(x_extended, y_pred_extended, color='red', label=f'Regression line: y={lr1.slope:.2f}x+{lr1.intercept:.2f}')
    
    # Create second line of best fit
    df_2 = df[df['Year']>=2000]
    x2 = df_2['Year']
    y2 = df_2['CSIRO Adjusted Sea Level']

    lr2 =linregress(x2, y2)
    # Add labels and title
    x_extended2 = pd.Series(range(2000, 2060))
    y_pred_extended2 = lr2.slope * x_extended2 + lr2.intercept  # Predicted y values

    

# Plot original data and regression line
    plt.scatter(x2, y2, color='green', label='Data points')
    plt.plot(x_extended2, y_pred_extended2, color='purple', label=f'Regression line: y={lr2.slope:.2f}x+{lr2.intercept:.2f}')
    
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()