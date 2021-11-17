from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df[
        (df['value'] >= (df['value'].quantile(0.025))) & 
        (df['value'] <= (df['value'].quantile(0.975)))   
       ]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(15,10))
    plt.plot(df.index, df['value'],color='black')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    
    df_bar.reset_index(inplace=True)
    df_bar['date'] = pd.to_datetime(df_bar['date'])
    df_bar['year'] = [d.strftime('%Y') for d in df_bar.date]
    df_bar['month'] = [d.strftime('%m') for d in df_bar.date]

    # print(df_bar.dtypes)
    # print(df_bar.month)
    df_bar = df_bar.groupby(["year", "month"])["value"].mean()
    df_bar = df_bar.unstack()

    clist_new = ["Jan","Feb", "Mar", "Apr", "May","Jun","Jul","Aug", "Sep","Oct","Nov","Dec"]
    df_bar = df_bar.set_axis(clist_new, axis=1, inplace=False)
    # print(df_bar)
    
    # Draw bar plot
    fig = df_bar.plot(kind ="bar", legend = True, figsize = (15,10)).figure
    plt.xlabel("Years", fontsize= 10)
    plt.ylabel("Average Page Views", fontsize= 10)
    plt.legend(fontsize = 10, title="Months",labels=["January","February", "March", "April", "May","June","July","August", "September","October","November","December"])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['date'] = pd.to_datetime(df_box['date'])
    df_box['year'] = [d.strftime('%Y') for d in df_box.date]
    df_box['month'] = [d.strftime('%m') for d in df_box.date]
    # print(df_box['month'])

    # Draw box plots (using Seaborn)
    clist_new = ["Jan","Feb", "Mar", "Apr", "May","Jun","Jul","Aug", "Sep","Oct","Nov","Dec"]
    
     # Draw box plot
    fig,ax = plt.subplots(nrows=1,ncols=2)
    fig.set_size_inches(12, 5)
    fig.tight_layout(pad=4)
    sns.boxplot(x = df_box['year'], y = df_box['value'], ax = ax[0]).set(xlabel='Year', ylabel='Page Views')
    sns.boxplot(x = df_box['month'], y = df_box['value'],order=["Jan","Feb", "Mar", "Apr", "May","Jun","Jul","Aug", "Sep","Oct","Nov","Dec"], ax = ax[1]).set(xlabel='Month', ylabel='Page Views')

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
