import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.5, label='Actual Data')
    
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.title('CSIRO Adjusted Sea Level Over Time')    
    

    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = list(range(df['Year'].min(), 2051))
    sea_levels_predicted = [slope * year + intercept for year in years_extended]

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000].reset_index(drop=True)

    years_recent = list(range(2000, 2051))
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])

    sea_levels_predicted_recent = [slope_recent * year + intercept_recent for year in years_recent]
    
    slope_original, intercept_original, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended_original = list(range(df['Year'].min(), 2051))
    sea_levels_predicted_original = [slope_original * year + intercept_original for year in years_extended_original]
    
    plt.plot(years_extended_original, sea_levels_predicted_original, color='red', linestyle='dashed', label='Best Fit (All Data)')
    plt.plot(years_recent, sea_levels_predicted_recent, color='green', label='Best Fit (2000-Present)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()