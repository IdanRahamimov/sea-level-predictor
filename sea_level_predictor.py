import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    slope, intercept, rvalue, pvalue, stderr = linregress(x, y)
    px = np.arange(1880, 2051, 1)
    py = slope*px + intercept
    plt.plot(px, py, label='prediction best line of fit')
  
    # Create second line of best fit
    recent_df = df[df['Year'] >= 2000]
    recent_x = recent_df['Year']
    recent_y = recent_df['CSIRO Adjusted Sea Level']
    slope, intercept, rvalue, pvalue, stderr = linregress(recent_x, recent_y)
    px = np.arange(2000, 2051, 1)
    py = slope*px + intercept
    plt.plot(px, py, label='prediction best line of fit')
  
    #Add labels and title
    
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()